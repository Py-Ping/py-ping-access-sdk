import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.engine_certificates_view import EngineCertificatesView as ModelEngineCertificatesView
from pingaccesssdk.models.engine_registration_token_view import EngineRegistrationTokenView as ModelEngineRegistrationTokenView
from pingaccesssdk.models.engine_health_status_view import EngineHealthStatusView as ModelEngineHealthStatusView
from pingaccesssdk.models.engine_view import EngineView as ModelEngineView
from pingaccesssdk.models.engines_view import EnginesView as ModelEnginesView
from pingaccesssdk.models.engine_certificate_view import EngineCertificateView as ModelEngineCertificateView


class Engines:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Engines")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getEnginesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelEnginesView:
        """ Get all Engines
        """
        try:
            response = self.session.get(
                url=self._build_uri("/engines"),
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
            return ModelEnginesView.from_dict(response.json())

    def addEngineCommand(self, Engine: ModelEngineView) -> ModelEngineView:
        """ Add an Engine
        """
        try:
            response = self.session.post(
                data=dumps(Engine.to_dict(Engine)),
                url=self._build_uri("/engines"),
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
            return ModelEngineView.from_dict(response.json())

    def getEngineCertificatesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, alias: str = None, sortKey: str = None, order: str = None) -> ModelEngineCertificatesView:
        """ Get all Engine Certificates
        """
        try:
            response = self.session.get(
                url=self._build_uri("/engines/certificates"),
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
            return ModelEngineCertificatesView.from_dict(response.json())

    def getEngineCertificateCommand(self, id: str) -> ModelEngineCertificateView:
        """ Get an Engine Certificate
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/engines/certificates/{id}"),
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
            return ModelEngineCertificateView.from_dict(response.json())

    def getEngineRegistrationJwtCommand(self, EngineRegistrationToken: ModelEngineRegistrationTokenView) -> dict:
        """ Get a JWT to use for engine self-registration
        """
        try:
            response = self.session.post(
                data=dumps(EngineRegistrationToken.to_dict(EngineRegistrationToken)),
                url=self._build_uri("/engines/registration/token"),
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

    def getEngineStatusCommand(self) -> ModelEngineHealthStatusView:
        """ Get health status of all Engines
        """
        try:
            response = self.session.get(
                url=self._build_uri("/engines/status"),
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
            return ModelEngineHealthStatusView.from_dict(response.json())

    def deleteEngineCommand(self, id: str) -> dict:
        """ Delete an Engine
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/engines/{id}"),
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
            return response

    def getEngineCommand(self, id: str) -> ModelEngineView:
        """ Get an Engine
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/engines/{id}"),
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
            return ModelEngineView.from_dict(response.json())

    def updateEngineCommand(self, id: str, Engine: ModelEngineView) -> ModelEngineView:
        """ Update an Engine
        """
        try:
            response = self.session.put(
                data=dumps(Engine.to_dict(Engine)),
                url=self._build_uri(f"/engines/{id}"),
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
            return ModelEngineView.from_dict(response.json())

    def getEngineConfigFileCommand(self, id: str) -> dict:
        """ Get configuration file for an Engine
        """
        try:
            response = self.session.post(
                url=self._build_uri(f"/engines/{id}/config"),
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
