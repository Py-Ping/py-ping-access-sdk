import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.ping_one_4_c_view import PingOne4CView as ModelPingOne4CView
from pingaccesssdk.models.o_i_d_c_provider_metadata import OIDCProviderMetadata as ModelOIDCProviderMetadata


class Pingone:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Pingone")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deletePingOne4CCommand(self) -> dict:
        """ Resets the PingOne For Customers configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/pingone/customers"),
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

    def getPingOne4CCommand(self) -> ModelPingOne4CView:
        """ Get the PingOne For Customers configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingone/customers"),
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
            return ModelPingOne4CView.from_dict(response.json())

    def updatePingOne4CCommand(self, PingOneForCustomers: ModelPingOne4CView) -> ModelPingOne4CView:
        """ Update the PingOne For Customers configuration
        """
        try:
            response = self.session.put(
                data=dumps(PingOneForCustomers.to_dict(PingOneForCustomers)),
                url=self._build_uri("/pingone/customers"),
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
            return ModelPingOne4CView.from_dict(response.json())

    def getPingOne4CMetadataCommand(self) -> ModelOIDCProviderMetadata:
        """ Get the PingOne for Customers metadata
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingone/customers/metadata"),
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
            return ModelOIDCProviderMetadata.from_dict(response.json())
