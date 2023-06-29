import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.key_algorithms_view import KeyAlgorithmsView as ModelKeyAlgorithmsView
from pingaccesssdk.models.p_k_c_s_1_2_file_import_doc_view import PKCS12FileImportDocView as ModelPKCS12FileImportDocView
from pingaccesssdk.models.chain_certificates_doc_view import ChainCertificatesDocView as ModelChainCertificatesDocView
from pingaccesssdk.models.key_pairs_view import KeyPairsView as ModelKeyPairsView
from pingaccesssdk.models.new_key_pair_config_view import NewKeyPairConfigView as ModelNewKeyPairConfigView
from pingaccesssdk.models.key_pair_view import KeyPairView as ModelKeyPairView
from pingaccesssdk.models.export_parameters import ExportParameters as ModelExportParameters
from pingaccesssdk.models.c_s_r_response_import_doc_view import CSRResponseImportDocView as ModelCSRResponseImportDocView
from pingaccesssdk.models.san_types import SanTypes as ModelSanTypes


class KeyPairs:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.KeyPairs")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getKeyPairsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, alias: str = None, sortKey: str = None, order: str = None) -> ModelKeyPairsView:
        """ Get all Key Pairs
        """
        try:
            response = self.session.get(
                url=self._build_uri("/keyPairs"),
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
            return ModelKeyPairsView.from_dict(response.json())

    def generateKeyPairCommand(self, NewKeyPairConfigView: ModelNewKeyPairConfigView) -> ModelKeyPairView:
        """ Generate a Key Pair
        """
        try:
            response = self.session.post(
                data=dumps(NewKeyPairConfigView.to_dict(NewKeyPairConfigView)),
                url=self._build_uri("/keyPairs/generate"),
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
            return ModelKeyPairView.from_dict(response.json())

    def importKeyPairCommand(self, KeyPairFile: ModelPKCS12FileImportDocView) -> ModelKeyPairView:
        """ Import a Key Pair from either a PKCS12 or PEM file
        """
        try:
            response = self.session.post(
                data=dumps(KeyPairFile.to_dict(KeyPairFile)),
                url=self._build_uri("/keyPairs/import"),
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
            return ModelKeyPairView.from_dict(response.json())

    def keyAlgorithms(self) -> ModelKeyAlgorithmsView:
        """ Get the key algorithms supported by Key Pair generation
        """
        try:
            response = self.session.get(
                url=self._build_uri("/keyPairs/keyAlgorithms"),
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
            return ModelKeyAlgorithmsView.from_dict(response.json())

    def getKeypairsCreatableGeneralNamesCommand(self) -> ModelSanTypes:
        """ Get the valid General Names for creating Subject Alternative Names
        """
        try:
            response = self.session.get(
                url=self._build_uri("/keyPairs/subjectAlternativeTypes"),
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
            return ModelSanTypes.from_dict(response.json())

    def deleteKeyPairCommand(self, id: str) -> dict:
        """ Delete a Key Pair
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/keyPairs/{id}"),
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

    def getKeyPairCommand(self, id: str) -> ModelKeyPairView:
        """ Get a Key Pair
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/{id}"),
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
            return ModelKeyPairView.from_dict(response.json())

    def patchKeyPairCommand(self, id: str, addChainCertificates: ModelChainCertificatesDocView) -> ModelKeyPairView:
        """ Update the chainCertificates of a Key Pair
        """
        try:
            response = self.session.patch(
                url=self._build_uri(f"/keyPairs/{id}"),
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
            return ModelKeyPairView.from_dict(response.json())

    def updateKeyPairCommand(self, id: str, PKCS12File: ModelPKCS12FileImportDocView) -> ModelKeyPairView:
        """ Update a Key Pair
        """
        try:
            response = self.session.put(
                data=dumps(PKCS12File.to_dict(PKCS12File)),
                url=self._build_uri(f"/keyPairs/{id}"),
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
            return ModelKeyPairView.from_dict(response.json())

    def exportKeyPairCert(self, id: str) -> dict:
        """ Export only the Certificate from a Key Pair
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/{id}/certificate"),
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

    def generateCsrCommand(self, id: str) -> dict:
        """ Generate a Certificate Signing Request for a Key Pair
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/{id}/csr"),
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

    def importCSRResponseCommand(self, id: str, CSRResponse: ModelCSRResponseImportDocView) -> ModelKeyPairView:
        """ Import a Certificate Signing Request response
        """
        try:
            response = self.session.post(
                data=dumps(CSRResponse.to_dict(CSRResponse)),
                url=self._build_uri(f"/keyPairs/{id}/csr"),
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
            return ModelKeyPairView.from_dict(response.json())

    def exportKeyPairPemCommand(self, id: str, ExportParameters: ModelExportParameters) -> dict:
        """ Export a Key Pair in the PEM file format
        """
        try:
            response = self.session.post(
                data=dumps(ExportParameters.to_dict(ExportParameters)),
                url=self._build_uri(f"/keyPairs/{id}/pem"),
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

    def exportKeyPairPkcs12Command(self, id: str, ExportParameters: ModelExportParameters) -> dict:
        """ Export a Key Pair in the PKCS12 file format
        """
        try:
            response = self.session.post(
                data=dumps(ExportParameters.to_dict(ExportParameters)),
                url=self._build_uri(f"/keyPairs/{id}/pkcs12"),
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

    def deleteChainCertificateCommand(self, keyPairId: str, chainCertificateId: str) -> dict:
        """ Delete a Chain Certificate
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/keyPairs/{keyPairId}/chainCertificates/{chainCertificateId}"),
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
