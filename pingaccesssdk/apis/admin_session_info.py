import os
import logging
import traceback

from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.session_info import SessionInfo as ModelSessionInfo


class AdminSessionInfo:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AdminSessionInfo")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def adminSessionDeleteCommand(self) -> dict:
        """ Invalidate the Admin session information
        """
        try:
            response = self.session.delete(
                url=self._build_uri("/adminSessionInfo"),
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

    def adminSessionInfoCommand(self) -> ModelSessionInfo:
        """ Return the Admin session information
        """
        try:
            response = self.session.get(
                url=self._build_uri("/adminSessionInfo"),
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
            return ModelSessionInfo.from_dict(response.json())

    def adminSessionInfoCheckCommand(self) -> ModelSessionInfo:
        """ Return the Admin session information without affecting session expiration
        """
        try:
            response = self.session.get(
                url=self._build_uri("/adminSessionInfo/checkOnly"),
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
            return ModelSessionInfo.from_dict(response.json())
