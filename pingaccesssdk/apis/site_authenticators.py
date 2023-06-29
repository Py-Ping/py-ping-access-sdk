import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView
from pingaccesssdk.models.site_authenticator_view import SiteAuthenticatorView as ModelSiteAuthenticatorView
from pingaccesssdk.models.descriptor_view import DescriptorView as ModelDescriptorView
from pingaccesssdk.models.site_authenticators_view import SiteAuthenticatorsView as ModelSiteAuthenticatorsView


class SiteAuthenticators:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.SiteAuthenticators")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSiteAuthenticatorsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelSiteAuthenticatorsView:
        """ Get all Site Authenticators
        """
        try:
            response = self.session.get(
                url=self._build_uri("/siteAuthenticators"),
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
            return ModelSiteAuthenticatorsView.from_dict(response.json())

    def addSiteAuthenticatorCommand(self, SiteAuthenticator: ModelSiteAuthenticatorView) -> ModelSiteAuthenticatorView:
        """ Create a Site Authenticator
        """
        try:
            response = self.session.post(
                data=dumps(SiteAuthenticator.to_dict(SiteAuthenticator)),
                url=self._build_uri("/siteAuthenticators"),
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
            return ModelSiteAuthenticatorView.from_dict(response.json())

    def getSiteAuthenticatorDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all supported Site Authenticator types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/siteAuthenticators/descriptors"),
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

    def getSiteAuthenticatorDescriptorCommand(self, siteAuthenticatorType: str) -> ModelDescriptorView:
        """ Get descriptor for a Site Authenticator type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/siteAuthenticators/descriptors/{siteAuthenticatorType}"),
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

    def deleteSiteAuthenticatorCommand(self, id: str) -> dict:
        """ Delete a Site Authenticator
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/siteAuthenticators/{id}"),
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

    def getSiteAuthenticatorCommand(self, id: str) -> ModelSiteAuthenticatorView:
        """ Get a Site Authenticator
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/siteAuthenticators/{id}"),
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
            return ModelSiteAuthenticatorView.from_dict(response.json())

    def updateSiteAuthenticatorCommand(self, id: str, SiteAuthenticator: ModelSiteAuthenticatorView) -> ModelSiteAuthenticatorView:
        """ Update a Site Authenticator
        """
        try:
            response = self.session.put(
                data=dumps(SiteAuthenticator.to_dict(SiteAuthenticator)),
                url=self._build_uri(f"/siteAuthenticators/{id}"),
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
            return ModelSiteAuthenticatorView.from_dict(response.json())
