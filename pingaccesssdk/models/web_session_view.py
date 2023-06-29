from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_auth_client_credentials_view import OAuthClientCredentialsView
from pingaccesssdk.enums import WebSessionCookieType
from pingaccesssdk.enums import RequestPreservationType
from pingaccesssdk.enums import OidcLoginType
from pingaccesssdk.enums import SameSiteTypeView
from pingaccesssdk.enums import WebStorageType
from pingaccesssdk.enums import PkceChallengeTypeView


class WebSessionView(Model):
    """A web session.

    Attributes
    ----------
    id: int
        When creating a new WebSession, this is the ID for the WebSession. If not specified, an ID will be automatically assigned. When updating an existing WebSession, this field is ignored and the ID is determined by the path parameter.

    audience: str
        (sortable) Enter a unique identifier between 1 and 32 characters that defines who the PA Token is applicable to.

    cacheUserAttributes: bool
        (sortable) Specify if PingAccess should cache user attribute information for use in policy decisions. When disabled, this data is encoded and stored in the session cookie.

    clientCredentials: OAuthClientCredentialsView
        Specify the client credentials.

    cookieDomain: str
        (sortable) The domain where the cookie is stored--for example, corp.yourcompany.com.

    cookieType: WebSessionCookieType
        (sortable) Specify an Encrypted JWT or a Signed JWT web session cookie. Default is Encrypted.

    enableRefreshUser: bool
        (sortable) Specify if you want to have PingAccess periodically refresh user data from PingFederate for use in policy decisions.

    failOnUnsupportedPreservationContentType: bool
        (sortable) Specify if PingAccess should produce a 415 HTTP response when it receives an unauthenticated POST request with a content type unsupported by request preservation. The only content type supported by request preservation is application/x-www-form-urlencoded. When disabled, PingAccess will challenge an unauthenticated POST request using an unsupported content type with the same challenge response sent to an unauthenticated GET request. The default is false.

    httpOnlyCookie: bool
        (sortable) Enable the HttpOnly flag on cookies that contain the PA Token.

    idleTimeoutInMinutes: int
        (sortable) The length of time you want the PingAccess Token to remain active when no activity is detected.

    name: str
        (sortable) The name of the web session.

    oidcLoginType: OidcLoginType
        (sortable) The web session token type.

    pfsessionStateCacheInSeconds: int
        (sortable) Specify the number of seconds to cache PingFederate Session State information.

    pkceChallengeType: PkceChallengeTypeView
        (sortable) Specify the code_challenge_method to use for PKCE during the Code login flow. OFF signifies to not use PKCE.

    refreshUserInfoClaimsInterval: int
        (sortable) Specify the maximum number of seconds to cache user attribute information when the Refresh User is enabled.

    requestPreservationType: RequestPreservationType
        (sortable) Specify the types of request data to be preserved if the user is redirected to an authentication page when submitting information to a protected resource.

    requestProfile: bool
        Specifies whether the default scopes ('profile', 'email', 'address', and 'phone') should be specified in the access request. (DEPRECATED - to be removed in a future release; please use 'scopes' instead)

    sameSite: SameSiteTypeView
        (sortable) Specify the SameSite attribute to be used when setting the PingAccess Cookie. Default is None which allows the cookie to be used in a third-party context. If the cookie is not used in a third-party context then Lax is recommended.

    scopes: list
        The list of scopes to be specified in the access request. If not specified, the default scopes ('profile', 'email', 'address', and 'phone') will be used. The openid scope is implied and does not need to be specified in this list.

    secureCookie: bool
        (sortable) Specify whether the PingAccess Cookie must be sent using only HTTPS connections.

    sendRequestedUrlToProvider: bool
        (sortable) Specify if you want to send the requested URL as part of the authentication request to the OpenID Connect Provider.

    sessionTimeoutInMinutes: int
        (sortable) The length of time you want the PA Token to remain active. Once the PA Token expires, an authenticated user must re-authenticate.

    validateSessionIsAlive: bool
        (sortable) Specify if PingAccess should validate sessions with the configured PingFederate instance during request processing.

    webStorageType: WebStorageType
        (sortable) Specify the type of web storage to use for request preservation data.  Default is SessionStorage.

    """

    def __init__(self, audience: str, clientCredentials: OAuthClientCredentialsView, failOnUnsupportedPreservationContentType: bool, name: str, id: int = None, cacheUserAttributes: bool = None, cookieDomain: str = None, cookieType: WebSessionCookieType = None, enableRefreshUser: bool = None, httpOnlyCookie: bool = None, idleTimeoutInMinutes: int = None, oidcLoginType: OidcLoginType = None, pfsessionStateCacheInSeconds: int = None, pkceChallengeType: PkceChallengeTypeView = None, refreshUserInfoClaimsInterval: int = None, requestPreservationType: RequestPreservationType = None, requestProfile: bool = None, sameSite: SameSiteTypeView = None, scopes: list = None, secureCookie: bool = None, sendRequestedUrlToProvider: bool = None, sessionTimeoutInMinutes: int = None, validateSessionIsAlive: bool = None, webStorageType: WebStorageType = None) -> None:
        self.id = id
        self.audience = audience
        self.cacheUserAttributes = cacheUserAttributes
        self.clientCredentials = clientCredentials
        self.cookieDomain = cookieDomain
        self.cookieType = cookieType
        self.enableRefreshUser = enableRefreshUser
        self.failOnUnsupportedPreservationContentType = failOnUnsupportedPreservationContentType
        self.httpOnlyCookie = httpOnlyCookie
        self.idleTimeoutInMinutes = idleTimeoutInMinutes
        self.name = name
        self.oidcLoginType = oidcLoginType
        self.pfsessionStateCacheInSeconds = pfsessionStateCacheInSeconds
        self.pkceChallengeType = pkceChallengeType
        self.refreshUserInfoClaimsInterval = refreshUserInfoClaimsInterval
        self.requestPreservationType = requestPreservationType
        self.requestProfile = requestProfile
        self.sameSite = sameSite
        self.scopes = scopes
        self.secureCookie = secureCookie
        self.sendRequestedUrlToProvider = sendRequestedUrlToProvider
        self.sessionTimeoutInMinutes = sessionTimeoutInMinutes
        self.validateSessionIsAlive = validateSessionIsAlive
        self.webStorageType = webStorageType

    def _validate(self) -> bool:
        return any(x for x in ["audience", "clientCredentials", "failOnUnsupportedPreservationContentType", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, WebSessionView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.audience, self.cacheUserAttributes, self.clientCredentials, self.cookieDomain, self.cookieType, self.enableRefreshUser, self.failOnUnsupportedPreservationContentType, self.httpOnlyCookie, self.idleTimeoutInMinutes, self.name, self.oidcLoginType, self.pfsessionStateCacheInSeconds, self.pkceChallengeType, self.refreshUserInfoClaimsInterval, self.requestPreservationType, self.requestProfile, self.sameSite, self.scopes, self.secureCookie, self.sendRequestedUrlToProvider, self.sessionTimeoutInMinutes, self.validateSessionIsAlive, self.webStorageType]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "audience", "cacheUserAttributes", "clientCredentials", "cookieDomain", "cookieType", "enableRefreshUser", "failOnUnsupportedPreservationContentType", "httpOnlyCookie", "idleTimeoutInMinutes", "name", "oidcLoginType", "pfsessionStateCacheInSeconds", "pkceChallengeType", "refreshUserInfoClaimsInterval", "requestPreservationType", "requestProfile", "sameSite", "scopes", "secureCookie", "sendRequestedUrlToProvider", "sessionTimeoutInMinutes", "validateSessionIsAlive", "webStorageType"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "audience":
                    valid_data[k] = str(v)
                if k == "cacheUserAttributes":
                    valid_data[k] = bool(v)
                if k == "clientCredentials":
                    valid_data[k] = OAuthClientCredentialsView(**v) if v is not None else None
                if k == "cookieDomain":
                    valid_data[k] = str(v)
                if k == "cookieType":
                    valid_data[k] = WebSessionCookieType[v]
                if k == "enableRefreshUser":
                    valid_data[k] = bool(v)
                if k == "failOnUnsupportedPreservationContentType":
                    valid_data[k] = bool(v)
                if k == "httpOnlyCookie":
                    valid_data[k] = bool(v)
                if k == "idleTimeoutInMinutes":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "oidcLoginType":
                    valid_data[k] = OidcLoginType[v]
                if k == "pfsessionStateCacheInSeconds":
                    valid_data[k] = int(v)
                if k == "pkceChallengeType":
                    valid_data[k] = PkceChallengeTypeView[v]
                if k == "refreshUserInfoClaimsInterval":
                    valid_data[k] = int(v)
                if k == "requestPreservationType":
                    valid_data[k] = RequestPreservationType[v]
                if k == "requestProfile":
                    valid_data[k] = bool(v)
                if k == "sameSite":
                    valid_data[k] = SameSiteTypeView[v]
                if k == "scopes":
                    valid_data[k] = [str(x) for x in v]
                if k == "secureCookie":
                    valid_data[k] = bool(v)
                if k == "sendRequestedUrlToProvider":
                    valid_data[k] = bool(v)
                if k == "sessionTimeoutInMinutes":
                    valid_data[k] = int(v)
                if k == "validateSessionIsAlive":
                    valid_data[k] = bool(v)
                if k == "webStorageType":
                    valid_data[k] = WebStorageType[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "audience", "cacheUserAttributes", "clientCredentials", "cookieDomain", "cookieType", "enableRefreshUser", "failOnUnsupportedPreservationContentType", "httpOnlyCookie", "idleTimeoutInMinutes", "name", "oidcLoginType", "pfsessionStateCacheInSeconds", "pkceChallengeType", "refreshUserInfoClaimsInterval", "requestPreservationType", "requestProfile", "sameSite", "scopes", "secureCookie", "sendRequestedUrlToProvider", "sessionTimeoutInMinutes", "validateSessionIsAlive", "webStorageType"]:
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
