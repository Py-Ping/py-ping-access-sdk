from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.host_port_view import HostPortView
from pingaccesssdk.models.target_host_port_view import TargetHostPortView
from pingaccesssdk.enums import AuditLevel


class RedirectView(Model):
    """A Redirect.

    Attributes
    ----------
    id: str
        When creating a new Redirect, this is the ID for the Redirect. If not specified, an ID will be automatically assigned. When updating an existing Redirect, this field is ignored and the ID is determined by the path parameter.

    auditLevel: AuditLevel
        (sortable) Indicates if audit logging is enabled for the redirect.

    responseCode: int
        (sortable) The Redirect HTTP status code used by the response.

    source: HostPortView
        (sortable) The source host and port of the Redirect. When used as a sort key, results are sorted by the host.

    target: TargetHostPortView
        (sortable) The target host and port of the Redirect. When used as a sort key, results are sorted by the host.

    """

    def __init__(self, id: str = None, auditLevel: AuditLevel = None, responseCode: int = None, source: HostPortView = None, target: TargetHostPortView = None) -> None:
        self.id = id
        self.auditLevel = auditLevel
        self.responseCode = responseCode
        self.source = source
        self.target = target

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RedirectView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.auditLevel, self.responseCode, self.source, self.target]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "auditLevel", "responseCode", "source", "target"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "auditLevel":
                    valid_data[k] = AuditLevel[v]
                if k == "responseCode":
                    valid_data[k] = int(v)
                if k == "source":
                    valid_data[k] = HostPortView(**v) if v is not None else None
                if k == "target":
                    valid_data[k] = TargetHostPortView(**v) if v is not None else None

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "auditLevel", "responseCode", "source", "target"]:
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
