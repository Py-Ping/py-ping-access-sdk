from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.enums import AuditLevel


class GlobalUnprotectedResourceView(Model):
    """A global unprotected resource.

    Attributes
    ----------
    id: str
        When creating a new GlobalUnprotectedResource, this is the ID for the GlobalUnprotectedResource. If not specified, an ID will be automatically assigned. When updating an existing GlobalUnprotectedResource, this field is ignored and the ID is determined by the path parameter.

    auditLevel: AuditLevel
        (sortable) Indicates if audit logging is enabled for the global unprotected resource.

    description: str
        (sortable) A description of the global unprotected resource.

    enabled: bool
        (sortable) True if the global resource is enabled.

    name: str
        (sortable) The name of the global unprotected resource.

    wildcardPath: str
        A path for the global unprotected resource.

    """

    def __init__(self, name: str, wildcardPath: str, id: str = None, auditLevel: AuditLevel = None, description: str = None, enabled: bool = None) -> None:
        self.id = id
        self.auditLevel = auditLevel
        self.description = description
        self.enabled = enabled
        self.name = name
        self.wildcardPath = wildcardPath

    def _validate(self) -> bool:
        return any(x for x in ["name", "wildcardPath"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, GlobalUnprotectedResourceView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.auditLevel, self.description, self.enabled, self.name, self.wildcardPath]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "auditLevel", "description", "enabled", "name", "wildcardPath"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "auditLevel":
                    valid_data[k] = AuditLevel[v]
                if k == "description":
                    valid_data[k] = str(v)
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "wildcardPath":
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
            if k in ["id", "auditLevel", "description", "enabled", "name", "wildcardPath"]:
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
