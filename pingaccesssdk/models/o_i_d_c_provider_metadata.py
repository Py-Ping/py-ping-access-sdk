from pingaccesssdk.model import Model
from enum import Enum


class OIDCProviderMetadata(Model):
    """The OpenID Connect provider's metadata.

    Attributes
    ----------
    authorization_endpoint: str
        URL of the OpenID Connect provider's authorization endpoint.

    backchannel_authentication_endpoint: str
        the endpoint used to initiate an out-of-band authentication.

    claim_types_supported: list
        JSON array containing a list of the claim types that the OpenID Connect provider supports.

    claims_parameter_supported: bool
        boolean value specifying whether the OpenID Connect provider supports use of the claims parameter, with true indicating support.

    claims_supported: list
        JSON array containing a list of the claim names of the claims that the OpenID Connect provider MAY be able to supply values for.

    code_challenge_methods_supported: list
        Proof Key for Code Exchange (PKCE) code challenge methods supported by this OpenID Connect provider.

    end_session_endpoint: str
        URL at the OpenID Connect provider to which a relying party can perform a redirect to request that the end-user be logged out at the OpenID Connect provider.

    grant_types_supported: list
        JSON array containing a list of the OAuth 2.0 grant type values that this OpenID Connect provider supports.

    id_token_signing_alg_values_supported: list
        JSON array containing a list of the JWS signing algorithms supported by the OpenID Connect provider for the id token to encode the claims in a JWT.

    introspection_endpoint: str
        URL of the OpenID Connect provider's OAuth 2.0 introspection endpoint.

    issuer: str
        OpenID Connect provider's issuer identifier URL.

    jwks_uri: str
        URL of the OpenID Connect provider's JWK Set document.

    mtls_endpoint_aliases: dict
        a map of alternative authorization server endpoints. The key is an authorization server endpoint, and the value is a preferred URL for the endpoint.

    ping_end_session_endpoint: str
        PingFederate logout endpoint. (Not applicable if PingFederate is not the OpenID Connect provider)

    ping_revoked_sris_endpoint: str
        PingFederate session revocation endpoint. (Not applicable if PingFederate is not the OpenID Connect provider)

    request_object_signing_alg_values_supported: list
        JSON array containing a list of the JWS signing algorithms supported by the OpenID Connect provider for request objects.

    request_parameter_supported: bool
        boolean value specifying whether the OpenID Connect provider supports use of the request parameter, with true indicating support.

    request_uri_parameter_supported: bool
        boolean value specifying whether the OpenID Connect provider supports use of the request_uri parameter, with true indicating support.

    response_modes_supported: list
        JSON array containing a list of the OAuth 2.0 "response_mode" values that this OpenID Connect provider supports.

    response_types_supported: list
        JSON array containing a list of the OAuth 2.0 "response_type" values that this OpenID Connect provider supports.

    revocation_endpoint: str
        URL of the OpenID Connect provider's OAuth 2.0 revocation endpoint.

    scopes_supported: list
        JSON array containing a list of the OAuth 2.0 "scope" values that this OpenID Connect provider supports.

    subject_types_supported: list
        JSON array containing a list of the Subject Identifier types that this OpenID Connect provider supports.

    token_endpoint: str
        URL of the OpenID Connect provider's token endpoint.

    token_endpoint_auth_methods_supported: list
        JSON array containing a list of client authentication methods supported by this token endpoint.

    token_endpoint_auth_signing_alg_values_supported: list
        JSON array containing a list of client authentication signing algorithms supported by this token endpoint.

    userinfo_endpoint: str
        URL of the OpenID Connect provider's userInfo endpoint.

    userinfo_signing_alg_values_supported: list
        JSON array containing a list of the JWS signing algorithms supported by the userInfo endpoint to encode the claims in a JWT.

    """

    def __init__(self, authorization_endpoint: str, backchannel_authentication_endpoint: str, claim_types_supported: list, claims_parameter_supported: bool, claims_supported: list, code_challenge_methods_supported: list, end_session_endpoint: str, grant_types_supported: list, id_token_signing_alg_values_supported: list, introspection_endpoint: str, issuer: str, jwks_uri: str, mtls_endpoint_aliases: dict, ping_end_session_endpoint: str, ping_revoked_sris_endpoint: str, request_object_signing_alg_values_supported: list, request_parameter_supported: bool, request_uri_parameter_supported: bool, response_modes_supported: list, response_types_supported: list, revocation_endpoint: str, scopes_supported: list, subject_types_supported: list, token_endpoint: str, token_endpoint_auth_methods_supported: list, token_endpoint_auth_signing_alg_values_supported: list, userinfo_endpoint: str, userinfo_signing_alg_values_supported: list) -> None:
        self.authorization_endpoint = authorization_endpoint
        self.backchannel_authentication_endpoint = backchannel_authentication_endpoint
        self.claim_types_supported = claim_types_supported
        self.claims_parameter_supported = claims_parameter_supported
        self.claims_supported = claims_supported
        self.code_challenge_methods_supported = code_challenge_methods_supported
        self.end_session_endpoint = end_session_endpoint
        self.grant_types_supported = grant_types_supported
        self.id_token_signing_alg_values_supported = id_token_signing_alg_values_supported
        self.introspection_endpoint = introspection_endpoint
        self.issuer = issuer
        self.jwks_uri = jwks_uri
        self.mtls_endpoint_aliases = mtls_endpoint_aliases
        self.ping_end_session_endpoint = ping_end_session_endpoint
        self.ping_revoked_sris_endpoint = ping_revoked_sris_endpoint
        self.request_object_signing_alg_values_supported = request_object_signing_alg_values_supported
        self.request_parameter_supported = request_parameter_supported
        self.request_uri_parameter_supported = request_uri_parameter_supported
        self.response_modes_supported = response_modes_supported
        self.response_types_supported = response_types_supported
        self.revocation_endpoint = revocation_endpoint
        self.scopes_supported = scopes_supported
        self.subject_types_supported = subject_types_supported
        self.token_endpoint = token_endpoint
        self.token_endpoint_auth_methods_supported = token_endpoint_auth_methods_supported
        self.token_endpoint_auth_signing_alg_values_supported = token_endpoint_auth_signing_alg_values_supported
        self.userinfo_endpoint = userinfo_endpoint
        self.userinfo_signing_alg_values_supported = userinfo_signing_alg_values_supported

    def _validate(self) -> bool:
        return any(x for x in ["authorization_endpoint", "backchannel_authentication_endpoint", "claim_types_supported", "claims_parameter_supported", "claims_supported", "code_challenge_methods_supported", "end_session_endpoint", "grant_types_supported", "id_token_signing_alg_values_supported", "introspection_endpoint", "issuer", "jwks_uri", "mtls_endpoint_aliases", "ping_end_session_endpoint", "ping_revoked_sris_endpoint", "request_object_signing_alg_values_supported", "request_parameter_supported", "request_uri_parameter_supported", "response_modes_supported", "response_types_supported", "revocation_endpoint", "scopes_supported", "subject_types_supported", "token_endpoint", "token_endpoint_auth_methods_supported", "token_endpoint_auth_signing_alg_values_supported", "userinfo_endpoint", "userinfo_signing_alg_values_supported"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCProviderMetadata):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.authorization_endpoint, self.backchannel_authentication_endpoint, self.claim_types_supported, self.claims_parameter_supported, self.claims_supported, self.code_challenge_methods_supported, self.end_session_endpoint, self.grant_types_supported, self.id_token_signing_alg_values_supported, self.introspection_endpoint, self.issuer, self.jwks_uri, self.mtls_endpoint_aliases, self.ping_end_session_endpoint, self.ping_revoked_sris_endpoint, self.request_object_signing_alg_values_supported, self.request_parameter_supported, self.request_uri_parameter_supported, self.response_modes_supported, self.response_types_supported, self.revocation_endpoint, self.scopes_supported, self.subject_types_supported, self.token_endpoint, self.token_endpoint_auth_methods_supported, self.token_endpoint_auth_signing_alg_values_supported, self.userinfo_endpoint, self.userinfo_signing_alg_values_supported]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["authorization_endpoint", "backchannel_authentication_endpoint", "claim_types_supported", "claims_parameter_supported", "claims_supported", "code_challenge_methods_supported", "end_session_endpoint", "grant_types_supported", "id_token_signing_alg_values_supported", "introspection_endpoint", "issuer", "jwks_uri", "mtls_endpoint_aliases", "ping_end_session_endpoint", "ping_revoked_sris_endpoint", "request_object_signing_alg_values_supported", "request_parameter_supported", "request_uri_parameter_supported", "response_modes_supported", "response_types_supported", "revocation_endpoint", "scopes_supported", "subject_types_supported", "token_endpoint", "token_endpoint_auth_methods_supported", "token_endpoint_auth_signing_alg_values_supported", "userinfo_endpoint", "userinfo_signing_alg_values_supported"]:
                if k == "authorization_endpoint":
                    valid_data[k] = str(v)
                if k == "backchannel_authentication_endpoint":
                    valid_data[k] = str(v)
                if k == "claim_types_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "claims_parameter_supported":
                    valid_data[k] = bool(v)
                if k == "claims_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "code_challenge_methods_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "end_session_endpoint":
                    valid_data[k] = str(v)
                if k == "grant_types_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "id_token_signing_alg_values_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "introspection_endpoint":
                    valid_data[k] = str(v)
                if k == "issuer":
                    valid_data[k] = str(v)
                if k == "jwks_uri":
                    valid_data[k] = str(v)
                if k == "mtls_endpoint_aliases":
                    valid_data[k] = {str(x): str(y) for x, y in v.items()}
                if k == "ping_end_session_endpoint":
                    valid_data[k] = str(v)
                if k == "ping_revoked_sris_endpoint":
                    valid_data[k] = str(v)
                if k == "request_object_signing_alg_values_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "request_parameter_supported":
                    valid_data[k] = bool(v)
                if k == "request_uri_parameter_supported":
                    valid_data[k] = bool(v)
                if k == "response_modes_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "response_types_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "revocation_endpoint":
                    valid_data[k] = str(v)
                if k == "scopes_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "subject_types_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "token_endpoint":
                    valid_data[k] = str(v)
                if k == "token_endpoint_auth_methods_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "token_endpoint_auth_signing_alg_values_supported":
                    valid_data[k] = [str(x) for x in v]
                if k == "userinfo_endpoint":
                    valid_data[k] = str(v)
                if k == "userinfo_signing_alg_values_supported":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["authorization_endpoint", "backchannel_authentication_endpoint", "claim_types_supported", "claims_parameter_supported", "claims_supported", "code_challenge_methods_supported", "end_session_endpoint", "grant_types_supported", "id_token_signing_alg_values_supported", "introspection_endpoint", "issuer", "jwks_uri", "mtls_endpoint_aliases", "ping_end_session_endpoint", "ping_revoked_sris_endpoint", "request_object_signing_alg_values_supported", "request_parameter_supported", "request_uri_parameter_supported", "response_modes_supported", "response_types_supported", "revocation_endpoint", "scopes_supported", "subject_types_supported", "token_endpoint", "token_endpoint_auth_methods_supported", "token_endpoint_auth_signing_alg_values_supported", "userinfo_endpoint", "userinfo_signing_alg_values_supported"]:
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
