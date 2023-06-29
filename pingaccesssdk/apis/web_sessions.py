import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.web_sessions_view import WebSessionsView as ModelWebSessionsView
from pingaccesssdk.models.web_session_view import WebSessionView as ModelWebSessionView


class WebSessions:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.WebSessions")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getWebSessionsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelWebSessionsView:
        """ Get all WebSessions
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessions"),
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
            return ModelWebSessionsView.from_dict(response.json())

    def addWebSessionCommand(self, WebSessions: ModelWebSessionView) -> ModelWebSessionView:
        """ Create a WebSession
        """
        try:
            response = self.session.post(
                data=dumps(WebSessions.to_dict(WebSessions)),
                url=self._build_uri("/webSessions"),
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
            return ModelWebSessionView.from_dict(response.json())

    def deleteWebSessionCommand(self, id: str) -> dict:
        """ Delete a WebSession
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/webSessions/{id}"),
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

    def getWebSessionCommand(self, id: int) -> ModelWebSessionView:
        """ Get a WebSession
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/webSessions/{id}"),
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
            return ModelWebSessionView.from_dict(response.json())

    def updateWebSessionCommand(self, id: str, WebSessions: ModelWebSessionView) -> ModelWebSessionView:
        """ Update a WebSession
        """
        try:
            response = self.session.put(
                data=dumps(WebSessions.to_dict(WebSessions)),
                url=self._build_uri(f"/webSessions/{id}"),
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
            return ModelWebSessionView.from_dict(response.json())
