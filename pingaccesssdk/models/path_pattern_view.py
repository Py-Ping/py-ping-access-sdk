from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.enums import PathPatternType


class PathPatternView(Model):
    """A pattern for matching request URI paths.

    Attributes
    ----------
    pattern: str
        The path-matching pattern, relative to the Application context root (interpreted according to the pattern 'type').

    type: PathPatternType
        The pattern syntax type.

    """

    def __init__(self, pattern: str, type: PathPatternType) -> None:
        self.pattern = pattern
        self.type = type

    def _validate(self) -> bool:
        return any(x for x in ["pattern", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PathPatternView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.pattern, self.type]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["pattern", "type"]:
                if k == "pattern":
                    valid_data[k] = str(v)
                if k == "type":
                    valid_data[k] = PathPatternType[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["pattern", "type"]:
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