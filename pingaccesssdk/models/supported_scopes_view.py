from pingaccesssdk.model import Model
from enum import Enum


class SupportedScopesView(Model):
    """A set of scopes supported by the OIDC Provider.

    Attributes
    ----------
    clientId: str
        The ID of the client that the scopes are associated with. If not specified, the list of scopes represents all scopes supported by the provider.

    scopes: list
        The list of supported scopes (excluding 'openid').

    """

    def __init__(self, clientId: str, scopes: list) -> None:
        self.clientId = clientId
        self.scopes = scopes

    def _validate(self) -> bool:
        return any(x for x in ["clientId", "scopes"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SupportedScopesView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.clientId, self.scopes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["clientId", "scopes"]:
                if k == "clientId":
                    valid_data[k] = str(v)
                if k == "scopes":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["clientId", "scopes"]:
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
