from pingaccesssdk.model import Model
from enum import Enum


class EngineRegistrationTokenView(Model):
    """A JWT to be used to initialize self-registration of an engine with its administrative console.

    Attributes
    ----------
    expirationSeconds: int
        The number of seconds after which this token will expire and be unavailable for use to register engines.

    httpProxyId: int
        The ID of the proxy to use for HTTP requests or zero if none.

    httpsProxyId: int
        The ID of the proxy to use for HTTPS requests or zero if none.

    selectedCertificateId: int
        The ID of the certificate the engine will use to contact PingAccess via SSL/TLS.

    """

    def __init__(self, expirationSeconds: int, httpProxyId: int = None, httpsProxyId: int = None, selectedCertificateId: int = None) -> None:
        self.expirationSeconds = expirationSeconds
        self.httpProxyId = httpProxyId
        self.httpsProxyId = httpsProxyId
        self.selectedCertificateId = selectedCertificateId

    def _validate(self) -> bool:
        return any(x for x in ["expirationSeconds"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, EngineRegistrationTokenView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.expirationSeconds, self.httpProxyId, self.httpsProxyId, self.selectedCertificateId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["expirationSeconds", "httpProxyId", "httpsProxyId", "selectedCertificateId"]:
                if k == "expirationSeconds":
                    valid_data[k] = int(v)
                if k == "httpProxyId":
                    valid_data[k] = int(v)
                if k == "httpsProxyId":
                    valid_data[k] = int(v)
                if k == "selectedCertificateId":
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
            if k in ["expirationSeconds", "httpProxyId", "httpsProxyId", "selectedCertificateId"]:
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
