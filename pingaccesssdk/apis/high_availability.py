import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView
from pingaccesssdk.models.load_balancing_strategy_view import LoadBalancingStrategyView as ModelLoadBalancingStrategyView
from pingaccesssdk.models.availability_profile_view import AvailabilityProfileView as ModelAvailabilityProfileView
from pingaccesssdk.models.descriptor_view import DescriptorView as ModelDescriptorView
from pingaccesssdk.models.load_balancing_strategies_view import LoadBalancingStrategiesView as ModelLoadBalancingStrategiesView
from pingaccesssdk.models.availability_profiles_view import AvailabilityProfilesView as ModelAvailabilityProfilesView


class HighAvailability:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.HighAvailability")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAvailabilityProfilesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelAvailabilityProfilesView:
        """ Get all Availability Profiles
        """
        try:
            response = self.session.get(
                url=self._build_uri("/highAvailability/availabilityProfiles"),
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
            return ModelAvailabilityProfilesView.from_dict(response.json())

    def addAvailabilityProfileCommand(self, AvailabilityProfile: ModelAvailabilityProfileView) -> ModelAvailabilityProfileView:
        """ Create an Availability Profile
        """
        try:
            response = self.session.post(
                data=dumps(AvailabilityProfile.to_dict(AvailabilityProfile)),
                url=self._build_uri("/highAvailability/availabilityProfiles"),
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
            return ModelAvailabilityProfileView.from_dict(response.json())

    def getAvailabilityProfileDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all Availability Profiles
        """
        try:
            response = self.session.get(
                url=self._build_uri("/highAvailability/availabilityProfiles/descriptors"),
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

    def getAvailabilityProfileDescriptorCommand(self, availabilityProfileType: str) -> ModelDescriptorView:
        """ Get a descriptor for an Availability Profile
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/highAvailability/availabilityProfiles/descriptors/{availabilityProfileType}"),
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

    def deleteAvailabilityProfileCommand(self, id: str) -> dict:
        """ Delete an Availability Profile
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/highAvailability/availabilityProfiles/{id}"),
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

    def getAvailabilityProfileCommand(self, id: str) -> ModelAvailabilityProfileView:
        """ Get an Availability Profile
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/highAvailability/availabilityProfiles/{id}"),
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
            return ModelAvailabilityProfileView.from_dict(response.json())

    def updateAvailabilityProfileCommand(self, id: str, AvailabilityProfile: ModelAvailabilityProfileView) -> ModelAvailabilityProfileView:
        """ Update an Availability Profile
        """
        try:
            response = self.session.put(
                data=dumps(AvailabilityProfile.to_dict(AvailabilityProfile)),
                url=self._build_uri(f"/highAvailability/availabilityProfiles/{id}"),
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
            return ModelAvailabilityProfileView.from_dict(response.json())

    def getLoadBalancingStrategiesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelLoadBalancingStrategiesView:
        """ Get all Load Balancing Strategies
        """
        try:
            response = self.session.get(
                url=self._build_uri("/highAvailability/loadBalancingStrategies"),
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
            return ModelLoadBalancingStrategiesView.from_dict(response.json())

    def addLoadBalancingStrategyCommand(self, LoadBalancingStrategy: ModelLoadBalancingStrategyView) -> ModelLoadBalancingStrategyView:
        """ Create a Load Balancing Strategy
        """
        try:
            response = self.session.post(
                data=dumps(LoadBalancingStrategy.to_dict(LoadBalancingStrategy)),
                url=self._build_uri("/highAvailability/loadBalancingStrategies"),
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
            return ModelLoadBalancingStrategyView.from_dict(response.json())

    def getLoadBalancingStrategyDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all Load Balancing Strategies
        """
        try:
            response = self.session.get(
                url=self._build_uri("/highAvailability/loadBalancingStrategies/descriptors"),
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

    def getLoadBalancingStrategyDescriptorCommand(self, loadBalancingStrategyType: str) -> ModelDescriptorView:
        """ Get a descriptor for a Load Balancing Strategy
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/highAvailability/loadBalancingStrategies/descriptors/{loadBalancingStrategyType}"),
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

    def deleteLoadBalancingStrategyCommand(self, id: str) -> dict:
        """ Delete a Load Balancing Strategy
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/highAvailability/loadBalancingStrategies/{id}"),
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

    def getLoadBalancingStrategyCommand(self, id: str) -> ModelLoadBalancingStrategyView:
        """ Get a Load Balancing Strategy
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/highAvailability/loadBalancingStrategies/{id}"),
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
            return ModelLoadBalancingStrategyView.from_dict(response.json())

    def updateLoadBalancingStrategyCommand(self, id: str, LoadBalancingStrategy: ModelLoadBalancingStrategyView) -> ModelLoadBalancingStrategyView:
        """ Update a Load Balancing Strategy
        """
        try:
            response = self.session.put(
                data=dumps(LoadBalancingStrategy.to_dict(LoadBalancingStrategy)),
                url=self._build_uri(f"/highAvailability/loadBalancingStrategies/{id}"),
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
            return ModelLoadBalancingStrategyView.from_dict(response.json())
