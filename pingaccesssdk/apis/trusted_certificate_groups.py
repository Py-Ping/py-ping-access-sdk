import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.trusted_certificate_group_view import TrustedCertificateGroupView as ModelTrustedCertificateGroupView
from pingaccesssdk.models.trusted_certificate_groups_view import TrustedCertificateGroupsView as ModelTrustedCertificateGroupsView


class TrustedCertificateGroups:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.TrustedCertificateGroups")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getTrustedCertificateGroupsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelTrustedCertificateGroupsView:
        """ Get all Trusted Certificate Groups
        """
        try:
            response = self.session.get(
                url=self._build_uri("/trustedCertificateGroups"),
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
            return ModelTrustedCertificateGroupsView.from_dict(response.json())

    def addTrustedCertificateGroupCommand(self, TrustedCertificateGroup: ModelTrustedCertificateGroupView) -> ModelTrustedCertificateGroupView:
        """ Create a Trusted Certificate Group
        """
        try:
            response = self.session.post(
                data=dumps(TrustedCertificateGroup.to_dict(TrustedCertificateGroup)),
                url=self._build_uri("/trustedCertificateGroups"),
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
            return ModelTrustedCertificateGroupView.from_dict(response.json())

    def deleteTrustedCertificateGroupCommand(self, id: str) -> dict:
        """ Delete a Trusted Certificate Group
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/trustedCertificateGroups/{id}"),
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

    def getTrustedCertificateGroupCommand(self, id: str) -> ModelTrustedCertificateGroupView:
        """ Get a Trusted Certificate Group
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/trustedCertificateGroups/{id}"),
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
            return ModelTrustedCertificateGroupView.from_dict(response.json())

    def updateTrustedCertificateGroupCommand(self, id: str, TrustedCertificateGroup: ModelTrustedCertificateGroupView) -> ModelTrustedCertificateGroupView:
        """ Update a TrustedCertificateGroup
        """
        try:
            response = self.session.put(
                data=dumps(TrustedCertificateGroup.to_dict(TrustedCertificateGroup)),
                url=self._build_uri(f"/trustedCertificateGroups/{id}"),
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
            return ModelTrustedCertificateGroupView.from_dict(response.json())
