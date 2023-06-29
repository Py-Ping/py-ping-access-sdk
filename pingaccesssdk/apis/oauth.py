import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.authorization_server_view import AuthorizationServerView as ModelAuthorizationServerView


class Oauth:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Oauth")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteAuthorizationServerCommand(self) -> dict:
        """ Resets the OpenID Connect Provider configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/oauth/authServer"),
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

    def getAuthorizationServerCommand(self) -> ModelAuthorizationServerView:
        """ Get Authorization Server configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/oauth/authServer"),
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
            return ModelAuthorizationServerView.from_dict(response.json())

    def updateAuthorizationServerCommand(self, OpenIDConnectProvider: ModelAuthorizationServerView) -> ModelAuthorizationServerView:
        """ Update OAuth 2.0 Authorization Server configuration
        """
        try:
            response = self.session.put(
                data=dumps(OpenIDConnectProvider.to_dict(OpenIDConnectProvider)),
                url=self._build_uri("/oauth/authServer"),
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
            return ModelAuthorizationServerView.from_dict(response.json())
