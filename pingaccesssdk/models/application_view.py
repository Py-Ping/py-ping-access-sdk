from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.policy_item import PolicyItem
from pingaccesssdk.enums import DestinationView
from pingaccesssdk.enums import DefaultAuthTypeView
from pingaccesssdk.enums import ApplicationTypeView


class ApplicationView(Model):
    """An application.

    Attributes
    ----------
    id: int
        When creating a new Application, this is the ID for the Application. If not specified, an ID will be automatically assigned. When updating an existing Application, this field is ignored and the ID is determined by the path parameter.

    accessValidatorId: int
        The ID of the access token validator for local token validation, 1 if the application is protected remotely by an Authorization Server, or zero if unprotected. Only applies to applications of type API.

    agentCacheInvalidatedExpiration: int
        (DEPRECATED - to be removed in a future release; this field is no longer used when processing requests for an application.)

    agentCacheInvalidatedResponseDuration: int
        (DEPRECATED - to be removed in a future release; this field is no longer used when processing requests for an application.)

    agentId: int
        The ID of the agent associated with the application or zero if none.

    allowEmptyPathSegments: bool
        When true, PingAccess will not remove empty path segments from the request URL before matching a request against the resources in this application. Defaults to false.

    applicationType: ApplicationTypeView
        (sortable) The type of application.

    authenticationChallengePolicyId: str
        The UUID of the authentication challenge policy associated with the application.

    caseSensitivePath: bool
        (sortable) True if the path is case sensitive.

    contextRoot: str
        (sortable) The context root of the application.

    defaultAuthType: DefaultAuthTypeView
        For Web + API applications (dynamic) defaultAuthType selects the processing mode when a request: does not have a token (web session, OAuth bearer) or has both tokens.  This setting applies to all resources in the application except where overridden with defaultAuthTypeOverride.

    description: str
        (sortable) A description of the application.

    destination: DestinationView
        (sortable) The application destination type.

    enabled: bool
        (sortable) True if the application is enabled.

    fallbackPostEncoding: str
        (sortable) Specify the name of an encoding to use when preserving POST parameters and the parameters are found to not be UTF-8 encoded.

    identityMappingIds: dict
        A map of Identity Mappings associated with the application. The key is 'Web' or 'API' and the value is an Identity Mapping ID.

    issuer: str
        Branded URL at the OpenID Connect provider to redirect unauthenticated requests to. When specified, this overrides the global token provider's issuer field.

    lastModified: int
        The last modified time of the configuration for this application, its resources and associated policy, as the number of milliseconds since January 1, 1970, 00:00:00 GMT. This field is read-only.

    manualOrderingEnabled: bool
        Enable explicit, manual ordering of application resources and permit regex path patterns.

    name: str
        (sortable) The application name.

    policy: dict
        A map of policy items associated with the application.  The key is 'Web' or 'API' and the value is a list of PolicyItems.

    realm: str
        (sortable) The OAuth realm associated with the application.

    requireHTTPS: bool
        (sortable) True if the application requires HTTPS connections.

    resourceOrder: list
        The explicit resource order defined when manual ordering is enabled. Each existing resource ID must be represented. (Required when 'manualOrderingEnabled' is true.)

    sidebandClientId: str
        The ID of the sideband client associated with the application or null if none.

    siteId: int
        The ID of the site associated with the application or zero if none.

    spaSupportEnabled: bool
        Enable SPA support.

    virtualHostIds: list
        An array of virtual host IDs associated with the application.

    webSessionId: int
        The ID of the web session associated with the application or zero if none.

    """

    def __init__(self, agentId: int, contextRoot: str, defaultAuthType: DefaultAuthTypeView, name: str, siteId: int, spaSupportEnabled: bool, virtualHostIds: list, id: int = None, accessValidatorId: int = None, agentCacheInvalidatedExpiration: int = None, agentCacheInvalidatedResponseDuration: int = None, allowEmptyPathSegments: bool = None, applicationType: ApplicationTypeView = None, caseSensitivePath: bool = None, description: str = None, destination: DestinationView = None, enabled: bool = None, fallbackPostEncoding: str = None, identityMappingIds: dict = None, issuer: str = None, lastModified: int = None, manualOrderingEnabled: bool = None, policy: dict = None, realm: str = None, requireHTTPS: bool = None, resourceOrder: list = None, webSessionId: int = None, authenticationChallengePolicyId: str = None, sidebandClientId: str = None) -> None:
        self.id = id
        self.accessValidatorId = accessValidatorId
        self.agentCacheInvalidatedExpiration = agentCacheInvalidatedExpiration
        self.agentCacheInvalidatedResponseDuration = agentCacheInvalidatedResponseDuration
        self.agentId = agentId
        self.allowEmptyPathSegments = allowEmptyPathSegments
        self.applicationType = applicationType
        self.authenticationChallengePolicyId = authenticationChallengePolicyId
        self.caseSensitivePath = caseSensitivePath
        self.contextRoot = contextRoot
        self.defaultAuthType = defaultAuthType
        self.description = description
        self.destination = destination
        self.enabled = enabled
        self.fallbackPostEncoding = fallbackPostEncoding
        self.identityMappingIds = identityMappingIds
        self.issuer = issuer
        self.lastModified = lastModified
        self.manualOrderingEnabled = manualOrderingEnabled
        self.name = name
        self.policy = policy
        self.realm = realm
        self.requireHTTPS = requireHTTPS
        self.resourceOrder = resourceOrder
        self.sidebandClientId = sidebandClientId
        self.siteId = siteId
        self.spaSupportEnabled = spaSupportEnabled
        self.virtualHostIds = virtualHostIds
        self.webSessionId = webSessionId

    def _validate(self) -> bool:
        return any(x for x in ["agentId", "authenticationChallengePolicyId", "contextRoot", "defaultAuthType", "name", "sidebandClientId", "siteId", "spaSupportEnabled", "virtualHostIds"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ApplicationView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.accessValidatorId, self.agentCacheInvalidatedExpiration, self.agentCacheInvalidatedResponseDuration, self.agentId, self.allowEmptyPathSegments, self.applicationType, self.authenticationChallengePolicyId, self.caseSensitivePath, self.contextRoot, self.defaultAuthType, self.description, self.destination, self.enabled, self.fallbackPostEncoding, self.identityMappingIds, self.issuer, self.lastModified, self.manualOrderingEnabled, self.name, self.policy, self.realm, self.requireHTTPS, self.resourceOrder, self.sidebandClientId, self.siteId, self.spaSupportEnabled, self.virtualHostIds, self.webSessionId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "accessValidatorId", "agentCacheInvalidatedExpiration", "agentCacheInvalidatedResponseDuration", "agentId", "allowEmptyPathSegments", "applicationType", "authenticationChallengePolicyId", "caseSensitivePath", "contextRoot", "defaultAuthType", "description", "destination", "enabled", "fallbackPostEncoding", "identityMappingIds", "issuer", "lastModified", "manualOrderingEnabled", "name", "policy", "realm", "requireHTTPS", "resourceOrder", "sidebandClientId", "siteId", "spaSupportEnabled", "virtualHostIds", "webSessionId"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "accessValidatorId":
                    valid_data[k] = int(v)
                if k == "agentCacheInvalidatedExpiration":
                    valid_data[k] = int(v)
                if k == "agentCacheInvalidatedResponseDuration":
                    valid_data[k] = int(v)
                if k == "agentId":
                    valid_data[k] = int(v)
                if k == "allowEmptyPathSegments":
                    valid_data[k] = bool(v)
                if k == "applicationType":
                    valid_data[k] = ApplicationTypeView[v]
                if k == "authenticationChallengePolicyId":
                    valid_data[k] = str(v)
                if k == "caseSensitivePath":
                    valid_data[k] = bool(v)
                if k == "contextRoot":
                    valid_data[k] = str(v)
                if k == "defaultAuthType":
                    valid_data[k] = DefaultAuthTypeView[v]
                if k == "description":
                    valid_data[k] = str(v)
                if k == "destination":
                    valid_data[k] = DestinationView[v]
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "fallbackPostEncoding":
                    valid_data[k] = str(v)
                if k == "identityMappingIds":
                    valid_data[k] = {str(x): int(y) for x, y in v.items()}
                if k == "issuer":
                    valid_data[k] = str(v)
                if k == "lastModified":
                    valid_data[k] = int(v)
                if k == "manualOrderingEnabled":
                    valid_data[k] = bool(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "policy":
                    valid_data[k] = {str(x): [PolicyItem(**z) if z is not None else None for z in y] for x, y in v.items()}
                if k == "realm":
                    valid_data[k] = str(v)
                if k == "requireHTTPS":
                    valid_data[k] = bool(v)
                if k == "resourceOrder":
                    valid_data[k] = [int(x) for x in v]
                if k == "sidebandClientId":
                    valid_data[k] = str(v)
                if k == "siteId":
                    valid_data[k] = int(v)
                if k == "spaSupportEnabled":
                    valid_data[k] = bool(v)
                if k == "virtualHostIds":
                    valid_data[k] = [int(x) for x in v]
                if k == "webSessionId":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "accessValidatorId", "agentCacheInvalidatedExpiration", "agentCacheInvalidatedResponseDuration", "agentId", "allowEmptyPathSegments", "applicationType", "authenticationChallengePolicyId", "caseSensitivePath", "contextRoot", "defaultAuthType", "description", "destination", "enabled", "fallbackPostEncoding", "identityMappingIds", "issuer", "lastModified", "manualOrderingEnabled", "name", "policy", "realm", "requireHTTPS", "resourceOrder", "sidebandClientId", "siteId", "spaSupportEnabled", "virtualHostIds", "webSessionId"]:
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
