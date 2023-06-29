import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.replica_admin_view import ReplicaAdminView as ModelReplicaAdminView
from pingaccesssdk.models.replica_admins_view import ReplicaAdminsView as ModelReplicaAdminsView
from pingaccesssdk.models.admin_configuration_view import AdminConfigurationView as ModelAdminConfigurationView


class AdminConfig:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AdminConfig")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def deleteAdminConfigurationCommand(self) -> dict:
        """ Resets the Admin Config to default values
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/adminConfig"),
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

    def getAdminConfigurationCommand(self) -> ModelAdminConfigurationView:
        """ Get the Admin Config
        """
        try:
            response = self.session.get(
                url=self._build_uri("/adminConfig"),
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
            return ModelAdminConfigurationView.from_dict(response.json())

    def updateAdminConfigurationCommand(self, AdminConfiguration: ModelAdminConfigurationView) -> ModelAdminConfigurationView:
        """ Update the Admin Config
        """
        try:
            response = self.session.put(
                data=dumps(AdminConfiguration.to_dict(AdminConfiguration)),
                url=self._build_uri("/adminConfig"),
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
            return ModelAdminConfigurationView.from_dict(response.json())

    def getReplicaAdminsCommand(self) -> ModelReplicaAdminsView:
        """ Get list of ReplicaAdmins
        """
        try:
            response = self.session.get(
                url=self._build_uri("/adminConfig/replicaAdmins"),
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
            return ModelReplicaAdminsView.from_dict(response.json())

    def addReplicaAdminCommand(self, replicaAdmin: ModelReplicaAdminView) -> ModelReplicaAdminView:
        """ Add a ReplicaAdmin
        """
        try:
            response = self.session.post(
                data=dumps(replicaAdmin.to_dict(replicaAdmin)),
                url=self._build_uri("/adminConfig/replicaAdmins"),
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
            return ModelReplicaAdminView.from_dict(response.json())

    def deleteReplicaAdminCommand(self, id: str) -> dict:
        """ Delete a ReplicaAdmin
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/adminConfig/replicaAdmins/{id}"),
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

    def getReplicaAdminCommand(self, id: str) -> ModelReplicaAdminView:
        """ Get a ReplicaAdmin
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/adminConfig/replicaAdmins/{id}"),
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
            return ModelReplicaAdminView.from_dict(response.json())

    def updateAdminReplicaCommand(self, id: str, replicaAdmin: ModelReplicaAdminView) -> ModelReplicaAdminView:
        """ Update a ReplicaAdmin
        """
        try:
            response = self.session.put(
                data=dumps(replicaAdmin.to_dict(replicaAdmin)),
                url=self._build_uri(f"/adminConfig/replicaAdmins/{id}"),
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
            return ModelReplicaAdminView.from_dict(response.json())

    def getAdminReplicaFileCommand(self, id: str) -> dict:
        """ Get configuration file for a given ReplicaAdmin
        """
        try:
            response = self.session.post(
                url=self._build_uri(f"/adminConfig/replicaAdmins/{id}/config"),
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
