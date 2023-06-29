from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.enums import SuccessCriteria
from pingaccesssdk.enums import RuleSetElementType


class RuleSetView(Model):
    """A rule set.

    Attributes
    ----------
    id: int
        When creating a new RuleSet, this is the ID for the RuleSet. If not specified, an ID will be automatically assigned. When updating an existing RuleSet, this field is ignored and the ID is determined by the path parameter.

    elementType: RuleSetElementType
        The rule set's element type (what it contains).

    name: str
        (sortable) The rule set's name.

    policy: list
        The list of policy ids assigned to the rule set.

    successCriteria: SuccessCriteria
        (sortable) The rule set's success criteria.

    """

    def __init__(self, name: str, policy: list, id: int = None, elementType: RuleSetElementType = None, successCriteria: SuccessCriteria = None) -> None:
        self.id = id
        self.elementType = elementType
        self.name = name
        self.policy = policy
        self.successCriteria = successCriteria

    def _validate(self) -> bool:
        return any(x for x in ["name", "policy"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RuleSetView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.elementType, self.name, self.policy, self.successCriteria]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "elementType", "name", "policy", "successCriteria"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "elementType":
                    valid_data[k] = RuleSetElementType[v]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "policy":
                    valid_data[k] = [int(x) for x in v]
                if k == "successCriteria":
                    valid_data[k] = SuccessCriteria[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "elementType", "name", "policy", "successCriteria"]:
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
