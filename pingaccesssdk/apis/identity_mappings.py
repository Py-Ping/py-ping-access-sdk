import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView
from pingaccesssdk.models.descriptor_view import DescriptorView as ModelDescriptorView
from pingaccesssdk.models.identity_mappings_view import IdentityMappingsView as ModelIdentityMappingsView
from pingaccesssdk.models.identity_mapping_view import IdentityMappingView as ModelIdentityMappingView


class IdentityMappings:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.IdentityMappings")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getIdentityMappingsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelIdentityMappingsView:
        """ Get all Identity Mappings
        """
        try:
            response = self.session.get(
                url=self._build_uri("/identityMappings"),
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
            return ModelIdentityMappingsView.from_dict(response.json())

    def addIdentityMappingCommand(self, IdentityMappings: ModelIdentityMappingView) -> ModelIdentityMappingView:
        """ Create an Identity Mapping
        """
        try:
            response = self.session.post(
                data=dumps(IdentityMappings.to_dict(IdentityMappings)),
                url=self._build_uri("/identityMappings"),
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
            return ModelIdentityMappingView.from_dict(response.json())

    def getIdentityMappingDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all supported Identity Mapping types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/identityMappings/descriptors"),
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

    def getIdentityMappingDescriptorCommand(self, identityMappingType: str) -> ModelDescriptorView:
        """ Get descriptor for an Identity Mapping type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/identityMappings/descriptors/{identityMappingType}"),
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

    def deleteIdentityMappingCommand(self, id: str) -> dict:
        """ Delete an Identity Mapping
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/identityMappings/{id}"),
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

    def getIdentityMappingCommand(self, id: str) -> ModelIdentityMappingView:
        """ Get an Identity Mapping
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/identityMappings/{id}"),
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
            return ModelIdentityMappingView.from_dict(response.json())

    def updateIdentityMappingCommand(self, id: str, IdentityMappings: ModelIdentityMappingView) -> ModelIdentityMappingView:
        """ Update an Identity Mapping
        """
        try:
            response = self.session.put(
                data=dumps(IdentityMappings.to_dict(IdentityMappings)),
                url=self._build_uri(f"/identityMappings/{id}"),
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
            return ModelIdentityMappingView.from_dict(response.json())
