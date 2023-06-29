from pingaccesssdk.model import Model
from enum import Enum


class SiteView(Model):
    """A site.

    Attributes
    ----------
    id: int
        When creating a new Site, this is the ID for the Site. If not specified, an ID will be automatically assigned. When updating an existing Site, this field is ignored and the ID is determined by the path parameter.

    availabilityProfileId: int
        The ID of the availability profile associated with the site.

    expectedHostname: str
        (sortable) The name of the host expected in the site's certificate.

    keepAliveTimeout: int
        (sortable) The time, in milliseconds, that an HTTP persistent connection to the site can be idle before PingAccess closes the connection.

    loadBalancingStrategyId: int
        The ID of the load balancing strategy associated with the site.

    maxConnections: int
        (sortable) The maximum number of HTTP persistent connections you want PingAccess to have open and maintain for the site. -1 indicates unlimited connections.

    maxWebSocketConnections: int
        (sortable) The maximum number of WebSocket connections you want PingAccess to have open and maintain for the site. -1 indicates unlimited connections.

    name: str
        (sortable) The name of the site.

    secure: bool
        (sortable) This field is true if the site expects HTTPS connections.

    sendPaCookie: bool
        (sortable) This field is true if the PingAccess Token or OAuth Access Token should be included in the request to the site.

    siteAuthenticatorIds: list
        The IDs of the site authenticators associated with the site.

    skipHostnameVerification: bool
        (sortable) This field is true if the hostname verification of the site's certificate should be skipped.

    targets: list
        The {hostname}:{port} pairs for the hosts that make up the site.

    trustedCertificateGroupId: int
        The ID of the trusted certificate group associated with the site.

    useProxy: bool
        (sortable) True if a proxy should be used for HTTP or HTTPS requests.

    useTargetHostHeader: bool
        (sortable) Setting this field to true causes PingAccess to adjust the Host header to the site's selected target host rather than the virtual host configured in the application.

    """

    def __init__(self, name: str, targets: list, id: int = None, availabilityProfileId: int = None, expectedHostname: str = None, keepAliveTimeout: int = None, loadBalancingStrategyId: int = None, maxConnections: int = None, maxWebSocketConnections: int = None, secure: bool = None, sendPaCookie: bool = None, siteAuthenticatorIds: list = None, skipHostnameVerification: bool = None, trustedCertificateGroupId: int = None, useProxy: bool = None, useTargetHostHeader: bool = None) -> None:
        self.id = id
        self.availabilityProfileId = availabilityProfileId
        self.expectedHostname = expectedHostname
        self.keepAliveTimeout = keepAliveTimeout
        self.loadBalancingStrategyId = loadBalancingStrategyId
        self.maxConnections = maxConnections
        self.maxWebSocketConnections = maxWebSocketConnections
        self.name = name
        self.secure = secure
        self.sendPaCookie = sendPaCookie
        self.siteAuthenticatorIds = siteAuthenticatorIds
        self.skipHostnameVerification = skipHostnameVerification
        self.targets = targets
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy
        self.useTargetHostHeader = useTargetHostHeader

    def _validate(self) -> bool:
        return any(x for x in ["name", "targets"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SiteView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.availabilityProfileId, self.expectedHostname, self.keepAliveTimeout, self.loadBalancingStrategyId, self.maxConnections, self.maxWebSocketConnections, self.name, self.secure, self.sendPaCookie, self.siteAuthenticatorIds, self.skipHostnameVerification, self.targets, self.trustedCertificateGroupId, self.useProxy, self.useTargetHostHeader]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "availabilityProfileId", "expectedHostname", "keepAliveTimeout", "loadBalancingStrategyId", "maxConnections", "maxWebSocketConnections", "name", "secure", "sendPaCookie", "siteAuthenticatorIds", "skipHostnameVerification", "targets", "trustedCertificateGroupId", "useProxy", "useTargetHostHeader"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "availabilityProfileId":
                    valid_data[k] = int(v)
                if k == "expectedHostname":
                    valid_data[k] = str(v)
                if k == "keepAliveTimeout":
                    valid_data[k] = int(v)
                if k == "loadBalancingStrategyId":
                    valid_data[k] = int(v)
                if k == "maxConnections":
                    valid_data[k] = int(v)
                if k == "maxWebSocketConnections":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "secure":
                    valid_data[k] = bool(v)
                if k == "sendPaCookie":
                    valid_data[k] = bool(v)
                if k == "siteAuthenticatorIds":
                    valid_data[k] = [int(x) for x in v]
                if k == "skipHostnameVerification":
                    valid_data[k] = bool(v)
                if k == "targets":
                    valid_data[k] = [str(x) for x in v]
                if k == "trustedCertificateGroupId":
                    valid_data[k] = int(v)
                if k == "useProxy":
                    valid_data[k] = bool(v)
                if k == "useTargetHostHeader":
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
            if k in ["id", "availabilityProfileId", "expectedHostname", "keepAliveTimeout", "loadBalancingStrategyId", "maxConnections", "maxWebSocketConnections", "name", "secure", "sendPaCookie", "siteAuthenticatorIds", "skipHostnameVerification", "targets", "trustedCertificateGroupId", "useProxy", "useTargetHostHeader"]:
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
