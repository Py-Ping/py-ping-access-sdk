import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.virtual_host_view import VirtualHostView as ModelVirtualHostView
from pingaccesssdk.models.virtual_hosts_view import VirtualHostsView as ModelVirtualHostsView


class Virtualhosts:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Virtualhosts")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getVirtualHostsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, virtualHost: str = None, sortKey: str = None, order: str = None) -> ModelVirtualHostsView:
        """ Get all Virtual Hosts
        """
        try:
            response = self.session.get(
                url=self._build_uri("/virtualhosts"),
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
            return ModelVirtualHostsView.from_dict(response.json())

    def addVirtualHostCommand(self, VirtualHost: ModelVirtualHostView) -> ModelVirtualHostView:
        """ Create a Virtual Host
        """
        try:
            response = self.session.post(
                data=dumps(VirtualHost.to_dict(VirtualHost)),
                url=self._build_uri("/virtualhosts"),
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
            return ModelVirtualHostView.from_dict(response.json())

    def deleteVirtualHostCommand(self, id: str) -> dict:
        """ Delete a Virtual Host
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/virtualhosts/{id}"),
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

    def getVirtualHostCommand(self, id: str) -> ModelVirtualHostView:
        """ Get a Virtual Host
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/virtualhosts/{id}"),
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
            return ModelVirtualHostView.from_dict(response.json())

    def updateVirtualHostCommand(self, id: str, VirtualHost: ModelVirtualHostView) -> ModelVirtualHostView:
        """ Update a Virtual Host
        """
        try:
            response = self.session.put(
                data=dumps(VirtualHost.to_dict(VirtualHost)),
                url=self._build_uri(f"/virtualhosts/{id}"),
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
            return ModelVirtualHostView.from_dict(response.json())
