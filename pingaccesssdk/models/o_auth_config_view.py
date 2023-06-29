from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_auth_client_credentials_view import OAuthClientCredentialsView
from pingaccesssdk.models.role_mapping_configuration_view import RoleMappingConfigurationView
from pingaccesssdk.models.embeddable_access_token_validator_view import EmbeddableAccessTokenValidatorView
from pingaccesssdk.models.hidden_field_view import HiddenFieldView


class OAuthConfigView(Model):
    """An OAuth authentication configuration.

    Attributes
    ----------
    accessTokenValidator: EmbeddableAccessTokenValidatorView
        Access Token Validator configuration if the OAuth token validation should occur locally rather than using token introspection.

    clientCredentials: OAuthClientCredentialsView
        Specify the client credentials. This field is ignored when the accessTokenValidator is configured.

    clientId: str
        The client_id of the OAuth client used for validating OAuth access tokens. (DEPRECATED - to be removed in a future release; please use 'clientCredentials' instead)

    clientSecret: HiddenFieldView
        The client secret of the OAuth client used for validating OAuth access tokens. (DEPRECATED - to be removed in a future release; please use 'clientCredentials' instead)

    enabled: bool
        This field is true if OAuth authentication to the Administrative API is enabled.

    roleMapping: RoleMappingConfigurationView
        The configuration for mapping user attributes to roles.

    scope: str
        The scope required to successfully access the API--for example, admin.

    subjectAttributeName: str
        The attribute you want to use from the OAuth access token as the subject for auditing purposes. At runtime, the attribute's value is used as the subject field in audit log entries for the Admin API. This field is ignored when the accessTokenValidator is configured.

    """

    def __init__(self, scope: str, accessTokenValidator: EmbeddableAccessTokenValidatorView = None, clientCredentials: OAuthClientCredentialsView = None, clientId: str = None, clientSecret: HiddenFieldView = None, enabled: bool = None, roleMapping: RoleMappingConfigurationView = None, subjectAttributeName: str = None) -> None:
        self.accessTokenValidator = accessTokenValidator
        self.clientCredentials = clientCredentials
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.enabled = enabled
        self.roleMapping = roleMapping
        self.scope = scope
        self.subjectAttributeName = subjectAttributeName

    def _validate(self) -> bool:
        return any(x for x in ["scope"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OAuthConfigView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.accessTokenValidator, self.clientCredentials, self.clientId, self.clientSecret, self.enabled, self.roleMapping, self.scope, self.subjectAttributeName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["accessTokenValidator", "clientCredentials", "clientId", "clientSecret", "enabled", "roleMapping", "scope", "subjectAttributeName"]:
                if k == "accessTokenValidator":
                    valid_data[k] = EmbeddableAccessTokenValidatorView(**v) if v is not None else None
                if k == "clientCredentials":
                    valid_data[k] = OAuthClientCredentialsView(**v) if v is not None else None
                if k == "clientId":
                    valid_data[k] = str(v)
                if k == "clientSecret":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "roleMapping":
                    valid_data[k] = RoleMappingConfigurationView(**v) if v is not None else None
                if k == "scope":
                    valid_data[k] = str(v)
                if k == "subjectAttributeName":
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
            if k in ["accessTokenValidator", "clientCredentials", "clientId", "clientSecret", "enabled", "roleMapping", "scope", "subjectAttributeName"]:
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
