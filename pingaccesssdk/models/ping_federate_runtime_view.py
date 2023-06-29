from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.ping_federate_runtime_application_view import PingFederateRuntimeApplicationView


class PingFederateRuntimeView(Model):
    """A PingFederate configuration.

    Attributes
    ----------
    application: PingFederateRuntimeApplicationView
        Application configuration for the PingFederate runtime application proxied by PingAccess.

    auditLevel: str
        ['ON' or 'OFF']: Enable to record requests to PingFederate to the audit store.

    availabilityProfileId: int
        The ID of the availability profile to use for the PingFederate runtime. When set to 0, an availability profile defined by the pa.default.availability.ondemand properties in run.properties will be used for back end communication to PingFederate.

    backChannelBasePath: str
        The base path, if needed, for the PingFederate Runtime accessed using a Back Channel hostname. This field is ignored when the PingFederate application is configured.

    backChannelSecure: bool
        Enable if PingFederate is expecting HTTPS connections for calls via the Back Channel hostnames.

    basePath: str
        The base path, if needed, for PingFederate Runtime. This field is ignored when the PingFederate application is configured.

    expectedHostname: str
        The name of the host expected in the certificate.

    host: str
        The host name or IP address for PingFederate Runtime. This field is ignored and can be an empty string when the PingFederate application is configured.

    loadBalancingStrategyId: int
        The ID of the load balancing strategy to use for requests to the PingFederate targets.

    port: int
        The port number for PingFederate Runtime. This field is ignored when the PingFederate application is configured.

    secure: bool
        Enable if PingFederate is expecting HTTPS connections. This field is ignored when the PingFederate application is configured. In this case, use backChannelSecure instead.

    skipHostnameVerification: bool
        Enable if the Back Channel servers should not perform hostname verification of the certificate.

    targets: list
        One or more server hostname:port pairs used to access the PingFederate server from inside a private network. Required when the PingFederate application is configured.

    trustedCertificateGroupId: int
        The group of certificates to use when authenticating to PingFederate.

    useProxy: bool
        True if a proxy should be used for HTTP or HTTPS requests.

    useSlo: bool
        Enable if OIDC single log out should be used on the /pa/oidc/logout on the engines.

    """

    def __init__(self, host: str, port: int, application: PingFederateRuntimeApplicationView = None, auditLevel: str = None, availabilityProfileId: int = None, backChannelBasePath: str = None, backChannelSecure: bool = None, basePath: str = None, expectedHostname: str = None, loadBalancingStrategyId: int = None, secure: bool = None, skipHostnameVerification: bool = None, targets: list = None, trustedCertificateGroupId: int = None, useProxy: bool = None, useSlo: bool = None) -> None:
        self.application = application
        self.auditLevel = auditLevel
        self.availabilityProfileId = availabilityProfileId
        self.backChannelBasePath = backChannelBasePath
        self.backChannelSecure = backChannelSecure
        self.basePath = basePath
        self.expectedHostname = expectedHostname
        self.host = host
        self.loadBalancingStrategyId = loadBalancingStrategyId
        self.port = port
        self.secure = secure
        self.skipHostnameVerification = skipHostnameVerification
        self.targets = targets
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy
        self.useSlo = useSlo

    def _validate(self) -> bool:
        return any(x for x in ["host", "port"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingFederateRuntimeView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.application, self.auditLevel, self.availabilityProfileId, self.backChannelBasePath, self.backChannelSecure, self.basePath, self.expectedHostname, self.host, self.loadBalancingStrategyId, self.port, self.secure, self.skipHostnameVerification, self.targets, self.trustedCertificateGroupId, self.useProxy, self.useSlo]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["application", "auditLevel", "availabilityProfileId", "backChannelBasePath", "backChannelSecure", "basePath", "expectedHostname", "host", "loadBalancingStrategyId", "port", "secure", "skipHostnameVerification", "targets", "trustedCertificateGroupId", "useProxy", "useSlo"]:
                if k == "application":
                    valid_data[k] = PingFederateRuntimeApplicationView(**v) if v is not None else None
                if k == "auditLevel":
                    valid_data[k] = str(v)
                if k == "availabilityProfileId":
                    valid_data[k] = int(v)
                if k == "backChannelBasePath":
                    valid_data[k] = str(v)
                if k == "backChannelSecure":
                    valid_data[k] = bool(v)
                if k == "basePath":
                    valid_data[k] = str(v)
                if k == "expectedHostname":
                    valid_data[k] = str(v)
                if k == "host":
                    valid_data[k] = str(v)
                if k == "loadBalancingStrategyId":
                    valid_data[k] = int(v)
                if k == "port":
                    valid_data[k] = int(v)
                if k == "secure":
                    valid_data[k] = bool(v)
                if k == "skipHostnameVerification":
                    valid_data[k] = bool(v)
                if k == "targets":
                    valid_data[k] = [str(x) for x in v]
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
            if k in ["application", "auditLevel", "availabilityProfileId", "backChannelBasePath", "backChannelSecure", "basePath", "expectedHostname", "host", "loadBalancingStrategyId", "port", "secure", "skipHostnameVerification", "targets", "trustedCertificateGroupId", "useProxy", "useSlo"]:
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
