from pingaccesssdk.model import Model
from enum import Enum


class ThirdPartyServiceView(Model):
    """A third-party service.

    Attributes
    ----------
    id: str
        When creating a new ThirdPartyService, this is the ID for the ThirdPartyService. If not specified, an ID will be automatically assigned. When updating an existing ThirdPartyService, this field is ignored and the ID is determined by the path parameter.

    availabilityProfileId: int
        The ID of the availability profile associated with the third-party service.

    expectedHostname: str
        (sortable) The name of the host expected in the third-party service's certificate.

    hostValue: str
        (sortable) The Host header field value in the requests sent to a Third-Party Services. When set, PingAccess will use the hostValue as the Host header field value. Otherwise, the target value will be used.

    loadBalancingStrategyId: int
        The ID of the load balancing strategy associated with the third-party service.

    maxConnections: int
        (sortable) The maximum number of HTTP persistent connections you want PingAccess to have open and maintain for the third-party service. -1 indicates unlimited connections.

    name: str
        (sortable) The name of the third-party service.

    secure: bool
        (sortable) This field is true if the third-party service expects HTTPS connections.

    skipHostnameVerification: bool
        (sortable) This field is true if the hostname verification of the third-party service's certificate should be skipped.

    targets: list
        The {hostname}:{port} pairs for the hosts that make up the third-party service.

    trustedCertificateGroupId: int
        The ID of the trusted certificate group associated with the third-party service.

    useProxy: bool
        (sortable) True if a proxy should be used for HTTP or HTTPS requests.

    """

    def __init__(self, name: str, targets: list, id: str = None, availabilityProfileId: int = None, expectedHostname: str = None, hostValue: str = None, loadBalancingStrategyId: int = None, maxConnections: int = None, secure: bool = None, skipHostnameVerification: bool = None, trustedCertificateGroupId: int = None, useProxy: bool = None) -> None:
        self.id = id
        self.availabilityProfileId = availabilityProfileId
        self.expectedHostname = expectedHostname
        self.hostValue = hostValue
        self.loadBalancingStrategyId = loadBalancingStrategyId
        self.maxConnections = maxConnections
        self.name = name
        self.secure = secure
        self.skipHostnameVerification = skipHostnameVerification
        self.targets = targets
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy

    def _validate(self) -> bool:
        return any(x for x in ["name", "targets"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ThirdPartyServiceView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.availabilityProfileId, self.expectedHostname, self.hostValue, self.loadBalancingStrategyId, self.maxConnections, self.name, self.secure, self.skipHostnameVerification, self.targets, self.trustedCertificateGroupId, self.useProxy]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "availabilityProfileId", "expectedHostname", "hostValue", "loadBalancingStrategyId", "maxConnections", "name", "secure", "skipHostnameVerification", "targets", "trustedCertificateGroupId", "useProxy"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "availabilityProfileId":
                    valid_data[k] = int(v)
                if k == "expectedHostname":
                    valid_data[k] = str(v)
                if k == "hostValue":
                    valid_data[k] = str(v)
                if k == "loadBalancingStrategyId":
                    valid_data[k] = int(v)
                if k == "maxConnections":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
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

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "availabilityProfileId", "expectedHostname", "hostValue", "loadBalancingStrategyId", "maxConnections", "name", "secure", "skipHostnameVerification", "targets", "trustedCertificateGroupId", "useProxy"]:
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
