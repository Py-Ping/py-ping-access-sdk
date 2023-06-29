from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_auth_client_credentials_view import OAuthClientCredentialsView
from pingaccesssdk.models.hidden_field_view import HiddenFieldView


class PingFederateAccessTokenView(Model):
    """A PingAccess OAuth client configuration.

    Attributes
    ----------
    accessValidatorId: int
        The Access Validator Id. This field is read-only.

    cacheTokens: bool
        Enable to retain token details for subsequent requests.

    clientCredentials: OAuthClientCredentialsView
        Specify the credentials for the OAuth client configured in PingFederate.

    clientId: str
        The Client ID which PingAccess should use when requesting PingFederate to validate access tokens. The client must have Access Token Validation grant type allowed. (DEPRECATED - to be removed in a future release; please use 'clientCredentials' instead)

    clientSecret: HiddenFieldView
        The Client Secret for the Client ID. (DEPRECATED - to be removed in a future release; please use 'clientCredentials' instead)

    name: str
        The unique Access Validator name. This field is read-only.

    sendAudience: bool
        Enable to send the URI the user requested as the 'aud' OAuth parameter for PingAccess to use to select an Access Token Manager.

    subjectAttributeName: str
        The attribute you want to use from the OAuth access token as the subject for auditing purposes.

    tokenTimeToLiveSeconds: int
        Defines the number of seconds to cache the access token. -1 means no limit. This value should be less than the PingFederate Token Lifetime.

    useTokenIntrospection: bool
        Specify if token introspection is enabled.

    """

    def __init__(self, accessValidatorId: int, subjectAttributeName: str, cacheTokens: bool = None, clientCredentials: OAuthClientCredentialsView = None, clientId: str = None, clientSecret: HiddenFieldView = None, name: str = None, sendAudience: bool = None, tokenTimeToLiveSeconds: int = None, useTokenIntrospection: bool = None) -> None:
        self.accessValidatorId = accessValidatorId
        self.cacheTokens = cacheTokens
        self.clientCredentials = clientCredentials
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.name = name
        self.sendAudience = sendAudience
        self.subjectAttributeName = subjectAttributeName
        self.tokenTimeToLiveSeconds = tokenTimeToLiveSeconds
        self.useTokenIntrospection = useTokenIntrospection

    def _validate(self) -> bool:
        return any(x for x in ["accessValidatorId", "subjectAttributeName"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingFederateAccessTokenView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.accessValidatorId, self.cacheTokens, self.clientCredentials, self.clientId, self.clientSecret, self.name, self.sendAudience, self.subjectAttributeName, self.tokenTimeToLiveSeconds, self.useTokenIntrospection]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["accessValidatorId", "cacheTokens", "clientCredentials", "clientId", "clientSecret", "name", "sendAudience", "subjectAttributeName", "tokenTimeToLiveSeconds", "useTokenIntrospection"]:
                if k == "accessValidatorId":
                    valid_data[k] = int(v)
                if k == "cacheTokens":
                    valid_data[k] = bool(v)
                if k == "clientCredentials":
                    valid_data[k] = OAuthClientCredentialsView(**v) if v is not None else None
                if k == "clientId":
                    valid_data[k] = str(v)
                if k == "clientSecret":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None
                if k == "name":
                    valid_data[k] = str(v)
                if k == "sendAudience":
                    valid_data[k] = bool(v)
                if k == "subjectAttributeName":
                    valid_data[k] = str(v)
                if k == "tokenTimeToLiveSeconds":
                    valid_data[k] = int(v)
                if k == "useTokenIntrospection":
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
            if k in ["accessValidatorId", "cacheTokens", "clientCredentials", "clientId", "clientSecret", "name", "sendAudience", "subjectAttributeName", "tokenTimeToLiveSeconds", "useTokenIntrospection"]:
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
