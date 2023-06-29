import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.key_set_view import KeySetView as ModelKeySetView
from pingaccesssdk.models.web_session_management_view import WebSessionManagementView as ModelWebSessionManagementView
from pingaccesssdk.models.request_preservation_types_view import RequestPreservationTypesView as ModelRequestPreservationTypesView
from pingaccesssdk.models.cookie_types_view import CookieTypesView as ModelCookieTypesView
from pingaccesssdk.models.signing_algorithms_view import SigningAlgorithmsView as ModelSigningAlgorithmsView
from pingaccesssdk.models.algorithms_view import AlgorithmsView as ModelAlgorithmsView
from pingaccesssdk.models.web_storage_types_view import WebStorageTypesView as ModelWebStorageTypesView
from pingaccesssdk.models.supported_scopes_view import SupportedScopesView as ModelSupportedScopesView
from pingaccesssdk.models.oidc_login_types_view import OidcLoginTypesView as ModelOidcLoginTypesView


class WebSessionManagement:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.WebSessionManagement")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteWebSessionManagementCommand(self) -> dict:
        """ Resets the Web Session Management configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/webSessionManagement"),
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

    def getWebSessionManagementCommand(self) -> ModelWebSessionManagementView:
        """ Get the Web Session Management configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement"),
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
            return ModelWebSessionManagementView.from_dict(response.json())

    def updateWebSessionManagementCommand(self, WebSessionManagement: ModelWebSessionManagementView) -> ModelWebSessionManagementView:
        """ Update the Web Session Management configuration
        """
        try:
            response = self.session.put(
                data=dumps(WebSessionManagement.to_dict(WebSessionManagement)),
                url=self._build_uri("/webSessionManagement"),
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
            return ModelWebSessionManagementView.from_dict(response.json())

    def getCookieTypes(self) -> ModelCookieTypesView:
        """ Get the valid OIDC Cookie Types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/cookieTypes"),
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
            return ModelCookieTypesView.from_dict(response.json())

    def getWebSessionSupportedEncryptionAlgorithmsCommand(self) -> ModelAlgorithmsView:
        """ Get the valid algorithms for Web Session Cookie Encryption
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/encryptionAlgorithms"),
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
            return ModelAlgorithmsView.from_dict(response.json())

    def getWebSessionKeySetCommand(self) -> ModelKeySetView:
        """ Get the Web Session key set configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/keySet"),
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
            return ModelKeySetView.from_dict(response.json())

    def updateWebSessionKeySetCommand(self, KeySet: ModelKeySetView) -> ModelKeySetView:
        """ Update the WebSession key set configuration
        """
        try:
            response = self.session.put(
                data=dumps(KeySet.to_dict(KeySet)),
                url=self._build_uri("/webSessionManagement/keySet"),
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
            return ModelKeySetView.from_dict(response.json())

    def getOidcLoginTypes(self) -> ModelOidcLoginTypesView:
        """ Get the valid OIDC Login Types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/oidcLoginTypes"),
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
            return ModelOidcLoginTypesView.from_dict(response.json())

    def getOidcScopesCommand(self, clientId: str = None) -> ModelSupportedScopesView:
        """ Get the scopes supported by the current OIDC Provider
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/oidcScopes"),
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

    def getRequestPreservationTypes(self) -> ModelRequestPreservationTypesView:
        """ Get the valid Request Preservation Types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/requestPreservationTypes"),
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
            return ModelRequestPreservationTypesView.from_dict(response.json())

    def getWebSessionSupportedSigningAlgorithms(self) -> ModelSigningAlgorithmsView:
        """ Get the valid algorithms for Web Session Cookie Signing
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/signingAlgorithms"),
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
            return ModelSigningAlgorithmsView.from_dict(response.json())

    def getWebStorageTypes(self) -> ModelWebStorageTypesView:
        """ Get the valid Web Storage Types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/webSessionManagement/webStorageTypes"),
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
            return ModelWebStorageTypesView.from_dict(response.json())
