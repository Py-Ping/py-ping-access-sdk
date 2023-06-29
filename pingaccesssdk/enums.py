from enum import Enum


ConfigurationType = Enum(
    value="ConfigurationType",
    names=[
        ("TEXT", 1),
        ("TEXTAREA", 2),
        ("TIME", 3),
        ("SELECT", 4),
        ("GROOVY", 5),
        ("CONCEALED", 6),
        ("LIST", 7),
        ("TABLE", 8),
        ("CHECKBOX", 9),
        ("AUTOCOMPLETEOPEN", 10),
        ("AUTOCOMPLETECLOSED", 11),
        ("COMPOSITE", 12),
        ("RADIO_BUTTON", 13),
    ]
)


AcmeCertState = Enum(
    value="AcmeCertState",
    names=[
        ("PENDING", 1),
        ("READY", 2),
        ("PROCESSING", 3),
        ("VALID", 4),
        ("INVALID", 5),
        ("UNKNOWN", 6),
    ]
)


HashAlgorithm = Enum(
    value="HashAlgorithm",
    names=[
        ("MD5", 1),
        ("SHA1", 2),
        ("SHA256", 3),
        ("SHA384", 4),
        ("SHA512", 5),
    ]
)


AdminAccessControlDirective = Enum(
    value="AdminAccessControlDirective",
    names=[
        ("DENY_POLICY_CONFIGURATION", 1),
        ("DENY_APPLICATION_CREATION", 2),
        ("DENY_API_APPLICATION_CREATION", 3),
        ("DENY_AUTH_REQ_CREATION", 4),
        ("DENY_PING_FEDERATE_CONFIGURATION", 5),
        ("DENY_THIRD_PARTY_OAUTH_CONFIGURATION", 6),
        ("DENY_XPOST_WEBSESSION_CONFIGURATION", 7),
        ("DENY_POST_WEBSESSION_CONFIGURATION", 8),
        ("REQUIRE_AAD_TOKEN_PROVIDER_ISSUER", 9),
        ("DENY_API_AUTHENTICATION_CONFIGURATION", 10),
        ("DENY_CUSTOM_SITE_AUTHENTICATOR_CREATION", 11),
        ("DENY_CUSTOM_LOAD_BALANCING_STRATEGY_CREATION", 12),
        ("DENY_CUSTOM_AVAILABILITY_PROFILE_CREATION", 13),
        ("DENY_CUSTOM_IDENTITY_MAPPING_CREATION", 14),
        ("DENY_ADMIN_AUTHENTICATION_CONFIGURATION", 15),
        ("DENY_ENVIRONMENT_CONFIGURATION", 16),
        ("DENY_USERS_CONFIGURATION", 17),
        ("DENY_WRITE_ACCESS", 18),
        ("DENY_BULK_CONFIG_ACCESS", 19),
    ]
)


Role = Enum(
    value="Role",
    names=[
        ("ADMINISTRATOR", 1),
        ("AUDITOR", 2),
        ("PLATFORM_ADMIN", 3),
    ]
)


CertStatus = Enum(
    value="CertStatus",
    names=[
        ("Valid", 1),
        ("Expired", 2),
        ("Not yet valid", 3),
        ("Revoked", 4),
        ("Undetermined revocation status", 5),
        ("No path to trust anchor", 6),
        ("Invalid", 7),
    ]
)


ListValueLocation = Enum(
    value="ListValueLocation",
    names=[
        ("FIRST", 1),
        ("LAST", 2),
    ]
)


GeneralNameEnum = Enum(
    value="GeneralNameEnum",
    names=[
        ("otherName", 1),
        ("rfc822Name", 2),
        ("dNSName", 3),
        ("x400Address", 4),
        ("directoryName", 5),
        ("ediPartyName", 6),
        ("uniformResourceIdentifier", 7),
        ("iPAddress", 8),
        ("registeredID", 9),
    ]
)


UnknownResourceMode = Enum(
    value="UnknownResourceMode",
    names=[
        ("DENY", 1),
        ("PASSTHROUGH", 2),
    ]
)


