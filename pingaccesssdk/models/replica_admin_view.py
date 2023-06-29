from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.hash import Hash
from pingaccesssdk.models.public_key_view import PublicKeyView


class ReplicaAdminView(Model):
    """A replica admin.

    Attributes
    ----------
    certificateHash: Hash
        The certificate hash.

    configReplicationEnabled: bool
        Set to true when configuration replication for the replica admin is enabled. False when configuration replication is suspended.

    description: str
        The description of the replica admin.

    hostPort: str
        The host and port of the replica admin.

    httpProxyId: int
        The ID of the proxy to use for HTTP requests or zero if none.

    httpsProxyId: int
        The ID of the proxy to use for HTTPS requests or zero if none.

    keys: list
        An array of public keys associated with the replica admin.

    name: str
        The name of the replica admin.

    selectedCertificateId: int
        The ID of the certificate the replica admin will use to contact PingAccess via SSL/TLS.

    """

    def __init__(self, hostPort: str, name: str, certificateHash: Hash = None, configReplicationEnabled: bool = None, description: str = None, httpProxyId: int = None, httpsProxyId: int = None, keys: list = None, selectedCertificateId: int = None) -> None:
        self.certificateHash = certificateHash
        self.configReplicationEnabled = configReplicationEnabled
        self.description = description
        self.hostPort = hostPort
        self.httpProxyId = httpProxyId
        self.httpsProxyId = httpsProxyId
        self.keys = keys
        self.name = name
        self.selectedCertificateId = selectedCertificateId

    def _validate(self) -> bool:
        return any(x for x in ["hostPort", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ReplicaAdminView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.certificateHash, self.configReplicationEnabled, self.description, self.hostPort, self.httpProxyId, self.httpsProxyId, self.keys, self.name, self.selectedCertificateId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["certificateHash", "configReplicationEnabled", "description", "hostPort", "httpProxyId", "httpsProxyId", "keys", "name", "selectedCertificateId"]:
                if k == "certificateHash":
                    valid_data[k] = Hash(**v) if v is not None else None
                if k == "configReplicationEnabled":
                    valid_data[k] = bool(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "hostPort":
                    valid_data[k] = str(v)
                if k == "httpProxyId":
                    valid_data[k] = int(v)
                if k == "httpsProxyId":
                    valid_data[k] = int(v)
                if k == "keys":
                    valid_data[k] = [PublicKeyView(**x) if x is not None else None for x in v or []]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "selectedCertificateId":
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
            if k in ["certificateHash", "configReplicationEnabled", "description", "hostPort", "httpProxyId", "httpsProxyId", "keys", "name", "selectedCertificateId"]:
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
