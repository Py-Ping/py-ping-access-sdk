from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.enums import WebSessionCookieType


class AdminBasicWebSessionView(Model):
    """An admin basic web session.

    Attributes
    ----------
    audience: str
        Enter a unique identifier between 1 and 32 characters that defines who the PA Admin Token is applicable to.

    cookieDomain: str
        The domain where the cookie is stored--for example, corp.yourcompany.com.

    cookieType: WebSessionCookieType
        Specify an Encrypted JWT or a Signed JWT web session cookie.

    expirationWarningInMinutes: int
        The time to have the UI display a warning before the session expires.

    idleTimeoutInMinutes: int
        The length of time you want the PingAccess Admin Token to remain active when no activity is detected.

    sessionPollIntervalInSeconds: int
        The interval between UI polling for session validity.

    sessionTimeoutInMinutes: int
        The length of time you want the PA Admin Token to remain active. Once the PA Admin Token expires, an authenticated user must re-authenticate.

    """

    def __init__(self, audience: str, cookieType: WebSessionCookieType, expirationWarningInMinutes: int, idleTimeoutInMinutes: int, sessionPollIntervalInSeconds: int, sessionTimeoutInMinutes: int, cookieDomain: str = None) -> None:
        self.audience = audience
        self.cookieDomain = cookieDomain
        self.cookieType = cookieType
        self.expirationWarningInMinutes = expirationWarningInMinutes
        self.idleTimeoutInMinutes = idleTimeoutInMinutes
        self.sessionPollIntervalInSeconds = sessionPollIntervalInSeconds
        self.sessionTimeoutInMinutes = sessionTimeoutInMinutes

    def _validate(self) -> bool:
        return any(x for x in ["audience", "cookieType", "expirationWarningInMinutes", "idleTimeoutInMinutes", "sessionPollIntervalInSeconds", "sessionTimeoutInMinutes"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AdminBasicWebSessionView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.audience, self.cookieDomain, self.cookieType, self.expirationWarningInMinutes, self.idleTimeoutInMinutes, self.sessionPollIntervalInSeconds, self.sessionTimeoutInMinutes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["audience", "cookieDomain", "cookieType", "expirationWarningInMinutes", "idleTimeoutInMinutes", "sessionPollIntervalInSeconds", "sessionTimeoutInMinutes"]:
                if k == "audience":
                    valid_data[k] = str(v)
                if k == "cookieDomain":
                    valid_data[k] = str(v)
                if k == "cookieType":
                    valid_data[k] = WebSessionCookieType[v]
                if k == "expirationWarningInMinutes":
                    valid_data[k] = int(v)
                if k == "idleTimeoutInMinutes":
                    valid_data[k] = int(v)
                if k == "sessionPollIntervalInSeconds":
                    valid_data[k] = int(v)
                if k == "sessionTimeoutInMinutes":
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
            if k in ["audience", "cookieDomain", "cookieType", "expirationWarningInMinutes", "idleTimeoutInMinutes", "sessionPollIntervalInSeconds", "sessionTimeoutInMinutes"]:
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
