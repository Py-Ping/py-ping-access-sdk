import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.acme_account_view import AcmeAccountView as ModelAcmeAccountView
from pingaccesssdk.models.acme_server_view import AcmeServerView as ModelAcmeServerView
from pingaccesssdk.models.acme_certificate_request_view import AcmeCertificateRequestView as ModelAcmeCertificateRequestView
from pingaccesssdk.models.acme_servers_view import AcmeServersView as ModelAcmeServersView
from pingaccesssdk.models.link_view import LinkView as ModelLinkView


class Acme:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Acme")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAcmeServersCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelAcmeServersView:
        """ Get all ACME Servers
        """
        try:
            response = self.session.get(
                url=self._build_uri("/acme/servers"),
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
            return ModelAcmeServersView.from_dict(response.json())

    def addAcmeServerCommand(self, AcmeServer: ModelAcmeServerView) -> ModelAcmeServerView:
        """ Add an ACME Server
        """
        try:
            response = self.session.post(
                data=dumps(AcmeServer.to_dict(AcmeServer)),
                url=self._build_uri("/acme/servers"),
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
            return ModelAcmeServerView.from_dict(response.json())

    def getDefaultAcmeServerCommand(self) -> ModelLinkView:
        """ Get the default ACME Server
        """
        try:
            response = self.session.get(
                url=self._build_uri("/acme/servers/default"),
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
            return ModelLinkView.from_dict(response.json())

    def updateDefaultAcmeServerCommand(self, AcmeServer: ModelLinkView) -> ModelLinkView:
        """ Update the default ACME Server
        """
        try:
            response = self.session.put(
                data=dumps(AcmeServer.to_dict(AcmeServer)),
                url=self._build_uri("/acme/servers/default"),
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
            return ModelLinkView.from_dict(response.json())

    def deleteAcmeServerCommand(self, acmeServerId: str) -> ModelAcmeServerView:
        """ Delete an ACME Server
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/acme/servers/{acmeServerId}"),
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
            return ModelAcmeServerView.from_dict(response.json())

    def getAcmeServerCommand(self, acmeServerId: str) -> ModelAcmeServerView:
        """ Get an ACME Server
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/acme/servers/{acmeServerId}"),
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
            return ModelAcmeServerView.from_dict(response.json())

    def getAcmeAccountsCommand(self, acmeServerId: str, page: int = None, numberPerPage: int = None, sortKey: str = None, order: str = None) -> ModelAcmeAccountView:
        """ Get all ACME Accounts
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts"),
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
            return ModelAcmeAccountView.from_dict(response.json())

    def addAcmeAccountCommand(self, acmeServerId: str, AcmeAccount: ModelAcmeAccountView = None) -> ModelAcmeAccountView:
        """ Add an ACME Account
        """
        try:
            response = self.session.post(
                data=dumps(AcmeAccount.to_dict(AcmeAccount)),
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts"),
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
            return ModelAcmeAccountView.from_dict(response.json())

    def deleteAcmeAccountCommand(self, acmeServerId: str, acmeAccountId: str) -> ModelAcmeAccountView:
        """ Delete an ACME Account
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts/{acmeAccountId}"),
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
            return ModelAcmeAccountView.from_dict(response.json())

    def getAcmeAccountCommand(self, acmeServerId: str, acmeAccountId: str) -> ModelAcmeAccountView:
        """ Get an ACME Account
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts/{acmeAccountId}"),
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
            return ModelAcmeAccountView.from_dict(response.json())

    def getAcmeCertificateRequestsCommand(self, acmeServerId: str, acmeAccountId: str, keyPairId: str = None, page: int = None, numberPerPage: int = None, sortKey: str = None, order: str = None) -> ModelAcmeCertificateRequestView:
        """ Get all ACME Certificate Requests
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts/{acmeAccountId}/certificateRequests"),
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
            return ModelAcmeCertificateRequestView.from_dict(response.json())

    def addAcmeCertificateRequestCommand(self, acmeServerId: str, acmeAccountId: str, AcmeCertificateRequest: ModelAcmeCertificateRequestView) -> ModelAcmeCertificateRequestView:
        """ Initiate the ACME protocol
        """
        try:
            response = self.session.post(
                data=dumps(AcmeCertificateRequest.to_dict(AcmeCertificateRequest)),
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts/{acmeAccountId}/certificateRequests"),
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
            return ModelAcmeCertificateRequestView.from_dict(response.json())

    def deleteAcmeCertificateRequestCommand(self, acmeServerId: str, acmeAccountId: str, acmeCertificateRequestId: str) -> ModelAcmeCertificateRequestView:
        """ Delete an ACME Certificate Request
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts/{acmeAccountId}/certificateRequests/{acmeCertificateRequestId}"),
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
            return ModelAcmeCertificateRequestView.from_dict(response.json())

    def getAcmeCertificateRequestCommand(self, acmeServerId: str, acmeAccountId: str, acmeCertificateRequestId: str) -> ModelAcmeCertificateRequestView:
        """ Get an ACME Certificate Request
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/acme/servers/{acmeServerId}/accounts/{acmeAccountId}/certificateRequests/{acmeCertificateRequestId}"),
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
            return ModelAcmeCertificateRequestView.from_dict(response.json())
