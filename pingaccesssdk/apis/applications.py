import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.methods_view import MethodsView as ModelMethodsView
from pingaccesssdk.models.reserved_application_view import ReservedApplicationView as ModelReservedApplicationView
from pingaccesssdk.models.resource_view import ResourceView as ModelResourceView
from pingaccesssdk.models.resource_order_view import ResourceOrderView as ModelResourceOrderView
from pingaccesssdk.models.applications_view import ApplicationsView as ModelApplicationsView
from pingaccesssdk.models.resources_view import ResourcesView as ModelResourcesView
from pingaccesssdk.models.application_view import ApplicationView as ModelApplicationView
from pingaccesssdk.models.descriptor_view import DescriptorView as ModelDescriptorView
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView
from pingaccesssdk.models.resource_matching_evaluation_order_view import ResourceMatchingEvaluationOrderView as ModelResourceMatchingEvaluationOrderView


class Applications:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Applications")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getApplicationsCommand(self, page: int = None, siteId: int = None, numberPerPage: int = None, agentId: int = None, sidebandClientId: int = None, virtualHostId: int = None, ruleId: int = None, rulesetId: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelApplicationsView:
        """ Get all Applications
        """
        try:
            response = self.session.get(
                url=self._build_uri("/applications"),
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
            return ModelApplicationsView.from_dict(response.json())

    def addApplicationCommand(self, Application: ModelApplicationView) -> ModelApplicationView:
        """ Add an Application
        """
        try:
            response = self.session.post(
                data=dumps(Application.to_dict(True)),
                url=self._build_uri("/applications"),
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
            return ModelApplicationView.from_dict(response.json())

    def deleteReservedApplicationCommand(self) -> dict:
        """ Resets the Reserved Application configuration to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/applications/reserved"),
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

    def getReservedApplicationCommand(self) -> ModelReservedApplicationView:
        """ Get Reserved Application configuration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/applications/reserved"),
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
            return ModelReservedApplicationView.from_dict(response.json())

    def updateReservedApplicationCommand(self, _applications_reserved: ModelReservedApplicationView) -> ModelReservedApplicationView:
        """ Update Reserved Application configuration
        """
        try:
            response = self.session.put(
                data=dumps(_applications_reserved.to_dict(_applications_reserved)),
                url=self._build_uri("/applications/reserved"),
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
            return ModelReservedApplicationView.from_dict(response.json())

    def getResourcesCommand(self, page: int = None, numberPerPage: int = None, ruleId: int = None, rulesetId: int = None, name: str = None, filter: str = None, sortKey: str = None, order: str = None) -> ModelResourcesView:
        """ Get all Resources
        """
        try:
            response = self.session.get(
                url=self._build_uri("/applications/resources"),
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
            return ModelResourcesView.from_dict(response.json())

    def getApplicationsResourcesMethodsCommand(self) -> ModelMethodsView:
        """ Get Application Resource Methods
        """
        try:
            response = self.session.get(
                url=self._build_uri("/applications/resources/methods"),
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
            return ModelMethodsView.from_dict(response.json())

    def getApplicationResourceResponseGeneratorDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all Application Resource Response Generators
        """
        try:
            response = self.session.get(
                url=self._build_uri("/applications/resources/responseGenerators/descriptors"),
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

    def getApplicationResourceResponseGeneratorDescriptorCommand(self, responseGeneratorType: str) -> ModelDescriptorView:
        """ Get descriptor for a Response Generator type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/applications/resources/responseGenerators/descriptors/{responseGeneratorType}"),
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

    def deleteApplicationResourceCommand(self, applicationId: str, resourceId: str) -> dict:
        """ Delete an Application Resource
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/applications/{applicationId}/resources/{resourceId}"),
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

    def getApplicationResourceCommand(self, applicationId: str, resourceId: str) -> ModelResourceView:
        """ Get an Application Resource
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/applications/{applicationId}/resources/{resourceId}"),
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
            return ModelResourceView.from_dict(response.json())

    def updateApplicationResourceCommand(self, applicationId: str, resourceId: str, Resource: ModelResourceView) -> ModelResourceView:
        """ Update an Application Resource
        """
        try:
            response = self.session.put(
                data=dumps(Resource.to_dict(Resource)),
                url=self._build_uri(f"/applications/{applicationId}/resources/{resourceId}"),
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
            return ModelResourceView.from_dict(response.json())

    def deleteApplicationCommand(self, id: str) -> dict:
        """ Delete an Application
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/applications/{id}"),
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

    def getApplicationCommand(self, id: str) -> ModelApplicationView:
        """ Get an Application
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/applications/{id}"),
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
            return ModelApplicationView.from_dict(response.json())

    def updateApplicationCommand(self, id: str, Application: ModelApplicationView) -> ModelApplicationView:
        """ Update an Application
        """
        try:
            response = self.session.put(
                data=dumps(Application.to_dict(Application)),
                url=self._build_uri(f"/applications/{id}"),
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
            return ModelApplicationView.from_dict(response.json())

    def getResourceMatchingEvaluationOrderCommand(self, id: str) -> ModelResourceMatchingEvaluationOrderView:
        """ Get the resource path ordering for an Application
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/applications/{id}/resourceMatchingEvaluationOrder"),
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
            return ModelResourceMatchingEvaluationOrderView.from_dict(response.json())

    def getApplicationResourcesCommand(self, id: str, page: int = None, numberPerPage: int = None, name: str = None, filter: str = None, sortKey: str = None, order: str = None) -> ModelResourcesView:
        """ Get Resources for an Application
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/applications/{id}/resources"),
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
            return ModelResourcesView.from_dict(response.json())

    def addApplicationResourceCommand(self, id: str, Resource: ModelResourceView) -> ModelResourceView:
        """ Add Resource to an Application
        """
        try:
            response = self.session.post(
                data=dumps(Resource.to_dict(Resource)),
                url=self._build_uri(f"/applications/{id}/resources"),
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
            return ModelResourceView.from_dict(response.json())

    def getResourceAutoOrderCommand(self, id: str) -> ModelResourceOrderView:
        """ Computes an automatic, intelligent resource ordering for an Application.
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/applications/{id}/resources/autoOrder"),
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
            return ModelResourceOrderView.from_dict(response.json())
