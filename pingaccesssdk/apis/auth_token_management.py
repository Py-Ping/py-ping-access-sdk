import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.auth_token_management_view import AuthTokenManagementView as ModelAuthTokenManagementView
from pingaccesssdk.models.key_set_view import KeySetView as ModelKeySetView


class AuthTokenManagement:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AuthTokenManagement")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteAuthTokenManagementCommand(self) -> dict:
        """ Resets the Auth Token Management configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/authTokenManagement"),
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

    def getAuthTokenManagementCommand(self) -> ModelAuthTokenManagementView:
        """ Get the Auth Token Management configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/authTokenManagement"),
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
            return ModelAuthTokenManagementView.from_dict(response.json())

    def updateAuthTokenManagementCommand(self, AuthTokenManagement: ModelAuthTokenManagementView) -> ModelAuthTokenManagementView:
        """ Update the Auth Token Management configuration
        """
        try:
            response = self.session.put(
                data=dumps(AuthTokenManagement.to_dict(AuthTokenManagement)),
                url=self._build_uri("/authTokenManagement"),
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
            return ModelAuthTokenManagementView.from_dict(response.json())

    def getAuthTokenKeySetCommand(self) -> ModelKeySetView:
        """ Get the Auth Token key set configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/authTokenManagement/keySet"),
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
            return ModelKeySetView.from_dict(response.json())

    def updateAuthTokenKeySetCommand(self, KeySet: ModelKeySetView) -> ModelKeySetView:
        """ Update the AuthToken key set configuration
        """
        try:
            response = self.session.put(
                data=dumps(KeySet.to_dict(KeySet)),
                url=self._build_uri("/authTokenManagement/keySet"),
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
            return ModelKeySetView.from_dict(response.json())
