import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.authn_req_lists_view import AuthnReqListsView as ModelAuthnReqListsView
from pingaccesssdk.models.authn_req_list_view import AuthnReqListView as ModelAuthnReqListView


class AuthnReqLists:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AuthnReqLists")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAuthnReqListsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelAuthnReqListsView:
        """ Get all Authentication Requirement Lists
        """
        try:
            response = self.session.get(
                url=self._build_uri("/authnReqLists"),
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
            return ModelAuthnReqListsView.from_dict(response.json())

    def addAuthnReqListCommand(self, AuthnReqList: ModelAuthnReqListView) -> ModelAuthnReqListView:
        """ Add an Authentication Requirement List
        """
        try:
            response = self.session.post(
                data=dumps(AuthnReqList.to_dict(AuthnReqList)),
                url=self._build_uri("/authnReqLists"),
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
            return ModelAuthnReqListView.from_dict(response.json())

    def deleteAuthnReqListCommand(self, id: str) -> dict:
        """ Delete an Authentication Requirement List
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/authnReqLists/{id}"),
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

    def getAuthnReqListCommand(self, id: str) -> ModelAuthnReqListView:
        """ Get an Authentication Requirement List
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/authnReqLists/{id}"),
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
            return ModelAuthnReqListView.from_dict(response.json())

    def updateAuthnReqListCommand(self, id: str, AuthnReqList: ModelAuthnReqListView) -> ModelAuthnReqListView:
        """ Update an Authentication Requirement List
        """
        try:
            response = self.session.put(
                data=dumps(AuthnReqList.to_dict(AuthnReqList)),
                url=self._build_uri(f"/authnReqLists/{id}"),
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
            return ModelAuthnReqListView.from_dict(response.json())
