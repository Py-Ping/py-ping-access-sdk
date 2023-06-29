from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.config_statuses_view import ConfigStatusesView
from pingaccesssdk.enums import AdminAccessControlDirective
from pingaccesssdk.enums import Role


class SessionInfo(Model):
    """A session.

    Attributes
    ----------
    accessControlDirectives: set
        The set of access control directives.

    configurationExports: ConfigStatusesView
        The configuration export workflows.

    configurationImports: ConfigStatusesView
        The configuration import workflows.

    exp: int
        Time at which session will expire due to inactivity.

    expWarn: int
        Length of time before a timeout at which warning should appear.

    fipsMode: bool
        Indicates whether FIPS mode is enabled or not.

    flash: str
        The Warning message.

    iat: int
        Time at which session was created.

    maxFileUploadSize: int
        The maximum file upload size in bytes.

    pollIntervalSeconds: int
        Session poll interval configuration in seconds.

    roles: set
        The user's roles.

    sesTimeout: int
        Maximum length of time that a session is allowed to live, regardless of user activity, -1 indicates disabled.

    showWarning: bool
        Indicates that a warning needs to be shown or not.

    sniEnabled: bool
        Indicates that SNI is enabled or not.

    sub: str
        The Session's subject.

    useSlo: bool
        Indicates whether single log out (SLO) is enabled or not.

    """

    def __init__(self, accessControlDirectives: set, configurationExports: ConfigStatusesView, configurationImports: ConfigStatusesView, exp: int, expWarn: int, fipsMode: bool, flash: str, iat: int, maxFileUploadSize: int, pollIntervalSeconds: int, roles: set, sesTimeout: int, showWarning: bool, sniEnabled: bool, sub: str, useSlo: bool) -> None:
        self.accessControlDirectives = accessControlDirectives
        self.configurationExports = configurationExports
        self.configurationImports = configurationImports
        self.exp = exp
        self.expWarn = expWarn
        self.fipsMode = fipsMode
        self.flash = flash
        self.iat = iat
        self.maxFileUploadSize = maxFileUploadSize
        self.pollIntervalSeconds = pollIntervalSeconds
        self.roles = roles
        self.sesTimeout = sesTimeout
        self.showWarning = showWarning
        self.sniEnabled = sniEnabled
        self.sub = sub
        self.useSlo = useSlo

    def _validate(self) -> bool:
        return any(x for x in ["accessControlDirectives", "configurationExports", "configurationImports", "exp", "expWarn", "fipsMode", "flash", "iat", "maxFileUploadSize", "pollIntervalSeconds", "roles", "sesTimeout", "showWarning", "sniEnabled", "sub", "useSlo"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SessionInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.accessControlDirectives, self.configurationExports, self.configurationImports, self.exp, self.expWarn, self.fipsMode, self.flash, self.iat, self.maxFileUploadSize, self.pollIntervalSeconds, self.roles, self.sesTimeout, self.showWarning, self.sniEnabled, self.sub, self.useSlo]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["accessControlDirectives", "configurationExports", "configurationImports", "exp", "expWarn", "fipsMode", "flash", "iat", "maxFileUploadSize", "pollIntervalSeconds", "roles", "sesTimeout", "showWarning", "sniEnabled", "sub", "useSlo"]:
                if k == "accessControlDirectives":
                    valid_data[k] = set({AdminAccessControlDirective[x] for x in v})
                if k == "configurationExports":
                    valid_data[k] = ConfigStatusesView(**v) if v is not None else None
                if k == "configurationImports":
                    valid_data[k] = ConfigStatusesView(**v) if v is not None else None
                if k == "exp":
                    valid_data[k] = int(v)
                if k == "expWarn":
                    valid_data[k] = int(v)
                if k == "fipsMode":
                    valid_data[k] = bool(v)
                if k == "flash":
                    valid_data[k] = str(v)
                if k == "iat":
                    valid_data[k] = int(v)
                if k == "maxFileUploadSize":
                    valid_data[k] = int(v)
                if k == "pollIntervalSeconds":
                    valid_data[k] = int(v)
                if k == "roles":
                    valid_data[k] = set({Role[x] for x in v})
                if k == "sesTimeout":
                    valid_data[k] = int(v)
                if k == "showWarning":
                    valid_data[k] = bool(v)
                if k == "sniEnabled":
                    valid_data[k] = bool(v)
                if k == "sub":
                    valid_data[k] = str(v)
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
            if k in ["accessControlDirectives", "configurationExports", "configurationImports", "exp", "expWarn", "fipsMode", "flash", "iat", "maxFileUploadSize", "pollIntervalSeconds", "roles", "sesTimeout", "showWarning", "sniEnabled", "sub", "useSlo"]:
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
