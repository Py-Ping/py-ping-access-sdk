from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_auth_client_credentials_view import OAuthClientCredentialsView
from pingaccesssdk.enums import AuditLevel


class AuthorizationServerView(Model):
    """The third-party OAuth 2.0 Authorization Server configuration.

    Attributes
    ----------
    auditLevel: AuditLevel
        Enable to record requests to third-party OAuth 2.0 Authorization Server to the audit store.

    cacheTokens: bool
        Enable to retain token details for subsequent requests.

    clientCredentials: OAuthClientCredentialsView
        Specify the client credentials.

    description: str
        The description of the third-party OAuth 2.0 Authorization Server.

    introspectionEndpoint: str
        The third-party OAuth 2.0 Authorization Server's token introspection endpoint.

    secure: bool
        Enable if third-party OAuth 2.0 Authorization Server is expecting HTTPS connections.

    sendAudience: bool
        Enable to send the URI the user requested as the 'aud' OAuth parameter for PingAccess to the OAuth 2.0 Authorization server.

    subjectAttributeName: str
        The attribute you want to use from the OAuth access token as the subject for auditing purposes.

    targets: list
        One or more server hostname:port pairs used to access third-party OAuth 2.0 Authorization Server.

    tokenEndpoint: str
        The third-party OAuth 2.0 Authorization Server's token endpoint.

    tokenTimeToLiveSeconds: int
        Defines the number of seconds to cache the access token. -1 means no limit. This value should be less than the PingFederate Token Lifetime.

    trustedCertificateGroupId: int
        The group of certificates to use when authenticating to third-party OAuth 2.0 Authorization Server.

    useProxy: bool
        True if a proxy should be used for HTTP or HTTPS requests.

    """

    def __init__(self, introspectionEndpoint: str, subjectAttributeName: str, targets: list, trustedCertificateGroupId: int, auditLevel: AuditLevel = None, cacheTokens: bool = None, clientCredentials: OAuthClientCredentialsView = None, description: str = None, secure: bool = None, sendAudience: bool = None, tokenEndpoint: str = None, tokenTimeToLiveSeconds: int = None, useProxy: bool = None) -> None:
        self.auditLevel = auditLevel
        self.cacheTokens = cacheTokens
        self.clientCredentials = clientCredentials
        self.description = description
        self.introspectionEndpoint = introspectionEndpoint
        self.secure = secure
        self.sendAudience = sendAudience
        self.subjectAttributeName = subjectAttributeName
        self.targets = targets
        self.tokenEndpoint = tokenEndpoint
        self.tokenTimeToLiveSeconds = tokenTimeToLiveSeconds
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy

    def _validate(self) -> bool:
        return any(x for x in ["introspectionEndpoint", "subjectAttributeName", "targets", "trustedCertificateGroupId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthorizationServerView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.auditLevel, self.cacheTokens, self.clientCredentials, self.description, self.introspectionEndpoint, self.secure, self.sendAudience, self.subjectAttributeName, self.targets, self.tokenEndpoint, self.tokenTimeToLiveSeconds, self.trustedCertificateGroupId, self.useProxy]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["auditLevel", "cacheTokens", "clientCredentials", "description", "introspectionEndpoint", "secure", "sendAudience", "subjectAttributeName", "targets", "tokenEndpoint", "tokenTimeToLiveSeconds", "trustedCertificateGroupId", "useProxy"]:
                if k == "auditLevel":
                    valid_data[k] = AuditLevel[v]
                if k == "cacheTokens":
                    valid_data[k] = bool(v)
                if k == "clientCredentials":
                    valid_data[k] = OAuthClientCredentialsView(**v) if v is not None else None
                if k == "description":
                    valid_data[k] = str(v)
                if k == "introspectionEndpoint":
                    valid_data[k] = str(v)
                if k == "secure":
                    valid_data[k] = bool(v)
                if k == "sendAudience":
                    valid_data[k] = bool(v)
                if k == "subjectAttributeName":
                    valid_data[k] = str(v)
                if k == "targets":
                    valid_data[k] = [str(x) for x in v]
                if k == "tokenEndpoint":
                    valid_data[k] = str(v)
                if k == "tokenTimeToLiveSeconds":
                    valid_data[k] = int(v)
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
            if k in ["auditLevel", "cacheTokens", "clientCredentials", "description", "introspectionEndpoint", "secure", "sendAudience", "subjectAttributeName", "targets", "tokenEndpoint", "tokenTimeToLiveSeconds", "trustedCertificateGroupId", "useProxy"]:
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
