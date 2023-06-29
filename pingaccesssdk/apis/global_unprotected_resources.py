import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.global_unprotected_resource_view import GlobalUnprotectedResourceView as ModelGlobalUnprotectedResourceView
from pingaccesssdk.models.global_unprotected_resources_view import GlobalUnprotectedResourcesView as ModelGlobalUnprotectedResourcesView


class GlobalUnprotectedResources:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.GlobalUnprotectedResources")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getGlobalUnprotectedResourcesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelGlobalUnprotectedResourcesView:
        """ Get all Global Unprotected Resources
        """
        try:
            response = self.session.get(
                url=self._build_uri("/globalUnprotectedResources"),
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
            return ModelGlobalUnprotectedResourcesView.from_dict(response.json())

    def addGlobalUnprotectedResourceCommand(self, GlobalUnprotectedResource: ModelGlobalUnprotectedResourceView) -> ModelGlobalUnprotectedResourceView:
        """ Add a Global Unprotected Resource
        """
        try:
            response = self.session.post(
                data=dumps(GlobalUnprotectedResource.to_dict(GlobalUnprotectedResource)),
                url=self._build_uri("/globalUnprotectedResources"),
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
            return ModelGlobalUnprotectedResourceView.from_dict(response.json())

    def deleteGlobalUnprotectedResourceCommand(self, id: str) -> dict:
        """ Delete a Global Unprotected Resource
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/globalUnprotectedResources/{id}"),
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

    def getGlobalUnprotectedResourceCommand(self, id: str) -> ModelGlobalUnprotectedResourceView:
        """ Get a Global Unprotected Resource
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/globalUnprotectedResources/{id}"),
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
            return ModelGlobalUnprotectedResourceView.from_dict(response.json())

    def updateGlobalUnprotectedResourceCommand(self, id: str, GlobalUnprotectedResource: ModelGlobalUnprotectedResourceView) -> ModelGlobalUnprotectedResourceView:
        """ Update a Global Unprotected Resource
        """
        try:
            response = self.session.put(
                data=dumps(GlobalUnprotectedResource.to_dict(GlobalUnprotectedResource)),
                url=self._build_uri(f"/globalUnprotectedResources/{id}"),
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
            return ModelGlobalUnprotectedResourceView.from_dict(response.json())
