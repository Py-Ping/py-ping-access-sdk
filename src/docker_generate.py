
import docker
import traceback
import os
import logging
import argparse

from helpers import get_auth_session, retry_with_backoff
from generate import Generate
from time import sleep

parser = argparse.ArgumentParser(description='PyLogger Generator')


def add_args():
    parser.add_argument(
        'version', type=str, choices=["5.3.2", "6.0.4", "6.1.0", "edge"],
        default="edge", help='Ping Access Version'
    )


class Container:
    """
        Manager class for the SDK generator, encapsulates the process in a
        docker container such that there is no external dependency on a
        live ping access instance

        TODO: make generic to run any other Ping solution
    """

    def __init__(self, home_path, user, pass_key, version="edge"):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p"
        )
        self.logger = logging.getLogger("PingSDK.Docker")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))

        self.client = docker.from_env()
        self.image_name = f"pingidentity/pingaccess:{version}"
        self.home = home_path
        self.ping_user = user
        self.ping_key = pass_key

        self.container = None

    def run(self):
        self.logger.info(f'Starting Container: {self.image_name}')
        self.container = self.client.containers.run(
            self.image_name,
            environment=[
                "PING_IDENTITY_ACCEPT_EULA=YES",
                f"PING_IDENTITY_DEVOPS_USER={self.ping_user}",
                f"PING_IDENTITY_DEVOPS_KEY={self.ping_key}",
                f"PING_IDENTITY_DEVOPS_HOME={self.home}/projects/devops",
                "PING_IDENTITY_DEVOPS_REGISTRY=docker.io/pingidentity",
                "PING_IDENTITY_DEVOPS_TAG=edge"
            ],
            name="pingaccess",
            ports={"443/tcp": 443, "9000/tcp": 9000},
            detach=True
        )

    def terminate(self):
        """
            Perform post generation cleanup
        """
        self.container.stop()
        self.container.wait()
        self.container.remove()

    def get_by_image_name(self, image_name):
        """
            Given an image name, return the first available container object.
        """
        for container in self.client.containers.list():
            if container.image.tags[0] == image_name:
                return container

    def wait(self):
        """
            Block execution until the container is paused, exited or running.
        """
        while self.container.status not in ["running", "exited", "paused"]:
            self.container = self.client.containers.get(self.container.id)
            sleep(5)

    def running(self, image_name):
        """
            Given an image name, return if currently running
        """
        for container in self.client.containers.list():
            if container.image.tags[0] == image_name:
                return True
        return False

    def __enter__(self):
        """
            Enter method to setup a Ping Access container
        """
        if not self.running(self.image_name):
            self.logger.info("Initialising Ping Access container...")
            self.run()
            self.wait()
        else:
            self.container = self.get_by_image_name(self.image_name)

        # replace with something that polls on service availability
        sleep(45)
        self.logger.info("Container ready, generating SDK objects...")
        return self.container

    def __exit__(self, type, value, traceback):
        """
            Exit method to cleanup Ping Access container when done
        """
        self.logger.info("Terminating container...")
        self.logger.debug("Terminating container...")
        self.terminate()


if __name__ == "__main__":
    add_args()
    args = parser.parse_args()
    home = os.environ["HOME"]
    ping_user = os.environ["PING_IDENTITY_DEVOPS_USER"]
    ping_key = os.environ["PING_IDENTITY_DEVOPS_KEY"]
    endpoint = "https://localhost:9000/pa-admin-api/v3"
    swagger_url = f"{endpoint}/api-docs/pa/api-docs.json"
    session = get_auth_session()
    session.verify = False
    session.auth = ('administrator', '2Access')

    with Container(home, ping_user, ping_key, args.version) as container:
        print(f'Running container {container.id}')
        if not retry_with_backoff(Generate(swagger_url).generate):
            print("Container service didn't stabilise, exiting...")
            exit(1)
        try:
            version = __import__("pingaccesssdk.apis.version", fromlist=[""])
            response = version.Version(endpoint, session).versionCommand()
            print(f"Ping Access, version: {response.version}")
        except Exception as err:
            print(f"Was unable to determine the Ping Access version: {err}")
            print(traceback.format_exc())
        finally:
            print("Ping Access SDK Generation Finished")
