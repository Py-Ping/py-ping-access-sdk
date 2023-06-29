import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.config_statuses_view import ConfigStatusesView as ModelConfigStatusesView
from pingaccesssdk.models.config_status_view import ConfigStatusView as ModelConfigStatusView
from pingaccesssdk.models.export_data import ExportData as ModelExportData


class Config:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Config")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def configExportCommand(self) -> ModelExportData:
        """ Export a JSON backup. This endpoint is not suitable for configurations that take longer than 30 seconds to export. For those configurations, use the "/config/export/workflows" endpoint instead.
        """
        try:
            response = self.session.get(
                url=self._build_uri("/config/export"),
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
            return ModelExportData.from_dict(response.json())

    def getConfigExportWorkflowsCommand(self) -> ModelConfigStatusesView:
        """ Get the status of pending Exports
        """
        try:
            response = self.session.get(
                url=self._build_uri("/config/export/workflows"),
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
            return ModelConfigStatusesView.from_dict(response.json())

    def addConfigExportWorkflowCommand(self) -> ModelConfigStatusView:
        """ Start a JSON backup of the entire system for export
        """
        try:
            response = self.session.post(
                url=self._build_uri("/config/export/workflows"),
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
            return ModelConfigStatusView.from_dict(response.json())

    def getConfigExportWorkflowCommand(self, id: str) -> ModelConfigStatusView:
        """ Check the status of an Export
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/config/export/workflows/{id}"),
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
            return ModelConfigStatusView.from_dict(response.json())

    def getConfigExportWorkflowDataCommand(self, id: str) -> ModelExportData:
        """ Export a JSON backup of the entire system
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/config/export/workflows/{id}/data"),
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
            return ModelExportData.from_dict(response.json())

    def configImportCommand(self, backupfile: str) -> dict:
        """ Import a JSON backup. This endpoint is not suitable for configurations that take longer than 30 seconds to import. For those configurations, use the "/config/import/workflows" endpoint instead.
        """
        try:
            response = self.session.post(
                data=dumps(backupfile.to_dict(backupfile)),
                url=self._build_uri("/config/import"),
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

    def getConfigImportWorkflowsCommand(self) -> ModelConfigStatusesView:
        """ Get the status of pending imports
        """
        try:
            response = self.session.get(
                url=self._build_uri("/config/import/workflows"),
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
            return ModelConfigStatusesView.from_dict(response.json())

    def addConfigImportWorkflowCommand(self, backupfile: ModelExportData, failFast: bool) -> dict:
        """ Start an Import of a JSON backup.
        """
        try:
            response = self.session.post(
                data=dumps(backupfile.to_dict(backupfile)),
                url=self._build_uri("/config/import/workflows"),
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

    def getConfigImportWorkflowCommand(self, id: str) -> ModelConfigStatusView:
        """ Check the status of an Import
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/config/import/workflows/{id}"),
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
            return ModelConfigStatusView.from_dict(response.json())
