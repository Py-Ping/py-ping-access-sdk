import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.shared_secrets_view import SharedSecretsView as ModelSharedSecretsView
from pingaccesssdk.models.shared_secret_view import SharedSecretView as ModelSharedSecretView


class SharedSecrets:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.SharedSecrets")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSharedSecretsCommand(self, sortKey: str = None, order: str = None) -> ModelSharedSecretsView:
        """ Get all Shared Secrets
        """
        try:
            response = self.session.get(
                url=self._build_uri("/sharedSecrets"),
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
            return ModelSharedSecretsView.from_dict(response.json())

    def addSharedSecretCommand(self, _sharedSecrets: ModelSharedSecretView) -> ModelSharedSecretView:
        """ Create a Shared Secret
        """
        try:
            response = self.session.post(
                data=dumps(_sharedSecrets.to_dict(_sharedSecrets)),
                url=self._build_uri("/sharedSecrets"),
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
            return ModelSharedSecretView.from_dict(response.json())

    def deleteSharedSecretCommand(self, id: str) -> dict:
        """ Delete a Shared Secret
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/sharedSecrets/{id}"),
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

    def getSharedSecretCommand(self, id: str) -> ModelSharedSecretView:
        """ Get a Shared Secret
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/sharedSecrets/{id}"),
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
            return ModelSharedSecretView.from_dict(response.json())
