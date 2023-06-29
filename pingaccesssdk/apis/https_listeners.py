import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.https_listeners_view import HttpsListenersView as ModelHttpsListenersView
from pingaccesssdk.models.https_listener_view import HttpsListenerView as ModelHttpsListenerView


class HttpsListeners:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.HttpsListeners")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getHttpsListenersCommand(self, sortKey: str = None, order: str = None) -> ModelHttpsListenersView:
        """ Get all HTTPS Listeners
        """
        try:
            response = self.session.get(
                url=self._build_uri("/httpsListeners"),
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
            return ModelHttpsListenersView.from_dict(response.json())

    def getHttpsListenerCommand(self, id: str) -> ModelHttpsListenerView:
        """ Get an HTTPS Listener
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/httpsListeners/{id}"),
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
            return ModelHttpsListenerView.from_dict(response.json())

    def updateHttpsListener(self, id: str, HttpsListeners: ModelHttpsListenerView) -> ModelHttpsListenerView:
        """ Update an HTTPS Listener
        """
        try:
            response = self.session.put(
                data=dumps(HttpsListeners.to_dict(HttpsListeners)),
                url=self._build_uri(f"/httpsListeners/{id}"),
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
            return ModelHttpsListenerView.from_dict(response.json())
