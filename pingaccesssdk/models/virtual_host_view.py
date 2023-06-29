from pingaccesssdk.model import Model
from enum import Enum


class VirtualHostView(Model):
    """A virtual host.

    Attributes
    ----------
    id: int
        When creating a new VirtualHost, this is the ID for the VirtualHost. If not specified, an ID will be automatically assigned. When updating an existing VirtualHost, this field is ignored and the ID is determined by the path parameter.

    agentResourceCacheTTL: int
        (sortable) Indicates the number of seconds the Agent can cache resources for this application.

    host: str
        (sortable) The host name for the Virtual Host.

    keyPairId: int
        Key pair assigned to Virtual Host used by SNI, If no key pair is assigned to a virtual host, ENGINE HTTPS Listener key pair will be used.

    port: int
        (sortable) The integer port number for the Virtual Host.

    trustedCertificateGroupId: int
        Trusted Certificate Group assigned to Virtual Host for client certificate authentication.

    """

    def __init__(self, host: str, port: int, id: int = None, agentResourceCacheTTL: int = None, keyPairId: int = None, trustedCertificateGroupId: int = None) -> None:
        self.id = id
        self.agentResourceCacheTTL = agentResourceCacheTTL
        self.host = host
        self.keyPairId = keyPairId
        self.port = port
        self.trustedCertificateGroupId = trustedCertificateGroupId

    def _validate(self) -> bool:
        return any(x for x in ["host", "port"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, VirtualHostView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.agentResourceCacheTTL, self.host, self.keyPairId, self.port, self.trustedCertificateGroupId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "agentResourceCacheTTL", "host", "keyPairId", "port", "trustedCertificateGroupId"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "agentResourceCacheTTL":
                    valid_data[k] = int(v)
                if k == "host":
                    valid_data[k] = str(v)
                if k == "keyPairId":
                    valid_data[k] = int(v)
                if k == "port":
                    valid_data[k] = int(v)
                if k == "trustedCertificateGroupId":
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
            if k in ["id", "agentResourceCacheTTL", "host", "keyPairId", "port", "trustedCertificateGroupId"]:
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
