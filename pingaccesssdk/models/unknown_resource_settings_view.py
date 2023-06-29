from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.enums import AuditLevel
from pingaccesssdk.enums import ContentType
from pingaccesssdk.enums import UnknownResourceMode


class UnknownResourceSettingsView(Model):
    """Global settings for unknown resources.

    Attributes
    ----------
    agentDefaultCacheTTL: int
        The default agent resource cache TTL (in seconds) to be used for unknown resources when a request cannot be mapped to a known virtual host.

    agentDefaultMode: UnknownResourceMode
        The default agent mode, which determines whether agent requests for unknown resources should generate an error response or be allowed to pass through unfiltered. This default setting may be overridden by individual agents.

    auditLevel: AuditLevel
        Indicates if audit logging is enabled for unknown resources.

    errorContentType: ContentType
        The content type of the error response

    errorStatusCode: int
        The HTTP error response status code

    errorTemplateFile: str
        The name of the velocity template file to use for generating the error response body

    """

    def __init__(self, agentDefaultCacheTTL: int, agentDefaultMode: UnknownResourceMode, errorContentType: ContentType, errorStatusCode: int, errorTemplateFile: str, auditLevel: AuditLevel = None) -> None:
        self.agentDefaultCacheTTL = agentDefaultCacheTTL
        self.agentDefaultMode = agentDefaultMode
        self.auditLevel = auditLevel
        self.errorContentType = errorContentType
        self.errorStatusCode = errorStatusCode
        self.errorTemplateFile = errorTemplateFile

    def _validate(self) -> bool:
        return any(x for x in ["agentDefaultCacheTTL", "agentDefaultMode", "errorContentType", "errorStatusCode", "errorTemplateFile"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, UnknownResourceSettingsView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.agentDefaultCacheTTL, self.agentDefaultMode, self.auditLevel, self.errorContentType, self.errorStatusCode, self.errorTemplateFile]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["agentDefaultCacheTTL", "agentDefaultMode", "auditLevel", "errorContentType", "errorStatusCode", "errorTemplateFile"]:
                if k == "agentDefaultCacheTTL":
                    valid_data[k] = int(v)
                if k == "agentDefaultMode":
                    valid_data[k] = UnknownResourceMode[v]
                if k == "auditLevel":
                    valid_data[k] = AuditLevel[v]
                if k == "errorContentType":
                    valid_data[k] = ContentType[v]
                if k == "errorStatusCode":
                    valid_data[k] = int(v)
                if k == "errorTemplateFile":
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
            if k in ["agentDefaultCacheTTL", "agentDefaultMode", "auditLevel", "errorContentType", "errorStatusCode", "errorTemplateFile"]:
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
