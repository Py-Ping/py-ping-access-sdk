from pingaccesssdk.model import Model
from enum import Enum


class AdminConfigurationView(Model):
    """An admin configuration.

    Attributes
    ----------
    hostPort: str
        The primary host and port of the administrative console.

    httpProxyId: int
        The ID of the proxy to use for HTTP requests or zero if none.

    httpsProxyId: int
        The ID of the proxy to use for HTTPS requests or zero if none.

    """

    def __init__(self, hostPort: str, httpProxyId: int = None, httpsProxyId: int = None) -> None:
        self.hostPort = hostPort
        self.httpProxyId = httpProxyId
        self.httpsProxyId = httpsProxyId

    def _validate(self) -> bool:
        return any(x for x in ["hostPort"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AdminConfigurationView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.hostPort, self.httpProxyId, self.httpsProxyId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["hostPort", "httpProxyId", "httpsProxyId"]:
                if k == "hostPort":
                    valid_data[k] = str(v)
                if k == "httpProxyId":
                    valid_data[k] = int(v)
                if k == "httpsProxyId":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["hostPort", "httpProxyId", "httpsProxyId"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
