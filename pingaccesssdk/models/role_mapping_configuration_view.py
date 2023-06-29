from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.required_attribute_mapping_view import RequiredAttributeMappingView
from pingaccesssdk.models.optional_attribute_mapping_view import OptionalAttributeMappingView


class RoleMappingConfigurationView(Model):
    """Configuration for mapping user attributes to roles.

    Attributes
    ----------
    administrator: RequiredAttributeMappingView
        The user attribute configuration for determining if a user has an administrator role.

    auditor: OptionalAttributeMappingView
        The user attribute configuration for determining if a user has an auditor role.

    enabled: bool
        Set to true to enable mapping of user attributes to roles.

    platformAdmin: OptionalAttributeMappingView
        The user attribute configuration for determining if a user has an platform administrator role.

    """

    def __init__(self, administrator: RequiredAttributeMappingView = None, auditor: OptionalAttributeMappingView = None, enabled: bool = None, platformAdmin: OptionalAttributeMappingView = None) -> None:
        self.administrator = administrator
        self.auditor = auditor
        self.enabled = enabled
        self.platformAdmin = platformAdmin

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RoleMappingConfigurationView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.administrator, self.auditor, self.enabled, self.platformAdmin]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["administrator", "auditor", "enabled", "platformAdmin"]:
                if k == "administrator":
                    valid_data[k] = RequiredAttributeMappingView(**v) if v is not None else None
                if k == "auditor":
                    valid_data[k] = OptionalAttributeMappingView(**v) if v is not None else None
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "platformAdmin":
                    valid_data[k] = OptionalAttributeMappingView(**v) if v is not None else None

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["administrator", "auditor", "enabled", "platformAdmin"]:
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
