import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.user_view import UserView as ModelUserView
from pingaccesssdk.models.users_view import UsersView as ModelUsersView
from pingaccesssdk.models.user_password_view import UserPasswordView as ModelUserPasswordView


class Users:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Users")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getUsersCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, username: str = None, sortKey: str = None, order: str = None) -> ModelUsersView:
        """ Get all Users
        """
        try:
            response = self.session.get(
                url=self._build_uri("/users"),
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
            return ModelUsersView.from_dict(response.json())

    def getUserCommand(self, id: str) -> ModelUserView:
        """ Get a User
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/users/{id}"),
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
            return ModelUserView.from_dict(response.json())

    def updateUserCommand(self, id: str, user: ModelUserView) -> ModelUserView:
        """ Update a User
        """
        try:
            response = self.session.put(
                data=dumps(user.to_dict(user)),
                url=self._build_uri(f"/users/{id}"),
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
            return ModelUserView.from_dict(response.json())

    def updateUserPasswordCommand(self, id: str, user: ModelUserPasswordView) -> dict:
        """ Update a User's Password
        """
        try:
            response = self.session.put(
                data=dumps(user.to_dict(user)),
                url=self._build_uri(f"/users/{id}/password"),
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
