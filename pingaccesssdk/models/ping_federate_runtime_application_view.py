from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.policy_item import PolicyItem


class PingFederateRuntimeApplicationView(Model):
    """Configuration required to help define application data to handle PingFederate as both a token provider and a proxied application.

    Attributes
    ----------
    additionalVirtualHostIds: list
        Additional virtual host IDs that can be used to proxy the PingFederate runtime application.

    caseSensitive: bool
        True if the context root is case sensitive.

    clientCertHeaderNames: list
        The header names to contain PEM-encoded client certificates. The list position correlates to the index in the client certificate chain. For example, the first element always maps to the leaf certificate.

    contextRoot: str
        The base path of the PingFederate runtime application. Default value is '/'.

    policy: list
        A List of PolicyItems associated with the PingFederate runtime application.

    primaryVirtualHostId: int
        The ID of the primary virtual host to use for front channel requests to the PA proxied PingFederate runtime application. This virtual host will be used for the default OpenID Connect Issuer when an application specific issuer is not configured.

    """

    def __init__(self, primaryVirtualHostId: int, additionalVirtualHostIds: list = None, caseSensitive: bool = None, clientCertHeaderNames: list = None, contextRoot: str = None, policy: list = None) -> None:
        self.additionalVirtualHostIds = additionalVirtualHostIds
        self.caseSensitive = caseSensitive
        self.clientCertHeaderNames = clientCertHeaderNames
        self.contextRoot = contextRoot
        self.policy = policy
        self.primaryVirtualHostId = primaryVirtualHostId

    def _validate(self) -> bool:
        return any(x for x in ["primaryVirtualHostId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingFederateRuntimeApplicationView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.additionalVirtualHostIds, self.caseSensitive, self.clientCertHeaderNames, self.contextRoot, self.policy, self.primaryVirtualHostId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["additionalVirtualHostIds", "caseSensitive", "clientCertHeaderNames", "contextRoot", "policy", "primaryVirtualHostId"]:
                if k == "additionalVirtualHostIds":
                    valid_data[k] = [int(x) for x in v]
                if k == "caseSensitive":
                    valid_data[k] = bool(v)
                if k == "clientCertHeaderNames":
                    valid_data[k] = [str(x) for x in v]
                if k == "contextRoot":
                    valid_data[k] = str(v)
                if k == "policy":
                    valid_data[k] = [PolicyItem(**x) if x is not None else None for x in v or []]
                if k == "primaryVirtualHostId":
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
            if k in ["additionalVirtualHostIds", "caseSensitive", "clientCertHeaderNames", "contextRoot", "policy", "primaryVirtualHostId"]:
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
