import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.http_monitoring_view import HttpMonitoringView as ModelHttpMonitoringView
from pingaccesssdk.models.ip_multi_value_source_view import IpMultiValueSourceView as ModelIpMultiValueSourceView
from pingaccesssdk.models.host_multi_value_source_view import HostMultiValueSourceView as ModelHostMultiValueSourceView
from pingaccesssdk.models.protocol_source_view import ProtocolSourceView as ModelProtocolSourceView


class HttpConfig:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.HttpConfig")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteHttpMonitoringCommand(self) -> dict:
        """ Resets the HTTP monitoring auditLevel to default value
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/httpConfig/monitoring"),
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

    def getHttpMonitoringCommand(self) -> ModelHttpMonitoringView:
        """ Get the HTTP monitoring auditLevel
        """
        try:
            response = self.session.get(
                url=self._build_uri("/httpConfig/monitoring"),
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
            return ModelHttpMonitoringView.from_dict(response.json())

    def updateHttpMonitoringCommand(self, Monitoring: ModelHttpMonitoringView) -> ModelHttpMonitoringView:
        """ Update the HTTP monitoring auditLevel
        """
        try:
            response = self.session.put(
                data=dumps(Monitoring.to_dict(Monitoring)),
                url=self._build_uri("/httpConfig/monitoring"),
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
            return ModelHttpMonitoringView.from_dict(response.json())

    def deleteHostSourceCommand(self) -> dict:
        """ Resets the HTTP request Host Source type to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/httpConfig/request/hostSource"),
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

    def getHostSourceCommand(self) -> ModelHostMultiValueSourceView:
        """ Get the HTTP request Host Source type
        """
        try:
            response = self.session.get(
                url=self._build_uri("/httpConfig/request/hostSource"),
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
            return ModelHostMultiValueSourceView.from_dict(response.json())

    def updateHostSourceCommand(self, HttpConfiguration: ModelHostMultiValueSourceView) -> ModelHostMultiValueSourceView:
        """ Update the HTTP request Host Source type
        """
        try:
            response = self.session.put(
                data=dumps(HttpConfiguration.to_dict(HttpConfiguration)),
                url=self._build_uri("/httpConfig/request/hostSource"),
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
            return ModelHostMultiValueSourceView.from_dict(response.json())

    def deleteIpSourceCommand(self) -> dict:
        """ Resets the HTTP request IP Source type to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/httpConfig/request/ipSource"),
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

    def getIpSourceCommand(self) -> ModelIpMultiValueSourceView:
        """ Get the HTTP request IP Source type
        """
        try:
            response = self.session.get(
                url=self._build_uri("/httpConfig/request/ipSource"),
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
            return ModelIpMultiValueSourceView.from_dict(response.json())

    def updateIpSourceCommand(self, HttpConfiguration: ModelIpMultiValueSourceView) -> ModelIpMultiValueSourceView:
        """ Update the HTTP request IP Source type
        """
        try:
            response = self.session.put(
                data=dumps(HttpConfiguration.to_dict(HttpConfiguration)),
                url=self._build_uri("/httpConfig/request/ipSource"),
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
            return ModelIpMultiValueSourceView.from_dict(response.json())

    def deleteProtoSourceCommand(self) -> dict:
        """ Resets the HTTP request Protocol Source type to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/httpConfig/request/protocolSource"),
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

    def getProtoSourceCommand(self) -> ModelProtocolSourceView:
        """ Get the HTTP request Protocol Source type
        """
        try:
            response = self.session.get(
                url=self._build_uri("/httpConfig/request/protocolSource"),
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
            return ModelProtocolSourceView.from_dict(response.json())

    def updateProtocolSourceCommand(self, HttpConfiguration: ModelProtocolSourceView) -> ModelProtocolSourceView:
        """ Update the HTTP request Protocol Source type
        """
        try:
            response = self.session.put(
                data=dumps(HttpConfiguration.to_dict(HttpConfiguration)),
                url=self._build_uri("/httpConfig/request/protocolSource"),
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
            return ModelProtocolSourceView.from_dict(response.json())
