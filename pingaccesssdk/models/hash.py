from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.enums import HashAlgorithm


class Hash(Model):
    """

    Attributes
    ----------
    algorithm: HashAlgorithm
    hexValue: str
    """

    def __init__(self, algorithm: HashAlgorithm, hexValue: str) -> None:
        self.algorithm = algorithm
        self.hexValue = hexValue

    def _validate(self) -> bool:
        return any(x for x in ["algorithm", "hexValue"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, Hash):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.algorithm, self.hexValue]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["algorithm", "hexValue"]:
                if k == "algorithm":
                    valid_data[k] = HashAlgorithm[v]
                if k == "hexValue":
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
            if k in ["algorithm", "hexValue"]:
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