import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.application_defaults_view import ApplicationDefaultsView as ModelApplicationDefaultsView


class Defaults:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Defaults")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteApplicationDefaultsCommand(self) -> dict:
        """ Resets the Application Defaults to their default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/defaults/entities/application"),
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

    def getApplicationDefaultsCommand(self) -> ModelApplicationDefaultsView:
        """ Get the default application settings
        """
        try:
            response = self.session.get(
                url=self._build_uri("/defaults/entities/application"),
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
            return ModelApplicationDefaultsView.from_dict(response.json())

    def updateApplicationDefaultsCommand(self, Defaults: ModelApplicationDefaultsView) -> ModelApplicationDefaultsView:
        """ Update the default application settings
        """
        try:
            response = self.session.put(
                data=dumps(Defaults.to_dict(Defaults)),
                url=self._build_uri("/defaults/entities/application"),
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
            return ModelApplicationDefaultsView.from_dict(response.json())
