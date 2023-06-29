import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.authentication_challenge_policy_view import AuthenticationChallengePolicyView as ModelAuthenticationChallengePolicyView
from pingaccesssdk.models.descriptor_view import DescriptorView as ModelDescriptorView
from pingaccesssdk.models.authentication_challenge_policies_view import AuthenticationChallengePoliciesView as ModelAuthenticationChallengePoliciesView
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView


class AuthenticationChallengePolicies:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AuthenticationChallengePolicies")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAuthenticationChallengePoliciesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelAuthenticationChallengePoliciesView:
        """ Get all Authentication Challenge Policies
        """
        try:
            response = self.session.get(
                url=self._build_uri("/authenticationChallengePolicies"),
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
            return ModelAuthenticationChallengePoliciesView.from_dict(response.json())

    def addAuthenticationChallengePolicyCommand(self, AuthenticationChallengePolicy: ModelAuthenticationChallengePolicyView) -> ModelAuthenticationChallengePolicyView:
        """ Create an Authentication Challenge Policy
        """
        try:
            response = self.session.post(
                data=dumps(AuthenticationChallengePolicy.to_dict(AuthenticationChallengePolicy)),
                url=self._build_uri("/authenticationChallengePolicies"),
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
            return ModelAuthenticationChallengePolicyView.from_dict(response.json())

    def getRequestMatcherDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get the descriptors for all the Authentication Challenge Policy Request Matchers
        """
        try:
            response = self.session.get(
                url=self._build_uri("/authenticationChallengePolicies/requestMatchers/descriptors"),
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

    def getRequestMatcherDescriptorCommand(self, requestMatcherType: str) -> ModelDescriptorView:
        """ Get the descriptor for an Authentication Challenge Policy Request Matcher type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationChallengePolicies/requestMatchers/descriptors/{requestMatcherType}"),
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

    def getChallengeResponseFilterDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get the descriptors for all the Authentication Challenge Policy Response Filtersr
        """
        try:
            response = self.session.get(
                url=self._build_uri("/authenticationChallengePolicies/responseFilters/descriptors"),
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

    def getChallengeResponseFilterDescriptorCommand(self, responseFilterType: str) -> ModelDescriptorView:
        """ Get the descriptor for an Authentication Challenge Policy Response Filter type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationChallengePolicies/responseFilters/descriptors/{responseFilterType}"),
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

    def getChallengeResponseGeneratorDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get the descriptors for all the Authentication Challenge Policy Response Generators
        """
        try:
            response = self.session.get(
                url=self._build_uri("/authenticationChallengePolicies/responseGenerators/descriptors"),
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

    def getChallengeResponseGeneratorDescriptorCommand(self, responseGeneratorType: str) -> ModelDescriptorView:
        """ Get the descriptor for an Authentication Challenge Policy Response Generator type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationChallengePolicies/responseGenerators/descriptors/{responseGeneratorType}"),
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

    def deleteAuthenticationChallengePolicyCommand(self, id: str) -> dict:
        """ Delete an Authentication Challenge Policy
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/authenticationChallengePolicies/{id}"),
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

    def getAuthenticationChallengePolicyCommand(self, id: str) -> ModelAuthenticationChallengePolicyView:
        """ Get an Authentication Challenge Policy
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationChallengePolicies/{id}"),
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
            return ModelAuthenticationChallengePolicyView.from_dict(response.json())

    def updateAuthenticationChallengePolicyCommand(self, id: str, AuthenticationChallengePolicy: ModelAuthenticationChallengePolicyView) -> ModelAuthenticationChallengePolicyView:
        """ Update an Authentication Challenge Policy
        """
        try:
            response = self.session.put(
                data=dumps(AuthenticationChallengePolicy.to_dict(AuthenticationChallengePolicy)),
                url=self._build_uri(f"/authenticationChallengePolicies/{id}"),
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
            return ModelAuthenticationChallengePolicyView.from_dict(response.json())
