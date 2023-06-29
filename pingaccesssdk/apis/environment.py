import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.environment_view import EnvironmentView as ModelEnvironmentView


class Environment:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Environment")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteEnvironmentCommand(self) -> dict:
        """ Resets the Environment configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/environment"),
                headers={"Content-Type": "application/json"}
            )
        except HTTPError as http_err:
            print(traceback.format_exc())
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise http_err
        except Exception as err:
            print(traceback.format_exc())
            self.logger.error(f"Error occurred: {err}")
            raise err
        else:
            print(response)
            return response.json()

    def getEnvironmentCommand(self) -> ModelEnvironmentView:
        """ Get the Environment
        """
        try:
            response = self.session.get(
                url=self._build_uri("/environment"),
                headers={"Content-Type": "application/json"}
            )
        except HTTPError as http_err:
            print(traceback.format_exc())
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise http_err
        except Exception as err:
            print(traceback.format_exc())
            self.logger.error(f"Error occurred: {err}")
            raise err
        else:
            print(response)
            return ModelEnvironmentView.from_dict(response.json())

    def updateEnvironmentCommand(self, _environment: ModelEnvironmentView) -> ModelEnvironmentView:
        """ Update the Environment
        """
        try:
            response = self.session.put(
                data=dumps(_environment.to_dict(_environment)),
                url=self._build_uri("/environment"),
                headers={"Content-Type": "application/json"}
            )
        except HTTPError as http_err:
            print(traceback.format_exc())
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise http_err
        except Exception as err:
            print(traceback.format_exc())
            self.logger.error(f"Error occurred: {err}")
            raise err
        else:
            print(response)
            return ModelEnvironmentView.from_dict(response.json())
