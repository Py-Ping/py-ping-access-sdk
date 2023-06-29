import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView
from pingaccesssdk.models.hsm_provider_view import HsmProviderView as ModelHsmProviderView


class HsmProviders:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.HsmProviders")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getHsmProvidersCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelHsmProviderView:
        """ Get all HSM Providers
        """
        try:
            response = self.session.get(
                url=self._build_uri("/hsmProviders"),
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
            return ModelHsmProviderView.from_dict(response.json())

    def addHsmProviderCommand(self, HsmProvider: ModelHsmProviderView) -> ModelHsmProviderView:
        """ Create an HSM Provider
        """
        try:
            response = self.session.post(
                data=dumps(HsmProvider.to_dict(HsmProvider)),
                url=self._build_uri("/hsmProviders"),
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
            return ModelHsmProviderView.from_dict(response.json())

    def getHsmProviderDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all HSM Providers
        """
        try:
            response = self.session.get(
                url=self._build_uri("/hsmProviders/descriptors"),
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

    def deleteHsmProviderCommand(self, id: str) -> dict:
        """ Delete an HSM Provider
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/hsmProviders/{id}"),
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

    def getHsmProviderCommand(self, id: str) -> ModelHsmProviderView:
        """ Get an HSM Provider
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/hsmProviders/{id}"),
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
            return ModelHsmProviderView.from_dict(response.json())

    def updateHsmProviderCommand(self, id: str, HsmProvider: ModelHsmProviderView) -> ModelHsmProviderView:
        """ Update an HSM Provider
        """
        try:
            response = self.session.put(
                data=dumps(HsmProvider.to_dict(HsmProvider)),
                url=self._build_uri(f"/hsmProviders/{id}"),
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
            return ModelHsmProviderView.from_dict(response.json())
