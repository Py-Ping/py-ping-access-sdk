from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_auth_client_credentials_view import OAuthClientCredentialsView
from pingaccesssdk.enums import ConfiguredAuthorizationServerType


class OAuthAuthenticationConfigurationView(Model):
    """Required when the authentication type is 'OAuth'.

    Attributes
    ----------
    clientCredentials: OAuthClientCredentialsView
        Specify the credentials for the OAuth client configured in the Token Provider.

    configuredAuthorizationServerType: ConfiguredAuthorizationServerType
        Specify an Authorization Server configured within PA that will be used for obtaining an access token. Default value is 'PINGFEDERATE_RUNTIME'.

    scopes: list
        The required scopes of validated ATs authorized to call the PingFederate administrative API. Scopes can be input as an array of case-sensitive strings.

    """

    def __init__(self, clientCredentials: OAuthClientCredentialsView, configuredAuthorizationServerType: ConfiguredAuthorizationServerType, scopes: list = None) -> None:
        self.clientCredentials = clientCredentials
        self.configuredAuthorizationServerType = configuredAuthorizationServerType
        self.scopes = scopes

    def _validate(self) -> bool:
        return any(x for x in ["clientCredentials", "configuredAuthorizationServerType"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OAuthAuthenticationConfigurationView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.clientCredentials, self.configuredAuthorizationServerType, self.scopes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["clientCredentials", "configuredAuthorizationServerType", "scopes"]:
                if k == "clientCredentials":
                    valid_data[k] = OAuthClientCredentialsView(**v) if v is not None else None
                if k == "configuredAuthorizationServerType":
                    valid_data[k] = ConfiguredAuthorizationServerType[v]
                if k == "scopes":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["clientCredentials", "configuredAuthorizationServerType", "scopes"]:
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