ApplicationTypeView = Enum(
    value="ApplicationTypeView",
    names=[
        ("Web", 1),
        ("API", 2),
        ("Dynamic", 3),
    ]
)


DefaultAuthTypeView = Enum(
    value="DefaultAuthTypeView",
    names=[
        ("Web", 1),
        ("API", 2),
    ]
)


DestinationView = Enum(
    value="DestinationView",
    names=[
        ("Site", 1),
        ("Agent", 2),
        ("Sideband", 3),
    ]
)


QueryParamPatternType = Enum(
    value="QueryParamPatternType",
    names=[
        ("EXACT", 1),
    ]
)


PathPatternType = Enum(
    value="PathPatternType",
    names=[
        ("WILDCARD", 1),
        ("REGEX", 2),
    ]
)


AuditLevel = Enum(
    value="AuditLevel",
    names=[
        ("ON", 1),
        ("OFF", 2),
    ]
)


ResourceTypeView = Enum(
    value="ResourceTypeView",
    names=[
        ("Standard", 1),
        ("Virtual", 2),
    ]
)


EntryType = Enum(
    value="EntryType",
    names=[
        ("ApplicationResource", 1),
        ("GlobalUnprotectedResource", 2),
    ]
)


OidcLoginType = Enum(
    value="OidcLoginType",
    names=[
        ("Code", 1),
        ("POST", 2),
        ("x_post", 3),
    ]
)


PkceChallengeTypeView = Enum(
    value="PkceChallengeTypeView",
    names=[
        ("SHA256", 1),
        ("OFF", 2),
    ]
)


CredentialsType = Enum(
    value="CredentialsType",
    names=[
        ("SECRET", 1),
        ("CERTIFICATE", 2),
        ("PRIVATE_KEY_JWT", 3),
    ]
)


WebSessionCookieType = Enum(
    value="WebSessionCookieType",
    names=[
        ("Encrypted", 1),
        ("Signed", 2),
    ]
)


ConfiguredAuthorizationServerType = Enum(
    value="ConfiguredAuthorizationServerType",
    names=[
        ("PINGFEDERATE_RUNTIME", 1),
        ("PINGONE", 2),
        ("COMMON_AUTHZSERVER", 3),
        ("ADMIN_TOKENPROVIDER", 4),
    ]
)


AuthenticationType = Enum(
    value="AuthenticationType",
    names=[
        ("OAuth", 1),
        ("Cookie", 2),
        ("Basic", 3),
    ]
)


RuleInterceptorCategory = Enum(
    value="RuleInterceptorCategory",
    names=[
        ("AccessControl", 1),
        ("Processing", 2),
    ]
)


RuleInterceptorSupportedDestination = Enum(
    value="RuleInterceptorSupportedDestination",
    names=[
        ("Site", 1),
        ("Agent", 2),
    ]
)


RuleSetElementType = Enum(
    value="RuleSetElementType",
    names=[
        ("Rule", 1),
        ("RuleSet", 2),
    ]
)


SuccessCriteria = Enum(
    value="SuccessCriteria",
    names=[
        ("SuccessIfAllSucceed", 1),
        ("SuccessIfAnyOneSucceeds", 2),
    ]
)


SidebandClientCredentialsType = Enum(
    value="SidebandClientCredentialsType",
    names=[
        ("SECRET", 1),
    ]
)


TokenProviderTypeView = Enum(
    value="TokenProviderTypeView",
    names=[
        ("PingFederate", 1),
        ("Common", 2),
        ("PingOneForCustomers", 3),
    ]
)


ContentType = Enum(
    value="ContentType",
    names=[
        ("JSON", 1),
        ("HTML", 2),
        ("TEXT", 3),
        ("XML", 4),
    ]
)


RequestPreservationType = Enum(
    value="RequestPreservationType",
    names=[
        ("None", 1),
        ("POST", 2),
        ("All", 3),
    ]
)


SameSiteTypeView = Enum(
    value="SameSiteTypeView",
    names=[
        ("Disabled", 1),
        ("Lax", 2),
        ("None", 3),
    ]
)


WebStorageType = Enum(
    value="WebStorageType",
    names=[
        ("SessionStorage", 1),
        ("LocalStorage", 2),
    ]
)
