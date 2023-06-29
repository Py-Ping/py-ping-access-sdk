import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.sites_view import SitesView as ModelSitesView
from pingaccesssdk.models.site_view import SiteView as ModelSiteView


class Sites:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Sites")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSitesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelSitesView:
        """ Get all Sites
        """
        try:
            response = self.session.get(
                url=self._build_uri("/sites"),
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
            return ModelSitesView.from_dict(response.json())

    def addSiteCommand(self, Site: ModelSiteView) -> ModelSiteView:
        """ Create a Site
        """
        try:
            response = self.session.post(
                data=dumps(Site.to_dict(Site)),
                url=self._build_uri("/sites"),
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
            return ModelSiteView.from_dict(response.json())

    def deleteSiteCommand(self, id: str) -> dict:
        """ Delete a Site
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/sites/{id}"),
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

    def getSiteCommand(self, id: str) -> ModelSiteView:
        """ Get a Site
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/sites/{id}"),
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
            return ModelSiteView.from_dict(response.json())

    def updateSiteCommand(self, id: str, Site: ModelSiteView) -> ModelSiteView:
        """ Update a Site
        """
        try:
            response = self.session.put(
                data=dumps(Site.to_dict(Site)),
                url=self._build_uri(f"/sites/{id}"),
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
            return ModelSiteView.from_dict(response.json())
