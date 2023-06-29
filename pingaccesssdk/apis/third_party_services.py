import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.third_party_service_view import ThirdPartyServiceView as ModelThirdPartyServiceView
from pingaccesssdk.models.third_party_services_view import ThirdPartyServicesView as ModelThirdPartyServicesView


class ThirdPartyServices:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.ThirdPartyServices")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getThirdPartyServicesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelThirdPartyServicesView:
        """ Get all Third-Party Services
        """
        try:
            response = self.session.get(
                url=self._build_uri("/thirdPartyServices"),
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
            return ModelThirdPartyServicesView.from_dict(response.json())

    def addThirdPartyServiceCommand(self, ThirdPartyService: ModelThirdPartyServiceView) -> ModelThirdPartyServiceView:
        """ Create a Third-Party Service
        """
        try:
            response = self.session.post(
                data=dumps(ThirdPartyService.to_dict(ThirdPartyService)),
                url=self._build_uri("/thirdPartyServices"),
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
            return ModelThirdPartyServiceView.from_dict(response.json())

    def deleteThirdPartyServiceCommand(self, id: str) -> dict:
        """ Delete a Third-Party Service
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/thirdPartyServices/{id}"),
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

    def getThirdPartyServiceCommand(self, id: str) -> ModelThirdPartyServiceView:
        """ Get a Third-Party Service
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/thirdPartyServices/{id}"),
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
            return ModelThirdPartyServiceView.from_dict(response.json())

    def updateThirdPartyServiceCommand(self, id: str, ThirdPartyService: ModelThirdPartyServiceView) -> ModelThirdPartyServiceView:
        """ Update a Third-Party Service
        """
        try:
            response = self.session.put(
                data=dumps(ThirdPartyService.to_dict(ThirdPartyService)),
                url=self._build_uri(f"/thirdPartyServices/{id}"),
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
            return ModelThirdPartyServiceView.from_dict(response.json())
