import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.access_token_validator_view import AccessTokenValidatorView as ModelAccessTokenValidatorView
from pingaccesssdk.models.access_token_validators_view import AccessTokenValidatorsView as ModelAccessTokenValidatorsView
from pingaccesssdk.models.descriptors_view import DescriptorsView as ModelDescriptorsView


class AccessTokenValidators:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AccessTokenValidators")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAccessTokenValidatorsCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelAccessTokenValidatorsView:
        """ Get all Access Token Validators
        """
        try:
            response = self.session.get(
                url=self._build_uri("/accessTokenValidators"),
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
            return ModelAccessTokenValidatorsView.from_dict(response.json())

    def addAccessTokenValidatorCommand(self, AccessTokenValidator: ModelAccessTokenValidatorView) -> ModelAccessTokenValidatorView:
        """ Create an Access Token Validator
        """
        try:
            response = self.session.post(
                data=dumps(AccessTokenValidator.to_dict(AccessTokenValidator)),
                url=self._build_uri("/accessTokenValidators"),
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
            return ModelAccessTokenValidatorView.from_dict(response.json())

    def getAccessTokenValidatorDescriptorsCommand(self) -> ModelDescriptorsView:
        """ Get descriptors for all Access Token Validators
        """
        try:
            response = self.session.get(
                url=self._build_uri("/accessTokenValidators/descriptors"),
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
            return ModelDescriptorsView.from_dict(response.json())

    def deleteAccessTokenValidatorCommand(self, id: str) -> dict:
        """ Delete a Access Token Validator
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/accessTokenValidators/{id}"),
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

    def getAccessTokenValidatorCommand(self, id: str) -> ModelAccessTokenValidatorView:
        """ Get an Access Token Validator
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/accessTokenValidators/{id}"),
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
            return ModelAccessTokenValidatorView.from_dict(response.json())

    def updateAccessTokenValidatorCommand(self, id: str, AccessTokenValidator: ModelAccessTokenValidatorView) -> ModelAccessTokenValidatorView:
        """ Update an Access Token Validator
        """
        try:
            response = self.session.put(
                data=dumps(AccessTokenValidator.to_dict(AccessTokenValidator)),
                url=self._build_uri(f"/accessTokenValidators/{id}"),
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
            return ModelAccessTokenValidatorView.from_dict(response.json())
