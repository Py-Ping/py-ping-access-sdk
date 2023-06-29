from pingaccesssdk.model import Model
from enum import Enum


class HsmProviderView(Model):
    """An HSM provider.

    Attributes
    ----------
    id: int
        When creating a new HsmProvider, this is the ID for the HsmProvider. If not specified, an ID will be automatically assigned. When updating an existing HsmProvider, this field is ignored and the ID is determined by the path parameter.

    className: str
        (sortable) The HSM provider's class name.

    configuration: dict
        The HSM provider's configuration data.

    name: str
        (sortable) The HSM provider's name.

    """

    def __init__(self, className: str, configuration: dict, name: str, id: int = None) -> None:
        self.id = id
        self.className = className
        self.configuration = configuration
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in ["className", "configuration", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, HsmProviderView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.className, self.configuration, self.name]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "className", "configuration", "name"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "className":
                    valid_data[k] = str(v)
                if k == "configuration":
                    valid_data[k] = {str(x): y for x, y in v.items()}
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
            if k in ["id", "className", "configuration", "name"]:
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
