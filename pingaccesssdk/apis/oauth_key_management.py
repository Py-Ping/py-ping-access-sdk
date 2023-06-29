import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.o_auth_key_management_view import OAuthKeyManagementView as ModelOAuthKeyManagementView
from pingaccesssdk.models.key_set_view import KeySetView as ModelKeySetView


class OauthKeyManagement:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthKeyManagement")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteOAuthKeyManagementCommand(self) -> dict:
        """ Resets the OAuth Key Management configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/oauthKeyManagement"),
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

    def getOAuthKeyManagementCommand(self) -> ModelOAuthKeyManagementView:
        """ Get the OAuth Key Management configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/oauthKeyManagement"),
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
            return ModelOAuthKeyManagementView.from_dict(response.json())

    def updateOAuthKeyManagementCommand(self, OAuthKeyManagement: ModelOAuthKeyManagementView) -> ModelOAuthKeyManagementView:
        """ Update the OAuth Key Management configuration
        """
        try:
            response = self.session.put(
                data=dumps(OAuthKeyManagement.to_dict(OAuthKeyManagement)),
                url=self._build_uri("/oauthKeyManagement"),
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
            return ModelOAuthKeyManagementView.from_dict(response.json())

    def getOAuthKeySetCommand(self) -> ModelKeySetView:
        """ Get the OAuth key set configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/oauthKeyManagement/keySet"),
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

    def updateOAuthKeySetCommand(self, KeySet: ModelKeySetView) -> ModelKeySetView:
        """ Update the OAuth key set configuration
        """
        try:
            response = self.session.put(
                data=dumps(KeySet.to_dict(KeySet)),
                url=self._build_uri("/oauthKeyManagement/keySet"),
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
