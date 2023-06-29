from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.o_i_d_c_provider_plugin_view import OIDCProviderPluginView
from pingaccesssdk.models.query_parameter_view import QueryParameterView
from pingaccesssdk.enums import AuditLevel


class OIDCProviderView(Model):
    """The third-party OpenID Connect provider configuration.

    Attributes
    ----------
    auditLevel: AuditLevel
        Enable to record requests to third-party OpenID Connect provider to the audit store.

    description: str
        The description of the third-party OpenID Connect provider.

    issuer: str
        The issuer of the third-party OpenID Connect provider.

    plugin: OIDCProviderPluginView
        The OpenID Connect provider plugin.

    queryParameters: list
        The query parameters used by the authentication request to third-party OpenID Connect provider.

    requestSupportedScopesOnly: bool
        Specifies whether the scopes in an access request should be limited to those advertised in the OIDC metadata.

    trustedCertificateGroupId: int
        The group of certificates to use when authenticating to third-party OpenID Connect provider.

    useProxy: bool
        True if a proxy should be used for HTTP or HTTPS requests.

    useSlo: bool
        True if single log off (SLO) should be used.

    """

    def __init__(self, issuer: str, auditLevel: AuditLevel = None, description: str = None, plugin: OIDCProviderPluginView = None, queryParameters: list = None, requestSupportedScopesOnly: bool = None, trustedCertificateGroupId: int = None, useProxy: bool = None, useSlo: bool = None) -> None:
        self.auditLevel = auditLevel
        self.description = description
        self.issuer = issuer
        self.plugin = plugin
        self.queryParameters = queryParameters
        self.requestSupportedScopesOnly = requestSupportedScopesOnly
        self.trustedCertificateGroupId = trustedCertificateGroupId
        self.useProxy = useProxy
        self.useSlo = useSlo

    def _validate(self) -> bool:
        return any(x for x in ["issuer"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCProviderView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.auditLevel, self.description, self.issuer, self.plugin, self.queryParameters, self.requestSupportedScopesOnly, self.trustedCertificateGroupId, self.useProxy, self.useSlo]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["auditLevel", "description", "issuer", "plugin", "queryParameters", "requestSupportedScopesOnly", "trustedCertificateGroupId", "useProxy", "useSlo"]:
                if k == "auditLevel":
                    valid_data[k] = AuditLevel[v]
                if k == "description":
                    valid_data[k] = str(v)
                if k == "issuer":
                    valid_data[k] = str(v)
                if k == "plugin":
                    valid_data[k] = OIDCProviderPluginView(**v) if v is not None else None
                if k == "queryParameters":
                    valid_data[k] = [QueryParameterView(**x) if x is not None else None for x in v or []]
                if k == "requestSupportedScopesOnly":
                    valid_data[k] = bool(v)
                if k == "trustedCertificateGroupId":
                    valid_data[k] = int(v)
                if k == "useProxy":
                    valid_data[k] = bool(v)
                if k == "useSlo":
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
            if k in ["auditLevel", "description", "issuer", "plugin", "queryParameters", "requestSupportedScopesOnly", "trustedCertificateGroupId", "useProxy", "useSlo"]:
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
