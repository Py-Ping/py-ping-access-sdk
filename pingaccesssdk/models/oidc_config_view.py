from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.admin_web_session_oidc_configuration_view import AdminWebSessionOidcConfigurationView
from pingaccesssdk.models.role_mapping_configuration_view import RoleMappingConfigurationView


class OidcConfigView(Model):
    """An OIDC authentication configuration.

    Attributes
    ----------
    authnReqListId: int
        The ID of the authentication requirement list for Administrative SSO login to PingAccess.

    enabled: bool
        This field is true to enable Administrator SSO Authentication.

    oidcConfiguration: AdminWebSessionOidcConfigurationView
        The OIDC configuration for the PA admin web session.

    roleMapping: RoleMappingConfigurationView
        The configuration for mapping user attributes to roles.

    useSlo: bool
        Enable if OIDC single log out should be used on the /pa/oidc/logout for admin console.

    usernameAttributeName: str
        Attribute to display as the logged in user. If not set, the sub attribute will be used.

    """

    def __init__(self, oidcConfiguration: AdminWebSessionOidcConfigurationView, authnReqListId: int = None, enabled: bool = None, roleMapping: RoleMappingConfigurationView = None, useSlo: bool = None, usernameAttributeName: str = None) -> None:
        self.authnReqListId = authnReqListId
        self.enabled = enabled
        self.oidcConfiguration = oidcConfiguration
        self.roleMapping = roleMapping
        self.useSlo = useSlo
        self.usernameAttributeName = usernameAttributeName

    def _validate(self) -> bool:
        return any(x for x in ["oidcConfiguration"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OidcConfigView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.authnReqListId, self.enabled, self.oidcConfiguration, self.roleMapping, self.useSlo, self.usernameAttributeName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["authnReqListId", "enabled", "oidcConfiguration", "roleMapping", "useSlo", "usernameAttributeName"]:
                if k == "authnReqListId":
                    valid_data[k] = int(v)
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "oidcConfiguration":
                    valid_data[k] = AdminWebSessionOidcConfigurationView(**v) if v is not None else None
                if k == "roleMapping":
                    valid_data[k] = RoleMappingConfigurationView(**v) if v is not None else None
                if k == "useSlo":
                    valid_data[k] = bool(v)
                if k == "usernameAttributeName":
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
            if k in ["authnReqListId", "enabled", "oidcConfiguration", "roleMapping", "useSlo", "usernameAttributeName"]:
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
