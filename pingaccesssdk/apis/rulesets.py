import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.rule_set_view import RuleSetView as ModelRuleSetView
from pingaccesssdk.models.rule_set_element_types_view import RuleSetElementTypesView as ModelRuleSetElementTypesView
from pingaccesssdk.models.rule_set_success_criteria_view import RuleSetSuccessCriteriaView as ModelRuleSetSuccessCriteriaView
from pingaccesssdk.models.rule_sets_view import RuleSetsView as ModelRuleSetsView


class Rulesets:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Rulesets")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getRuleSetsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelRuleSetsView:
        """ Get all Rule Sets
        """
        try:
            response = self.session.get(
                url=self._build_uri("/rulesets"),
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
            return ModelRuleSetsView.from_dict(response.json())

    def addRuleSetCommand(self, RuleSet: ModelRuleSetView) -> ModelRuleSetView:
        """ Add a Rule Set
        """
        try:
            response = self.session.post(
                data=dumps(RuleSet.to_dict(RuleSet)),
                url=self._build_uri("/rulesets"),
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
            return ModelRuleSetView.from_dict(response.json())

    def getRuleSetElementTypesCommand(self) -> ModelRuleSetElementTypesView:
        """ Get all Rule Set Element Types
        """
        try:
            response = self.session.get(
                url=self._build_uri("/rulesets/elementTypes"),
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
            return ModelRuleSetElementTypesView.from_dict(response.json())

    def getRuleSetSuccessCriteriaCommand(self) -> ModelRuleSetSuccessCriteriaView:
        """ Get all Success Criteria
        """
        try:
            response = self.session.get(
                url=self._build_uri("/rulesets/successCriteria"),
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
            return ModelRuleSetSuccessCriteriaView.from_dict(response.json())

    def deleteRuleSetCommand(self, id: str) -> dict:
        """ Delete a Rule Set
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/rulesets/{id}"),
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

    def getRuleSetCommand(self, id: str) -> ModelRuleSetView:
        """ Get a Rule Set
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/rulesets/{id}"),
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
            return ModelRuleSetView.from_dict(response.json())

    def updateRuleSetCommand(self, id: str, RuleSet: ModelRuleSetView) -> ModelRuleSetView:
        """ Update a Rule Set
        """
        try:
            response = self.session.put(
                data=dumps(RuleSet.to_dict(RuleSet)),
                url=self._build_uri(f"/rulesets/{id}"),
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
            return ModelRuleSetView.from_dict(response.json())
