import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.agent_view import AgentView as ModelAgentView
from pingaccesssdk.models.agent_certificates_view import AgentCertificatesView as ModelAgentCertificatesView
from pingaccesssdk.models.agents_view import AgentsView as ModelAgentsView
from pingaccesssdk.models.agent_certificate_view import AgentCertificateView as ModelAgentCertificateView


class Agents:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Agents")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAgentsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelAgentsView:
        """ Get all Agents
        """
        try:
            response = self.session.get(
                url=self._build_uri("/agents"),
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
            return ModelAgentsView.from_dict(response.json())

    def addAgentCommand(self, Agent: ModelAgentView) -> ModelAgentView:
        """ Add an Agent
        """
        try:
            response = self.session.post(
                data=dumps(Agent.to_dict(Agent)),
                url=self._build_uri("/agents"),
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
            return ModelAgentView.from_dict(response.json())

    def getAgentCertificatesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, alias: str = None, sortKey: str = None, order: str = None) -> ModelAgentCertificatesView:
        """ Get all Agent Certificates
        """
        try:
            response = self.session.get(
                url=self._build_uri("/agents/certificates"),
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
            return ModelAgentCertificatesView.from_dict(response.json())

    def getAgentCertificateCommand(self, id: str) -> ModelAgentCertificateView:
        """ Get an Agent Certificate
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/agents/certificates/{id}"),
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
            return ModelAgentCertificateView.from_dict(response.json())

    def getAgentFileCommand(self, agentId: str, sharedSecretId: str) -> dict:
        """ Get a configuration file for an Agent
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/agents/{agentId}/config/{sharedSecretId}"),
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

    def deleteAgentCommand(self, id: str) -> dict:
        """ Delete an Agent
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/agents/{id}"),
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

    def getAgentCommand(self, id: str) -> ModelAgentView:
        """ Get an Agent
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/agents/{id}"),
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
            return ModelAgentView.from_dict(response.json())

    def updateAgentCommand(self, id: str, Agent: ModelAgentView) -> ModelAgentView:
        """ Update an Agent
        """
        try:
            response = self.session.put(
                data=dumps(Agent.to_dict(Agent)),
                url=self._build_uri(f"/agents/{id}"),
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
            return ModelAgentView.from_dict(response.json())
