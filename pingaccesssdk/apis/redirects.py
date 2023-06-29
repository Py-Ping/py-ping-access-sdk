import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.redirects_view import RedirectsView as ModelRedirectsView
from pingaccesssdk.models.redirect_view import RedirectView as ModelRedirectView


class Redirects:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Redirects")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getRedirectsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, source: str = None, target: str = None, sortKey: str = None, order: str = None) -> ModelRedirectsView:
        """ Get all Redirects
        """
        try:
            response = self.session.get(
                url=self._build_uri("/redirects"),
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
            return ModelRedirectsView.from_dict(response.json())

    def addRedirectCommand(self, Redirects: ModelRedirectView) -> ModelRedirectView:
        """ Add a Redirect
        """
        try:
            response = self.session.post(
                data=dumps(Redirects.to_dict(Redirects)),
                url=self._build_uri("/redirects"),
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
            return ModelRedirectView.from_dict(response.json())

    def deleteRedirectCommand(self, id: str) -> dict:
        """ Delete a Redirect
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/redirects/{id}"),
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

    def getRedirectCommand(self, id: str) -> ModelRedirectView:
        """ Get a Redirect
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/redirects/{id}"),
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
            return ModelRedirectView.from_dict(response.json())

    def updateRedirectCommand(self, id: str, Redirects: ModelRedirectView) -> ModelRedirectView:
        """ Update a Redirect
        """
        try:
            response = self.session.put(
                data=dumps(Redirects.to_dict(Redirects)),
                url=self._build_uri(f"/redirects/{id}"),
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
            return ModelRedirectView.from_dict(response.json())
