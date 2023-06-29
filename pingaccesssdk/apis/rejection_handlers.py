import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.descriptor_view import DescriptorView as ModelDescriptorView
from pingaccesssdk.models.rejection_handlers_view import RejectionHandlersView as ModelRejectionHandlersView
from pingaccesssdk.models.rejection_handler_view import RejectionHandlerView as ModelRejectionHandlerView
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView


class RejectionHandlers:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.RejectionHandlers")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getRejectionHandlersCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelRejectionHandlersView:
        """ Get all Rejection Handlers
        """
        try:
            response = self.session.get(
                url=self._build_uri("/rejectionHandlers"),
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
            return ModelRejectionHandlersView.from_dict(response.json())

    def addRejectionHandlerCommand(self, RejectionHandler: ModelRejectionHandlerView) -> ModelRejectionHandlerView:
        """ Create a Rejection Handler
        """
        try:
            response = self.session.post(
                data=dumps(RejectionHandler.to_dict(RejectionHandler)),
                url=self._build_uri("/rejectionHandlers"),
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
            return ModelRejectionHandlerView.from_dict(response.json())

    def getRejectionHandlerDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all supported Rejection Handler types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/rejectionHandlers/descriptors"),
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
            return ModelDescriptorsView.from_dict(response.json())

    def getRejecitonHandlerDescriptorCommand(self, rejectionHandlerType: str) -> ModelDescriptorView:
        """ Get descriptor for a Rejection Handler type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/rejectionHandlers/descriptors/{rejectionHandlerType}"),
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
            return ModelDescriptorView.from_dict(response.json())

    def deleteRejectionHandlerCommand(self, id: str) -> dict:
        """ Delete a Rejection Handler
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/rejectionHandlers/{id}"),
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

    def getRejectionHandlerCommand(self, id: str) -> ModelRejectionHandlerView:
        """ Get a Rejection Handler
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/rejectionHandlers/{id}"),
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
            return ModelRejectionHandlerView.from_dict(response.json())

    def updateRejectionHandlerCommand(self, id: str, RejectionHandler: ModelRejectionHandlerView) -> ModelRejectionHandlerView:
        """ Update a Rejection Handler
        """
        try:
            response = self.session.put(
                data=dumps(RejectionHandler.to_dict(RejectionHandler)),
                url=self._build_uri(f"/rejectionHandlers/{id}"),
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
            return ModelRejectionHandlerView.from_dict(response.json())
