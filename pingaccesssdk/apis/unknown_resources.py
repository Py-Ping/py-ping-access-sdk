import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.unknown_resource_settings_view import UnknownResourceSettingsView as ModelUnknownResourceSettingsView


class UnknownResources:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.UnknownResources")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def delete(self) -> dict:
        """ Resets the global settings for unknown resources to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/unknownResources/settings"),
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

    def get(self) -> ModelUnknownResourceSettingsView:
        """ Retrieves the global settings for unknown resources
        """
        try:
            response = self.session.get(
                url=self._build_uri("/unknownResources/settings"),
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
            return ModelUnknownResourceSettingsView.from_dict(response.json())

    def update(self, settings: ModelUnknownResourceSettingsView) -> ModelUnknownResourceSettingsView:
        """ Updates the global settings for unknown resources
        """
        try:
            response = self.session.put(
                data=dumps(settings.to_dict(settings)),
                url=self._build_uri("/unknownResources/settings"),
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
            return ModelUnknownResourceSettingsView.from_dict(response.json())
