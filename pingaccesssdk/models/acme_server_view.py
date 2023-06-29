from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.link_view import LinkView


class AcmeServerView(Model):
    """An ACME server.

    Attributes
    ----------
    id: str
        When creating a new AcmeServer, this is the ID for the AcmeServer. If not specified, an ID will be automatically assigned. When updating an existing AcmeServer, this field is ignored and the ID is determined by the path parameter.

    acmeAccounts: list
        An array of references to accounts. This array is read-only.

    name: str
        (sortable) A user-friendly name for the ACME server.

    url: str
        The URL of the ACME directory resource on the ACME server.

    """

    def __init__(self, name: str, url: str, id: str = None, acmeAccounts: list = None) -> None:
        self.id = id
        self.acmeAccounts = acmeAccounts
        self.name = name
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in ["name", "url"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AcmeServerView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.acmeAccounts, self.name, self.url]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "acmeAccounts", "name", "url"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "acmeAccounts":
                    valid_data[k] = [LinkView(**x) if x is not None else None for x in v or []]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "url":
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
            if k in ["id", "acmeAccounts", "name", "url"]:
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
