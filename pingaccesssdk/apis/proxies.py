import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingaccesssdk.models.http_client_proxy_view import HttpClientProxyView as ModelHttpClientProxyView


class Proxies:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Proxies")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getProxiesCommand(self, page: int = None, numberPerPage: int = None, filter: str = None, name: str = None, sortKey: str = None, order: str = None) -> ModelHttpClientProxyView:
        """ Get all Proxies
        """
        try:
            response = self.session.get(
                url=self._build_uri("/proxies"),
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
            return ModelHttpClientProxyView.from_dict(response.json())

    def addProxyCommand(self, Proxy: ModelHttpClientProxyView) -> ModelHttpClientProxyView:
        """ Create a Proxy
        """
        try:
            response = self.session.post(
                data=dumps(Proxy.to_dict(Proxy)),
                url=self._build_uri("/proxies"),
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
            return ModelHttpClientProxyView.from_dict(response.json())

    def deleteProxyCommand(self, id: str) -> dict:
        """ Delete a Proxy
        """
        try:
            response = self.session.delete(
                url=self._build_uri(f"/proxies/{id}"),
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

    def getProxyCommand(self, id: str) -> ModelHttpClientProxyView:
        """ Get a Proxy
        """
        try:
            response = self.session.get(
                url=self._build_uri(f"/proxies/{id}"),
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
            return ModelHttpClientProxyView.from_dict(response.json())

    def updateProxyCommand(self, id: str, Proxy: ModelHttpClientProxyView) -> ModelHttpClientProxyView:
        """ Update a Proxy
        """
        try:
            response = self.session.put(
                data=dumps(Proxy.to_dict(Proxy)),
                url=self._build_uri(f"/proxies/{id}"),
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
            return ModelHttpClientProxyView.from_dict(response.json())
