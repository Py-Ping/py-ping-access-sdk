import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.engine_listener_view import EngineListenerView as ModelEngineListenerView
from pingaccesssdk.models.engine_listeners_view import EngineListenersView as ModelEngineListenersView


class EngineListeners:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.EngineListeners")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getEngineListenersCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelEngineListenersView:
        """ Get all Engine Listeners
        """
        try:
            response = self.session.get(
                url=self._build_uri("/engineListeners"),
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
            return ModelEngineListenersView.from_dict(response.json())

    def addEngineListenerCommand(self, EngineListener: ModelEngineListenerView) -> ModelEngineListenerView:
        """ Create an Engine Listener
        """
        try:
            response = self.session.post(
                data=dumps(EngineListener.to_dict(EngineListener)),
                url=self._build_uri("/engineListeners"),
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
            return ModelEngineListenerView.from_dict(response.json())

    def deleteEngineListenerCommand(self, id: str) -> dict:
        """ Delete an Engine Listener
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/engineListeners/{id}"),
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

    def getEngineListenerCommand(self, id: str) -> ModelEngineListenerView:
        """ Get an Engine Listener
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/engineListeners/{id}"),
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
            return ModelEngineListenerView.from_dict(response.json())

    def updateEngineListenerCommand(self, id: str, EngineListener: ModelEngineListenerView) -> ModelEngineListenerView:
        """ Update an Engine Listener
        """
        try:
            response = self.session.put(
                data=dumps(EngineListener.to_dict(EngineListener)),
                url=self._build_uri(f"/engineListeners/{id}"),
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
            return ModelEngineListenerView.from_dict(response.json())
