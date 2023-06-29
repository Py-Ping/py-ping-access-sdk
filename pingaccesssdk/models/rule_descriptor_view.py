from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.configuration_field import ConfigurationField
from pingaccesssdk.enums import RuleInterceptorCategory
from pingaccesssdk.enums import RuleInterceptorSupportedDestination


class RuleDescriptorView(Model):
    """A rule descriptor.

    Attributes
    ----------
    agentCachingDisabled: bool
        Indicates that agent caching is disabled or not.

    category: RuleInterceptorCategory
        The category of the rule.

    className: str
        The class name of the rule.

    configurationFields: list
        The list of configuration fields of the rule

    label: str
        The label of the rule.

    modes: list
        The modes that the rules can be used in. Site mode implies Sideband and Site destination support.

    type: str
        The type of the rule.

    """

    def __init__(self, agentCachingDisabled: bool, category: RuleInterceptorCategory, className: str, configurationFields: list, label: str, modes: list, type: str) -> None:
        self.agentCachingDisabled = agentCachingDisabled
        self.category = category
        self.className = className
        self.configurationFields = configurationFields
        self.label = label
        self.modes = modes
        self.type = type

    def _validate(self) -> bool:
        return any(x for x in ["agentCachingDisabled", "category", "className", "configurationFields", "label", "modes", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RuleDescriptorView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.agentCachingDisabled, self.category, self.className, self.configurationFields, self.label, self.modes, self.type]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["agentCachingDisabled", "category", "className", "configurationFields", "label", "modes", "type"]:
                if k == "agentCachingDisabled":
                    valid_data[k] = bool(v)
                if k == "category":
                    valid_data[k] = RuleInterceptorCategory[v]
                if k == "className":
                    valid_data[k] = str(v)
                if k == "configurationFields":
                    valid_data[k] = [ConfigurationField(**x) if x is not None else None for x in v or []]
                if k == "label":
                    valid_data[k] = str(v)
                if k == "modes":
                    valid_data[k] = [RuleInterceptorSupportedDestination[x] for x in v]
                if k == "type":
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
            if k in ["agentCachingDisabled", "category", "className", "configurationFields", "label", "modes", "type"]:
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
