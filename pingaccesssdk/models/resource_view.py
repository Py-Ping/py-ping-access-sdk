from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.path_pattern_view import PathPatternView
from pingaccesssdk.models.resource_type_configuration_view import ResourceTypeConfigurationView
from pingaccesssdk.models.query_param_config_view import QueryParamConfigView
from pingaccesssdk.models.policy_item import PolicyItem
from pingaccesssdk.enums import AuditLevel
from pingaccesssdk.enums import ResourceTypeView
from pingaccesssdk.enums import DefaultAuthTypeView


class ResourceView(Model):
    """A resource.

    Attributes
    ----------
    id: int
        When creating a new Resource, this is the ID for the Resource. If not specified, an ID will be automatically assigned. When updating an existing Resource, this field is ignored and the ID is determined by the path parameter.

    anonymous: bool
        (sortable) True if the resource is anonymous.

    applicationId: int
        The id of the associated application. This field is read-only.

    auditLevel: AuditLevel
        (sortable) Indicates if audit logging is enabled for the resource.

    authenticationChallengePolicyId: str
        The UUID of the authentication challenge policy associated with the resource. This policy takes precedence over an application-level policy.

    defaultAuthTypeOverride: DefaultAuthTypeView
        For Web + API applications (dynamic) defaultAuthType selects the processing mode when a request: does not have a token (web session, OAuth bearer) or has both tokens.  defaultAuthTypeOverride overrides the defaultAuthType at the application level for this resource.  A value of null indicates the resource should not override the defaultAuthType.

    enabled: bool
        (sortable) True if the resource is enabled.

    methods: set
        An array of HTTP methods configured for the resource.

    name: str
        (sortable) The name of the resource.

    pathPatterns: list
        A list of one or more request path-matching patterns.

    pathPrefixes: list
        An array of path prefixes for the resource (DEPRECATED - to be removed in a future release; please use 'pathPatterns' instead).

    policy: dict
        A map of policy items associated with the resource.  The key is 'Web' or 'API' and the value is a list of PolicyItems.

    queryParamConfig: QueryParamConfigView
        Query parameter configuration settings for matching a query string.

    resourceType: ResourceTypeView
        (sortable) The type of this resource. 'Standard' resources are those served by the protected applications. 'Virtual' resources do not have a corresponding resource in the protected application. Instead, when accessing the resource, PingAccess returns a response created by the response generator defined in the resource type configuration. The default type is 'Standard'.

    resourceTypeConfiguration: ResourceTypeConfigurationView
        A container for configuration specific to different types of resources.

    rootResource: bool
        (sortable) True if the resource is the root resource for the application.

    unprotected: bool
        (sortable) True if the resource is unprotected.

    """

    def __init__(self, authenticationChallengePolicyId: str, defaultAuthTypeOverride: DefaultAuthTypeView, methods: set, name: str, id: int = None, anonymous: bool = None, applicationId: int = None, auditLevel: AuditLevel = None, enabled: bool = None, pathPatterns: list = None, pathPrefixes: list = None, policy: dict = None, queryParamConfig: QueryParamConfigView = None, resourceType: ResourceTypeView = None, resourceTypeConfiguration: ResourceTypeConfigurationView = None, rootResource: bool = None, unprotected: bool = None) -> None:
        self.id = id
        self.anonymous = anonymous
        self.applicationId = applicationId
        self.auditLevel = auditLevel
        self.authenticationChallengePolicyId = authenticationChallengePolicyId
        self.defaultAuthTypeOverride = defaultAuthTypeOverride
        self.enabled = enabled
        self.methods = methods
        self.name = name
        self.pathPatterns = pathPatterns
        self.pathPrefixes = pathPrefixes
        self.policy = policy
        self.queryParamConfig = queryParamConfig
        self.resourceType = resourceType
        self.resourceTypeConfiguration = resourceTypeConfiguration
        self.rootResource = rootResource
        self.unprotected = unprotected

    def _validate(self) -> bool:
        return any(x for x in ["authenticationChallengePolicyId", "defaultAuthTypeOverride", "methods", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ResourceView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.anonymous, self.applicationId, self.auditLevel, self.authenticationChallengePolicyId, self.defaultAuthTypeOverride, self.enabled, self.methods, self.name, self.pathPatterns, self.pathPrefixes, self.policy, self.queryParamConfig, self.resourceType, self.resourceTypeConfiguration, self.rootResource, self.unprotected]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "anonymous", "applicationId", "auditLevel", "authenticationChallengePolicyId", "defaultAuthTypeOverride", "enabled", "methods", "name", "pathPatterns", "pathPrefixes", "policy", "queryParamConfig", "resourceType", "resourceTypeConfiguration", "rootResource", "unprotected"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "anonymous":
                    valid_data[k] = bool(v)
                if k == "applicationId":
                    valid_data[k] = int(v)
                if k == "auditLevel":
                    valid_data[k] = AuditLevel[v]
                if k == "authenticationChallengePolicyId":
                    valid_data[k] = str(v)
                if k == "defaultAuthTypeOverride":
                    valid_data[k] = DefaultAuthTypeView[v]
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "methods":
                    valid_data[k] = set({str(x) for x in v})
                if k == "name":
                    valid_data[k] = str(v)
                if k == "pathPatterns":
                    valid_data[k] = [PathPatternView(**x) if x is not None else None for x in v or []]
                if k == "pathPrefixes":
                    valid_data[k] = [str(x) for x in v]
                if k == "policy":
                    valid_data[k] = {str(x): [PolicyItem(**z) if z is not None else None for z in y] for x, y in v.items()}
                if k == "queryParamConfig":
                    valid_data[k] = QueryParamConfigView(**v) if v is not None else None
                if k == "resourceType":
                    valid_data[k] = ResourceTypeView[v]
                if k == "resourceTypeConfiguration":
                    valid_data[k] = ResourceTypeConfigurationView(**v) if v is not None else None
                if k == "rootResource":
                    valid_data[k] = bool(v)
                if k == "unprotected":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "anonymous", "applicationId", "auditLevel", "authenticationChallengePolicyId", "defaultAuthTypeOverride", "enabled", "methods", "name", "pathPatterns", "pathPrefixes", "policy", "queryParamConfig", "resourceType", "resourceTypeConfiguration", "rootResource", "unprotected"]:
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
