from pingaccesssdk.model import Model
from enum import Enum


class AuthnReqListView(Model):
    """An authentication requirements list.

    Attributes
    ----------
    id: int
        When creating a new AuthnReqList, this is the ID for the AuthnReqList. If not specified, an ID will be automatically assigned. When updating an existing AuthnReqList, this field is ignored and the ID is determined by the path parameter.

    authnReqs: list
        The ordered list of authentication requirements, or identifiers, which define how PingFederate will authenticate a user during the OIDC login flow.

    name: str
        (sortable) The name of the authentication requirements list.

    """

    def __init__(self, authnReqs: list, name: str, id: int = None) -> None:
        self.id = id
        self.authnReqs = authnReqs
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in ["authnReqs", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnReqListView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.authnReqs, self.name]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "authnReqs", "name"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "authnReqs":
                    valid_data[k] = [str(x) for x in v]
                if k == "name":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "authnReqs", "name"]:
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
