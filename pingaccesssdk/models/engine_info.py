from pingaccesssdk.model import Model
from enum import Enum


class EngineInfo(Model):
    """

    Attributes
    ----------
    description: str
    lastUpdated: int
    name: str
    pollingDelay: int
    """

    def __init__(self, description: str, lastUpdated: int, name: str, pollingDelay: int) -> None:
        self.description = description
        self.lastUpdated = lastUpdated
        self.name = name
        self.pollingDelay = pollingDelay

    def _validate(self) -> bool:
        return any(x for x in ["description", "lastUpdated", "name", "pollingDelay"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, EngineInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.description, self.lastUpdated, self.name, self.pollingDelay]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["description", "lastUpdated", "name", "pollingDelay"]:
                if k == "description":
                    valid_data[k] = str(v)
                if k == "lastUpdated":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "pollingDelay":
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
            if k in ["description", "lastUpdated", "name", "pollingDelay"]:
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
