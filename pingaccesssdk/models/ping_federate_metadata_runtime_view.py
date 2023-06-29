from pingaccesssdk.model import Model
from enum import Enum


class PingFederateMetadataRuntimeView(Model):
    """A PingFederate configuration.

    Attributes
    ----------
    description: str
        The description of the PingFederate Runtime token provider.

    issuer: str
        The issuer url of the PingFederate token provider.

    skipHostnameVerification: bool
        Set to true if HTTP communications to PingFederate should not perform hostname verification of the certificate.

    stsTokenExchangeEndpoint: str
        The url of the PingFederate STS token-to-token exchange endpoint that is used for token mediation. Specify if it is being served from a different host/port than the issuer is. Otherwise, it is assumed to be {{issuer}}/pf/sts.wst.

    trustedCertificateGroupId: int
        The group of certificates to use when authenticating to PingFederate.

    useProxy: bool
        Set to true if a proxy should be used for HTTP or HTTPS requests.

    useSlo: bool
        Set to true if OIDC single log out should be used on the /pa/oidc/logout on the engines.

    """

    def __init__(self, issuer: str, description: str = None, skipHostnameVerification: bool = None, stsTokenExchangeEndpoint: str = None, trustedCertificateGroupId: int = None, useProxy: bool = None, useSlo: bool = None) -> None:
        self.description = description
        self.issuer = issuer
        self.skipHostnameVerification = skipHostnameVerification
        self.stsTokenExchangeEndpoint = stsTokenExchangeEndpoint
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy
        self.useSlo = useSlo

    def _validate(self) -> bool:
        return any(x for x in ["issuer"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingFederateMetadataRuntimeView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.description, self.issuer, self.skipHostnameVerification, self.stsTokenExchangeEndpoint, self.trustedCertificateGroupId, self.useProxy, self.useSlo]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["description", "issuer", "skipHostnameVerification", "stsTokenExchangeEndpoint", "trustedCertificateGroupId", "useProxy", "useSlo"]:
                if k == "description":
                    valid_data[k] = str(v)
                if k == "issuer":
                    valid_data[k] = str(v)
                if k == "skipHostnameVerification":
                    valid_data[k] = bool(v)
                if k == "stsTokenExchangeEndpoint":
                    valid_data[k] = str(v)
                if k == "trustedCertificateGroupId":
                    valid_data[k] = int(v)
                if k == "useProxy":
                    valid_data[k] = bool(v)
                if k == "useSlo":
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
            if k in ["description", "issuer", "skipHostnameVerification", "stsTokenExchangeEndpoint", "trustedCertificateGroupId", "useProxy", "useSlo"]:
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
