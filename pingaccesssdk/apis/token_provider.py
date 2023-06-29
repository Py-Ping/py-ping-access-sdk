import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.token_provider_setting_view import TokenProviderSettingView as ModelTokenProviderSettingView


class TokenProvider:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.TokenProvider")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteTokenProviderSettingCommand(self) -> dict:
        """ Resets the Token Provider settings to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/tokenProvider/settings"),
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

    def getTokenProviderSettingCommand(self) -> ModelTokenProviderSettingView:
        """ Get the Token Provider settings
        """
        try:
            response = self.session.get(
                url=self._build_uri("/tokenProvider/settings"),
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
            return ModelTokenProviderSettingView.from_dict(response.json())

    def updateTokenProviderSettingCommand(self, TokenProviderSettings: ModelTokenProviderSettingView) -> ModelTokenProviderSettingView:
        """ Update the Token Provider setting
        """
        try:
            response = self.session.put(
                data=dumps(TokenProviderSettings.to_dict(TokenProviderSettings)),
                url=self._build_uri("/tokenProvider/settings"),
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
            return ModelTokenProviderSettingView.from_dict(response.json())
