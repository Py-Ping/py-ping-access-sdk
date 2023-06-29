import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.x_5_0_9_file_import_doc_view import X509FileImportDocView as ModelX509FileImportDocView
from pingaccesssdk.models.trusted_cert_view import TrustedCertView as ModelTrustedCertView
from pingaccesssdk.models.trusted_certs_view import TrustedCertsView as ModelTrustedCertsView


class Certificates:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Certificates")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getTrustedCerts(self, page: int = None, numberPerPage: int = None, filter: str = None, alias: str = None, sortKey: str = None, order: str = None) -> ModelTrustedCertsView:
        """ Get all Certificates
        """
        try:
            response = self.session.get(
                url=self._build_uri("/certificates"),
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
            return ModelTrustedCertsView.from_dict(response.json())

    def importTrustedCert(self, X509File: ModelX509FileImportDocView) -> dict:
        """ Import a Certificate
        """
        try:
            response = self.session.post(
                data=dumps(X509File.to_dict(X509File)),
                url=self._build_uri("/certificates"),
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

    def deleteTrustedCertCommand(self, id: str) -> dict:
        """ Delete a Certificate
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/certificates/{id}"),
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

    def getTrustedCert(self, id: str) -> ModelTrustedCertView:
        """ Get a Certificate
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/certificates/{id}"),
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
            return ModelTrustedCertView.from_dict(response.json())

    def updateTrustedCert(self, id: str, X509File: ModelX509FileImportDocView) -> dict:
        """ Update a Certificate
        """
        try:
            response = self.session.put(
                data=dumps(X509File.to_dict(X509File)),
                url=self._build_uri(f"/certificates/{id}"),
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

    def exportTrustedCert(self, id: str) -> dict:
        """ Export a Certificate
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/certificates/{id}/file"),
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
