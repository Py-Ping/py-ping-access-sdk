import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.sideband_client_view import SidebandClientView as ModelSidebandClientView
from pingaccesssdk.models.sideband_clients_view import SidebandClientsView as ModelSidebandClientsView


class SidebandClients:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.SidebandClients")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSidebandClientsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelSidebandClientsView:
        """ Get all Sideband Clients
        """
        try:
            response = self.session.get(
                url=self._build_uri("/sidebandClients"),
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
            return ModelSidebandClientsView.from_dict(response.json())

    def addSidebandClientCommand(self, SidebandClient: ModelSidebandClientView) -> ModelSidebandClientView:
        """ Create a Sideband Client
        """
        try:
            response = self.session.post(
                data=dumps(SidebandClient.to_dict(SidebandClient)),
                url=self._build_uri("/sidebandClients"),
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
            return ModelSidebandClientView.from_dict(response.json())

    def deleteSidebandClientCommand(self, id: str) -> dict:
        """ Delete a Sideband Client
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/sidebandClients/{id}"),
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

    def getSidebandClientCommand(self, id: str) -> ModelSidebandClientView:
        """ Get a Sideband Client
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/sidebandClients/{id}"),
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
            return ModelSidebandClientView.from_dict(response.json())

    def updateSidebandClientCommand(self, id: str, SidebandClient: ModelSidebandClientView) -> ModelSidebandClientView:
        """ Update a Sideband Client
        """
        try:
            response = self.session.put(
                data=dumps(SidebandClient.to_dict(SidebandClient)),
                url=self._build_uri(f"/sidebandClients/{id}"),
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
            return ModelSidebandClientView.from_dict(response.json())
