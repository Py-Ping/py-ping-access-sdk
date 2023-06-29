from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.configuration_parent_field import ConfigurationParentField
from pingaccesssdk.models.help import Help
from pingaccesssdk.models.configuration_option import ConfigurationOption
from pingaccesssdk.enums import ConfigurationType


class ConfigurationField(Model):
    """Details for configuration in the administrator console.

    Attributes
    ----------
    advanced: bool
        Indicates that the configuration field is an advanced field or not.

    buttonGroup: str
        The name of group radio buttons that cooperate in a single selection.

    default: str
        The default value of the configuration field.

    deselectable: bool
        Indicates that a radio button is able to be deselected.

    fields: list
        The list of configuration fields that the current configuration field is the parent of.

    help: Help
        The help attributes of the configuration field.

    label: str
        The label of the configuration field.

    name: str
        The name of the configuration field.

    options: list
        The available options for the select based configuration fields.

    parentField: ConfigurationParentField
        The parent field attributes.

    required: bool
        Indicates that the configuration field value is required or not.

    type: ConfigurationType
        The type of the configuration field.

    """

    def __init__(self, advanced: bool, buttonGroup: str, default: str, deselectable: bool, fields: list, help: Help, label: str, name: str, options: list, parentField: ConfigurationParentField, required: bool, type: ConfigurationType) -> None:
        self.advanced = advanced
        self.buttonGroup = buttonGroup
        self.default = default
        self.deselectable = deselectable
        self.fields = fields
        self.help = help
        self.label = label
        self.name = name
        self.options = options
        self.parentField = parentField
        self.required = required
        self.type = type

    def _validate(self) -> bool:
        return any(x for x in ["advanced", "buttonGroup", "default", "deselectable", "fields", "help", "label", "name", "options", "parentField", "required", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigurationField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.advanced, self.buttonGroup, self.default, self.deselectable, self.fields, self.help, self.label, self.name, self.options, self.parentField, self.required, self.type]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["advanced", "buttonGroup", "default", "deselectable", "fields", "help", "label", "name", "options", "parentField", "required", "type"]:
                if k == "advanced":
                    valid_data[k] = bool(v)
                if k == "buttonGroup":
                    valid_data[k] = str(v)
                if k == "default":
                    valid_data[k] = str(v)
                if k == "deselectable":
                    valid_data[k] = bool(v)
                if k == "fields":
                    valid_data[k] = [ConfigurationField(**x) if x is not None else None for x in v or []]
                if k == "help":
                    valid_data[k] = Help(**v) if v is not None else None
                if k == "label":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "options":
                    valid_data[k] = [ConfigurationOption(**x) if x is not None else None for x in v or []]
                if k == "parentField":
                    valid_data[k] = ConfigurationParentField(**v) if v is not None else None
                if k == "required":
                    valid_data[k] = bool(v)
                if k == "type":
                    valid_data[k] = ConfigurationType[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["advanced", "buttonGroup", "default", "deselectable", "fields", "help", "label", "name", "options", "parentField", "required", "type"]:
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
