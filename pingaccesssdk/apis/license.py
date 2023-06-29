import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.license_import_doc_view import LicenseImportDocView as ModelLicenseImportDocView
from pingaccesssdk.models.license_view import LicenseView as ModelLicenseView


class License:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.License")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getLicenseCommand(self) -> ModelLicenseView:
        """ Get the License File
        """
        try:
            response = self.session.get(
                url=self._build_uri("/license"),
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
            return ModelLicenseView.from_dict(response.json())

    def importLicenseCommand(self, LicenseFile: ModelLicenseImportDocView) -> ModelLicenseView:
        """ Import a License
        """
        try:
            response = self.session.post(
                data=dumps(LicenseFile.to_dict(LicenseFile)),
                url=self._build_uri("/license"),
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
            return ModelLicenseView.from_dict(response.json())
