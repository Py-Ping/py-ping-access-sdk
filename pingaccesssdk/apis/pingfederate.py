import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.o_i_d_c_provider_metadata import OIDCProviderMetadata as ModelOIDCProviderMetadata
from pingaccesssdk.models.ping_federate_metadata_runtime_view import PingFederateMetadataRuntimeView as ModelPingFederateMetadataRuntimeView
from pingaccesssdk.models.ping_federate_access_token_view import PingFederateAccessTokenView as ModelPingFederateAccessTokenView
from pingaccesssdk.models.ping_federate_admin_view import PingFederateAdminView as ModelPingFederateAdminView
from pingaccesssdk.models.ping_federate_runtime_view import PingFederateRuntimeView as ModelPingFederateRuntimeView


class Pingfederate:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Pingfederate")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deletePingFederateCommand(self) -> dict:
        """ Resets the PingFederate configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/pingfederate"),
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

    def getPingFederateCommand(self) -> ModelPingFederateRuntimeView:
        """ Get the PingFederate configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingfederate"),
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
            return ModelPingFederateRuntimeView.from_dict(response.json())

    def updatePingFederateCommand(self, PingFederate: ModelPingFederateRuntimeView) -> ModelPingFederateRuntimeView:
        """ Update the PingFederate configuration
        """
        try:
            response = self.session.put(
                data=dumps(PingFederate.to_dict(PingFederate)),
                url=self._build_uri("/pingfederate"),
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
            return ModelPingFederateRuntimeView.from_dict(response.json())

    def deletePingFederateAccessTokensCommand(self) -> dict:
        """ Resets the PingAccess OAuth Client configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/pingfederate/accessTokens"),
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

    def getPingFederateAccessTokensCommand(self) -> ModelPingFederateAccessTokenView:
        """ Get the PingAccess OAuth Client configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingfederate/accessTokens"),
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
            return ModelPingFederateAccessTokenView.from_dict(response.json())

    def updatePingFederateAccessTokensCommand(self, PingFederateAccessToken: ModelPingFederateAccessTokenView) -> ModelPingFederateAccessTokenView:
        """ Update the PingFederate OAuth Client configuration
        """
        try:
            response = self.session.put(
                data=dumps(PingFederateAccessToken.to_dict(PingFederateAccessToken)),
                url=self._build_uri("/pingfederate/accessTokens"),
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
            return ModelPingFederateAccessTokenView.from_dict(response.json())

    def deletePingFederateAdminCommand(self) -> dict:
        """ Resets the PingFederate Admin configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/pingfederate/admin"),
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

    def getPingFederateAdminCommand(self) -> ModelPingFederateAdminView:
        """ Get the PingFederate Admin configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingfederate/admin"),
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
            return ModelPingFederateAdminView.from_dict(response.json())

    def updatePingFederateAdminCommand(self, PingFederate: ModelPingFederateAdminView) -> ModelPingFederateAdminView:
        """ Update the PingFederate Admin configuration
        """
        try:
            response = self.session.put(
                data=dumps(PingFederate.to_dict(PingFederate)),
                url=self._build_uri("/pingfederate/admin"),
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
            return ModelPingFederateAdminView.from_dict(response.json())

    def getPingFederateMetadataCommand(self) -> ModelOIDCProviderMetadata:
        """ Get the PingFederate metadata
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingfederate/metadata"),
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

    def deletePingFederateRuntimeCommand(self) -> dict:
        """ Resets the PingFederate configuration
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/pingfederate/runtime"),
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

    def getPingFederateRuntimeCommand(self) -> ModelPingFederateMetadataRuntimeView:
        """ Get the PingFederate configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingfederate/runtime"),
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
            return ModelPingFederateMetadataRuntimeView.from_dict(response.json())

    def updatePingFederateRuntimeCommand(self, PingFederate: ModelPingFederateMetadataRuntimeView) -> ModelPingFederateMetadataRuntimeView:
        """ Update the PingFederate configuration
        """
        try:
            response = self.session.put(
                data=dumps(PingFederate.to_dict(PingFederate)),
                url=self._build_uri("/pingfederate/runtime"),
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
            return ModelPingFederateMetadataRuntimeView.from_dict(response.json())

    def getPingFederateRuntimeMetadataCommand(self) -> ModelOIDCProviderMetadata:
        """ Get the PingFederate Runtime metadata
        """
        try:
            response = self.session.get(
                url=self._build_uri("/pingfederate/runtime/metadata"),
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
