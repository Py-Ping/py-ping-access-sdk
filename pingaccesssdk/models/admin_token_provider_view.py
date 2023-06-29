from pingaccesssdk.model import Model
from enum import Enum


class AdminTokenProviderView(Model):
    """An Admin Token Provider.

    Attributes
    ----------
    description: str
        The description of the Admin Token Provider.

    issuer: str
        The issuer url of the Admin Token Provider.

    sslCiphers: list
        Array of SSL ciphers to use for HTTPS requests. Empty to use all available ciphers.

    sslProtocols: list
        Array of SSL protocolsto use for HTTPS requests. Empty to use all available protocols.

    trustedCertificateGroupId: int
        The group of certificates to use when authenticating to the Admin Token Provider.

    useProxy: bool
        True if a proxy should be used for HTTPS requests.

    """

    def __init__(self, issuer: str, sslCiphers: list, sslProtocols: list, description: str = None, trustedCertificateGroupId: int = None, useProxy: bool = None) -> None:
        self.description = description
        self.issuer = issuer
        self.sslCiphers = sslCiphers
        self.sslProtocols = sslProtocols
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy

    def _validate(self) -> bool:
        return any(x for x in ["issuer", "sslCiphers", "sslProtocols"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AdminTokenProviderView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.description, self.issuer, self.sslCiphers, self.sslProtocols, self.trustedCertificateGroupId, self.useProxy]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["description", "issuer", "sslCiphers", "sslProtocols", "trustedCertificateGroupId", "useProxy"]:
                if k == "description":
                    valid_data[k] = str(v)
                if k == "issuer":
                    valid_data[k] = str(v)
                if k == "sslCiphers":
                    valid_data[k] = [str(x) for x in v]
                if k == "sslProtocols":
                    valid_data[k] = [str(x) for x in v]
                if k == "trustedCertificateGroupId":
                    valid_data[k] = int(v)
                if k == "useProxy":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["description", "issuer", "sslCiphers", "sslProtocols", "trustedCertificateGroupId", "useProxy"]:
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
