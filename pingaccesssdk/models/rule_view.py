from pingaccesssdk.model import Model
from enum import Enum


class RuleView(Model):
    """A rule.

    Attributes
    ----------
    id: int
        When creating a new Rule, this is the ID for the Rule. If not specified, an ID will be automatically assigned. When updating an existing Rule, this field is ignored and the ID is determined by the path parameter.

    className: str
        (sortable) The rule's class name.

    configuration: dict
        The rule's configuration data.

    name: str
        (sortable) The rule's name.

    supportedDestinations: set
        The supported destinations for this rule. This field is read-only and meant to provide contextual metadata on where the rule can be applied.

    """

    def __init__(self, className: str, configuration: dict, name: str, id: int = None, supportedDestinations: set = None) -> None:
        self.id = id
        self.className = className
        self.configuration = configuration
        self.name = name
        self.supportedDestinations = supportedDestinations

    def _validate(self) -> bool:
        return any(x for x in ["className", "configuration", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RuleView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.className, self.configuration, self.name, self.supportedDestinations]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "className", "configuration", "name", "supportedDestinations"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "className":
                    valid_data[k] = str(v)
                if k == "configuration":
                    valid_data[k] = {str(x): y for x, y in v.items()}
                if k == "name":
                    valid_data[k] = str(v)
                if k == "supportedDestinations":
                    valid_data[k] = set({str(x) for x in v})

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "className", "configuration", "name", "supportedDestinations"]:
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
