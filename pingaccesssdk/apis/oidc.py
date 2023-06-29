import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.o_i_d_c_provider_view import OIDCProviderView as ModelOIDCProviderView
from pingaccesssdk.models.o_i_d_c_provider_metadata import OIDCProviderMetadata as ModelOIDCProviderMetadata
from pingaccesssdk.models.descriptor_view import DescriptorView as ModelDescriptorView
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView


class Oidc:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Oidc")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteOIDCProviderCommand(self) -> dict:
        """ Resets the OpenID Connect Provider configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/oidc/provider"),
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

    def getOIDCProviderCommand(self) -> ModelOIDCProviderView:
        """ Get the OpenID Connect Provider configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/oidc/provider"),
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
            return ModelOIDCProviderView.from_dict(response.json())

    def updateOIDCProviderCommand(self, OpenIDConnectProvider: ModelOIDCProviderView) -> ModelOIDCProviderView:
        """ Update the OpenID Connect Provider configuration
        """
        try:
            response = self.session.put(
                data=dumps(OpenIDConnectProvider.to_dict(OpenIDConnectProvider)),
                url=self._build_uri("/oidc/provider"),
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
            return ModelOIDCProviderView.from_dict(response.json())

    def getOIDCProviderPluginDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all OIDC Provider plugins
        """
        try:
            response = self.session.get(
                url=self._build_uri("/oidc/provider/descriptors"),
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

    def getOIDCProviderPluginDescriptorCommand(self, pluginType: str) -> ModelDescriptorView:
        """ Get a descriptor for a OIDC Provider plugin
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/oidc/provider/descriptors/{pluginType}"),
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

    def getOIDCProviderMetadataCommand(self) -> ModelOIDCProviderMetadata:
        """ Get the OpenID Connect Provider's metadata
        """
        try:
            response = self.session.get(
                url=self._build_uri("/oidc/provider/metadata"),
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
