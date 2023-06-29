from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.link_view import LinkView
from pingaccesssdk.enums import EntryType
from pingaccesssdk.enums import PathPatternType


class ResourceMatchingEntryView(Model):
    """A resource matching entry.

    Attributes
    ----------
    link: LinkView
        A link to the associated resource.

    methods: set
        A set of HTTP methods configured for the resource, or '*' to indicate any method.

    name: str
        The name of the associated resource.

    pattern: str
        A path-matching pattern, relative to the Application context root (interpreted according to the pattern 'type').

    patternType: PathPatternType
        The pattern syntax type.

    type: EntryType
        The enumerated type of the associated resource.

    """

    def __init__(self, link: LinkView, methods: set, name: str, pattern: str, patternType: PathPatternType, type: EntryType) -> None:
        self.link = link
        self.methods = methods
        self.name = name
        self.pattern = pattern
        self.patternType = patternType
        self.type = type

    def _validate(self) -> bool:
        return any(x for x in ["link", "methods", "name", "pattern", "patternType", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ResourceMatchingEntryView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.link, self.methods, self.name, self.pattern, self.patternType, self.type]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["link", "methods", "name", "pattern", "patternType", "type"]:
                if k == "link":
                    valid_data[k] = LinkView(**v) if v is not None else None
                if k == "methods":
                    valid_data[k] = set({str(x) for x in v})
                if k == "name":
                    valid_data[k] = str(v)
                if k == "pattern":
                    valid_data[k] = str(v)
                if k == "patternType":
                    valid_data[k] = PathPatternType[v]
                if k == "type":
                    valid_data[k] = EntryType[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["link", "methods", "name", "pattern", "patternType", "type"]:
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
