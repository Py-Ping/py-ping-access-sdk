from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.sideband_client_credentials_view import SidebandClientCredentialsView


class SidebandClientView(Model):
    """A sideband client.

    Attributes
    ----------
    id: str
        When creating a new SidebandClient, this is the ID for the SidebandClient. If not specified, an ID will be automatically assigned. When updating an existing SidebandClient, this field is ignored and the ID is determined by the path parameter.

    clientCredentials: list
        The authentication configuration for the sideband client.

    description: str
        (sortable) Description of the sideband client.

    name: str
        (sortable) Name of the sideband client.

    """

    def __init__(self, clientCredentials: list, name: str, id: str = None, description: str = None) -> None:
        self.id = id
        self.clientCredentials = clientCredentials
        self.description = description
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in ["clientCredentials", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SidebandClientView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.clientCredentials, self.description, self.name]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "clientCredentials", "description", "name"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "clientCredentials":
                    valid_data[k] = [SidebandClientCredentialsView(**x) if x is not None else None for x in v or []]
                if k == "description":
                    valid_data[k] = str(v)
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
            if k in ["id", "clientCredentials", "description", "name"]:
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
