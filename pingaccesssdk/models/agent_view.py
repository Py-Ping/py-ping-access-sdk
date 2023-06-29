from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.ip_multi_value_source_view import IpMultiValueSourceView
from pingaccesssdk.models.hash import Hash
from pingaccesssdk.enums import UnknownResourceMode


class AgentView(Model):
    """An agent.

    Attributes
    ----------
    id: int
        When creating a new Agent, this is the ID for the Agent. If not specified, an ID will be automatically assigned. When updating an existing Agent, this field is ignored and the ID is determined by the path parameter.

    certificateHash: Hash
        The certificate hash.

    description: str
        (sortable) A description of the agent.

    failedRetryTimeout: int
        The number of seconds to wait before an agent should retry an unavailable policy server.

    failoverHosts: list
        A list of hostname:port strings for the backup PingAccess policy servers.

    hostname: str
        (sortable) The hostname where the agent is listening.

    ipSource: IpMultiValueSourceView
        Overrides the default IP source settings.

    maxRetries: int
        The max number of times an agent request will be attempted before failing over to a backup policy server and marking the current policy server as unavailable.

    name: str
        (sortable) The name of the agent.

    overrideIpSource: bool
        (sortable) Indicates whether the default IP source is overridden for this agent.

    port: int
        (sortable) The port the agent is listening on.

    selectedCertificateId: int
        The ID of the certificate the agent will use to contact PingAccess via SSL/TLS.

    sharedSecretIds: list
        An array of shared secret ids associated with this agent.

    unknownResourceMode: UnknownResourceMode
        Specifies how requests for unknown resources should be handled. This mode is optional. If not set, the default agent mode will be used.

    """

    def __init__(self, hostname: str, name: str, port: int, sharedSecretIds: list, id: int = None, certificateHash: Hash = None, description: str = None, failedRetryTimeout: int = None, failoverHosts: list = None, ipSource: IpMultiValueSourceView = None, maxRetries: int = None, overrideIpSource: bool = None, selectedCertificateId: int = None, unknownResourceMode: UnknownResourceMode = None) -> None:
        self.id = id
        self.certificateHash = certificateHash
        self.description = description
        self.failedRetryTimeout = failedRetryTimeout
        self.failoverHosts = failoverHosts
        self.hostname = hostname
        self.ipSource = ipSource
        self.maxRetries = maxRetries
        self.name = name
        self.overrideIpSource = overrideIpSource
        self.port = port
        self.selectedCertificateId = selectedCertificateId
        self.sharedSecretIds = sharedSecretIds
        self.unknownResourceMode = unknownResourceMode

    def _validate(self) -> bool:
        return any(x for x in ["hostname", "name", "port", "sharedSecretIds"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AgentView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.certificateHash, self.description, self.failedRetryTimeout, self.failoverHosts, self.hostname, self.ipSource, self.maxRetries, self.name, self.overrideIpSource, self.port, self.selectedCertificateId, self.sharedSecretIds, self.unknownResourceMode]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "certificateHash", "description", "failedRetryTimeout", "failoverHosts", "hostname", "ipSource", "maxRetries", "name", "overrideIpSource", "port", "selectedCertificateId", "sharedSecretIds", "unknownResourceMode"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "certificateHash":
                    valid_data[k] = Hash(**v) if v is not None else None
                if k == "description":
                    valid_data[k] = str(v)
                if k == "failedRetryTimeout":
                    valid_data[k] = int(v)
                if k == "failoverHosts":
                    valid_data[k] = [str(x) for x in v]
                if k == "hostname":
                    valid_data[k] = str(v)
                if k == "ipSource":
                    valid_data[k] = IpMultiValueSourceView(**v) if v is not None else None
                if k == "maxRetries":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "overrideIpSource":
                    valid_data[k] = bool(v)
                if k == "port":
                    valid_data[k] = int(v)
                if k == "selectedCertificateId":
                    valid_data[k] = int(v)
                if k == "sharedSecretIds":
                    valid_data[k] = [int(x) for x in v]
                if k == "unknownResourceMode":
                    valid_data[k] = UnknownResourceMode[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "certificateHash", "description", "failedRetryTimeout", "failoverHosts", "hostname", "ipSource", "maxRetries", "name", "overrideIpSource", "port", "selectedCertificateId", "sharedSecretIds", "unknownResourceMode"]:
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
