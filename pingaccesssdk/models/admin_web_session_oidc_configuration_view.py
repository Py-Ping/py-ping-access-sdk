from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_auth_client_credentials_view import OAuthClientCredentialsView
from pingaccesssdk.enums import OidcLoginType
from pingaccesssdk.enums import PkceChallengeTypeView


class AdminWebSessionOidcConfigurationView(Model):
    """An admin web session OIDC configuration.

    Attributes
    ----------
    cacheUserAttributes: bool
        Specify if PingAccess should cache user attribute information for use in policy decisions. When disabled, this data is encoded and stored in the session cookie.

    clientCredentials: OAuthClientCredentialsView
        Specify the client credentials.

    enableRefreshUser: bool
        Specify if you want to have PingAccess periodically refresh user data from PingFederate for use in policy decisions.

    oidcLoginType: OidcLoginType
        The web session token type.

    pfsessionStateCacheInSeconds: int
        Specify the number of seconds to cache PingFederate Session State information.

    pkceChallengeType: PkceChallengeTypeView
        (sortable) Specify the code_challenge_method to use for PKCE during the Code login flow. OFF signifies to not use PKCE.

    refreshUserInfoClaimsInterval: int
        Specify the maximum number of seconds to cache user attribute information when the Refresh User is enabled.

    scopes: list
        The list of scopes. The openid scope is implied and does not need to be specified in this list.

    sendRequestedUrlToProvider: bool
        Specify if you want to send the requested URL as part of the authentication request to the OpenID Connect Provider.

    validateSessionIsAlive: bool
        Specify if PingAccess should validate sessions with the configured PingFederate instance during request processing.

    """

    def __init__(self, clientCredentials: OAuthClientCredentialsView, cacheUserAttributes: bool = None, enableRefreshUser: bool = None, oidcLoginType: OidcLoginType = None, pfsessionStateCacheInSeconds: int = None, pkceChallengeType: PkceChallengeTypeView = None, refreshUserInfoClaimsInterval: int = None, scopes: list = None, sendRequestedUrlToProvider: bool = None, validateSessionIsAlive: bool = None) -> None:
        self.cacheUserAttributes = cacheUserAttributes
        self.clientCredentials = clientCredentials
        self.enableRefreshUser = enableRefreshUser
        self.oidcLoginType = oidcLoginType
        self.pfsessionStateCacheInSeconds = pfsessionStateCacheInSeconds
        self.pkceChallengeType = pkceChallengeType
        self.refreshUserInfoClaimsInterval = refreshUserInfoClaimsInterval
        self.scopes = scopes
        self.sendRequestedUrlToProvider = sendRequestedUrlToProvider
        self.validateSessionIsAlive = validateSessionIsAlive

    def _validate(self) -> bool:
        return any(x for x in ["clientCredentials"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AdminWebSessionOidcConfigurationView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.cacheUserAttributes, self.clientCredentials, self.enableRefreshUser, self.oidcLoginType, self.pfsessionStateCacheInSeconds, self.pkceChallengeType, self.refreshUserInfoClaimsInterval, self.scopes, self.sendRequestedUrlToProvider, self.validateSessionIsAlive]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["cacheUserAttributes", "clientCredentials", "enableRefreshUser", "oidcLoginType", "pfsessionStateCacheInSeconds", "pkceChallengeType", "refreshUserInfoClaimsInterval", "scopes", "sendRequestedUrlToProvider", "validateSessionIsAlive"]:
                if k == "cacheUserAttributes":
                    valid_data[k] = bool(v)
                if k == "clientCredentials":
                    valid_data[k] = OAuthClientCredentialsView(**v) if v is not None else None
                if k == "enableRefreshUser":
                    valid_data[k] = bool(v)
                if k == "oidcLoginType":
                    valid_data[k] = OidcLoginType[v]
                if k == "pfsessionStateCacheInSeconds":
                    valid_data[k] = int(v)
                if k == "pkceChallengeType":
                    valid_data[k] = PkceChallengeTypeView[v]
                if k == "refreshUserInfoClaimsInterval":
                    valid_data[k] = int(v)
                if k == "scopes":
                    valid_data[k] = [str(x) for x in v]
                if k == "sendRequestedUrlToProvider":
                    valid_data[k] = bool(v)
                if k == "validateSessionIsAlive":
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
            if k in ["cacheUserAttributes", "clientCredentials", "enableRefreshUser", "oidcLoginType", "pfsessionStateCacheInSeconds", "pkceChallengeType", "refreshUserInfoClaimsInterval", "scopes", "sendRequestedUrlToProvider", "validateSessionIsAlive"]:
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
