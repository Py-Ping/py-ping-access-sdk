import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.rule_view import RuleView as ModelRuleView
from pingaccesssdk.models.rule_descriptors_view import RuleDescriptorsView as ModelRuleDescriptorsView
from pingaccesssdk.models.rule_descriptor_view import RuleDescriptorView as ModelRuleDescriptorView
from pingaccesssdk.models.rules_view import RulesView as ModelRulesView


class Rules:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Rules")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getRulesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelRulesView:
        """ Get all Rules
        """
        try:
            response = self.session.get(
                url=self._build_uri("/rules"),
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
            return ModelRulesView.from_dict(response.json())

    def addRuleCommand(self, Rule: ModelRuleView) -> ModelRuleView:
        """ Add a Rule
        """
        try:
            response = self.session.post(
                data=dumps(Rule.to_dict(Rule)),
                url=self._build_uri("/rules"),
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
            return ModelRuleView.from_dict(response.json())

    def getRuleDescriptorsCommand(self) -> ModelRuleDescriptorsView:
        """ Get descriptors for all supported Rule types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/rules/descriptors"),
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
            return ModelRuleDescriptorsView.from_dict(response.json())

    def getRuleDescriptorCommand(self, ruleType: str) -> ModelRuleDescriptorView:
        """ Get descriptor for a Rule type
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/rules/descriptors/{ruleType}"),
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
            return ModelRuleDescriptorView.from_dict(response.json())

    def deleteRuleCommand(self, id: str) -> dict:
        """ Delete a Rule
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/rules/{id}"),
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

    def getRuleCommand(self, id: str) -> ModelRuleView:
        """ Get a Rule
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/rules/{id}"),
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
            return ModelRuleView.from_dict(response.json())

    def updateRuleCommand(self, id: str, Rule: ModelRuleView) -> ModelRuleView:
        """ Update a Rule
        """
        try:
            response = self.session.put(
                data=dumps(Rule.to_dict(Rule)),
                url=self._build_uri(f"/rules/{id}"),
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
            return ModelRuleView.from_dict(response.json())
