import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.admin_token_provider_view import AdminTokenProviderView as ModelAdminTokenProviderView
from pingaccesssdk.models.basic_auth_config_view import BasicAuthConfigView as ModelBasicAuthConfigView
from pingaccesssdk.models.oidc_config_view import OidcConfigView as ModelOidcConfigView
from pingaccesssdk.models.basic_config import BasicConfig as ModelBasicConfig
from pingaccesssdk.models.o_auth_config_view import OAuthConfigView as ModelOAuthConfigView
from pingaccesssdk.models.o_i_d_c_provider_metadata import OIDCProviderMetadata as ModelOIDCProviderMetadata
from pingaccesssdk.models.admin_basic_web_session_view import AdminBasicWebSessionView as ModelAdminBasicWebSessionView
from pingaccesssdk.models.supported_scopes_view import SupportedScopesView as ModelSupportedScopesView


class Auth:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Auth")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteBasicAuthCommand(self) -> dict:
        """ Resets the HTTP Basic Authentication configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/auth/basic"),
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

    def getBasicAuthCommand(self) -> ModelBasicConfig:
        """ Get the HTTP Basic Authentication configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/auth/basic"),
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
            return ModelBasicConfig.from_dict(response.json())

    def updateBasicAuthCommand(self, BasicConfig: ModelBasicAuthConfigView) -> ModelBasicAuthConfigView:
        """ Update the Basic Authentication configuration
        """
        try:
            response = self.session.put(
                data=dumps(BasicConfig.to_dict(BasicConfig)),
                url=self._build_uri("/auth/basic"),
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
            return ModelBasicAuthConfigView.from_dict(response.json())

    def deleteOAuthAuthCommand(self) -> dict:
        """ Resets the OAuth Authentication configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/auth/oauth"),
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

    def getOAuthAuthCommand(self) -> ModelOAuthConfigView:
        """ Get the OAuth Authentication configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/auth/oauth"),
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
            return ModelOAuthConfigView.from_dict(response.json())

    def updateOAuthAuthCommand(self, OAuthConfig: ModelOAuthConfigView) -> ModelOAuthConfigView:
        """ Update the OAuth Authentication configuration
        """
        try:
            response = self.session.put(
                data=dumps(OAuthConfig.to_dict(OAuthConfig)),
                url=self._build_uri("/auth/oauth"),
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
            return ModelOAuthConfigView.from_dict(response.json())

    def deleteOidcAuthCommand(self) -> dict:
        """ Resets the OIDC Authentication configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/auth/oidc"),
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

    def getOidcAuthCommand(self) -> ModelOidcConfigView:
        """ Get the OIDC Authentication configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/auth/oidc"),
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
            return ModelOidcConfigView.from_dict(response.json())

    def updateOidcAuthCommand(self, OidcConfig: ModelOidcConfigView) -> ModelOidcConfigView:
        """ Update the OIDC Authentication configuration
        """
        try:
            response = self.session.put(
                data=dumps(OidcConfig.to_dict(OidcConfig)),
                url=self._build_uri("/auth/oidc"),
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
            return ModelOidcConfigView.from_dict(response.json())

    def getAuthOidcScopesCommand(self, clientId: str = None) -> ModelSupportedScopesView:
        """ Get the scopes supported by the current Admin OIDC Provider
        """
        try:
            response = self.session.get(
                url=self._build_uri("/auth/oidc/scopes"),
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
            return ModelSupportedScopesView.from_dict(response.json())

    def deleteAdminTokenProviderCommand(self) -> dict:
        """ Resets the Admin Token Provider configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/auth/tokenProvider"),
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

    def getAdminTokenProviderCommand(self) -> ModelAdminTokenProviderView:
        """ Get the Admin Token Provider configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/auth/tokenProvider"),
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
            return ModelAdminTokenProviderView.from_dict(response.json())

    def updateAdminTokenProviderCommand(self, AdminTokenProvider: ModelAdminTokenProviderView) -> ModelAdminTokenProviderView:
        """ Update the Admin Token Provider configuration
        """
        try:
            response = self.session.put(
                data=dumps(AdminTokenProvider.to_dict(AdminTokenProvider)),
                url=self._build_uri("/auth/tokenProvider"),
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
            return ModelAdminTokenProviderView.from_dict(response.json())

    def getAdminTokenProviderMetadataCommand(self) -> ModelOIDCProviderMetadata:
        """ Get the Admin Token Provider metadata
        """
        try:
            response = self.session.get(
                url=self._build_uri("/auth/tokenProvider/metadata"),
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

    def deleteAdminBasicWebSessionCommand(self) -> dict:
        """ Resets the Admin Web Session configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/auth/webSession"),
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

    def getAdminBasicWebSessionCommand(self) -> ModelAdminBasicWebSessionView:
        """ Get the admin web session configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/auth/webSession"),
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
            return ModelAdminBasicWebSessionView.from_dict(response.json())

    def updateAdminBasicWebSessionCommand(self, AdminWebSession: ModelAdminBasicWebSessionView) -> ModelAdminBasicWebSessionView:
        """ Update the admin web session configuration
        """
        try:
            response = self.session.put(
                data=dumps(AdminWebSession.to_dict(AdminWebSession)),
                url=self._build_uri("/auth/webSession"),
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
            return ModelAdminBasicWebSessionView.from_dict(response.json())
