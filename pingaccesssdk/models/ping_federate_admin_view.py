from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_auth_authentication_configuration_view import OAuthAuthenticationConfigurationView
from pingaccesssdk.models.hidden_field_view import HiddenFieldView
from pingaccesssdk.enums import AuthenticationType


class PingFederateAdminView(Model):
    """A PingFederate Admin configuration.

    Attributes
    ----------
    adminPassword: HiddenFieldView
        The password for the administrator username. Required when the authentication type is set to 'Basic'.

    adminUsername: str
        The administrator username. Required when the authentication type is set to 'Basic'.

    auditLevel: str
        ['ON' or 'OFF']: Enable to record requests to the PingFederate Administrative API to the audit store.

    authenticationType: AuthenticationType
        Specify the authentication type for a PingFederate Admin node. Default value is 'Basic'. When not set, this field will be treated as having a value of 'Basic'. 'Cookie' type authentication is not supported at the moment.

    basePath: str
        The base path, if needed, for Administration API.

    expectedHostname: str
        The name of the host expected in the certificate used by PingFederate.

    host: str
        The host name or IP address for PingFederate Administration API.

    oAuthAuthenticationConfig: OAuthAuthenticationConfigurationView
    port: int
        The port number for PingFederate Administration API.

    secure: bool
        Enable if PingFederate is expecting HTTPS connections.

    skipHostnameVerification: bool
        Set to true if HTTP communications to PingFederate should not perform hostname verification of the certificate.

    trustedCertificateGroupId: int
        The group of certificates to use when authenticating to PingFederate Administrative API.

    useProxy: bool
        True if a proxy should be used for HTTP or HTTPS requests.

    """

    def __init__(self, adminPassword: HiddenFieldView, host: str, port: int, adminUsername: str = None, auditLevel: str = None, authenticationType: AuthenticationType = None, basePath: str = None, expectedHostname: str = None, oAuthAuthenticationConfig: OAuthAuthenticationConfigurationView = None, secure: bool = None, skipHostnameVerification: bool = None, trustedCertificateGroupId: int = None, useProxy: bool = None) -> None:
        self.adminPassword = adminPassword
        self.adminUsername = adminUsername
        self.auditLevel = auditLevel
        self.authenticationType = authenticationType
        self.basePath = basePath
        self.expectedHostname = expectedHostname
        self.host = host
        self.oAuthAuthenticationConfig = oAuthAuthenticationConfig
        self.port = port
        self.secure = secure
        self.skipHostnameVerification = skipHostnameVerification
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy

    def _validate(self) -> bool:
        return any(x for x in ["adminPassword", "host", "port"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingFederateAdminView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.adminPassword, self.adminUsername, self.auditLevel, self.authenticationType, self.basePath, self.expectedHostname, self.host, self.oAuthAuthenticationConfig, self.port, self.secure, self.skipHostnameVerification, self.trustedCertificateGroupId, self.useProxy]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["adminPassword", "adminUsername", "auditLevel", "authenticationType", "basePath", "expectedHostname", "host", "oAuthAuthenticationConfig", "port", "secure", "skipHostnameVerification", "trustedCertificateGroupId", "useProxy"]:
                if k == "adminPassword":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None
                if k == "adminUsername":
                    valid_data[k] = str(v)
                if k == "auditLevel":
                    valid_data[k] = str(v)
                if k == "authenticationType":
                    valid_data[k] = AuthenticationType[v]
                if k == "basePath":
                    valid_data[k] = str(v)
                if k == "expectedHostname":
                    valid_data[k] = str(v)
                if k == "host":
                    valid_data[k] = str(v)
                if k == "oAuthAuthenticationConfig":
                    valid_data[k] = OAuthAuthenticationConfigurationView(**v) if v is not None else None
                if k == "port":
                    valid_data[k] = int(v)
                if k == "secure":
                    valid_data[k] = bool(v)
                if k == "skipHostnameVerification":
                    valid_data[k] = bool(v)
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
            if k in ["adminPassword", "adminUsername", "auditLevel", "authenticationType", "basePath", "expectedHostname", "host", "oAuthAuthenticationConfig", "port", "secure", "skipHostnameVerification", "trustedCertificateGroupId", "useProxy"]:
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
