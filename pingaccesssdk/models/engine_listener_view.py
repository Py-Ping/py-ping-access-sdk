from pingaccesssdk.model import Model
from enum import Enum


class EngineListenerView(Model):
    """An engine listener.

    Attributes
    ----------
    id: int
        When creating a new EngineListener, this is the ID for the EngineListener. If not specified, an ID will be automatically assigned. When updating an existing EngineListener, this field is ignored and the ID is determined by the path parameter.

    name: str
        (sortable) The name of the engine listener.

    port: int
        (sortable) The port the engine listener listens on.

    secure: bool
        (sortable) Indicator if the engine listener should listen to HTTPS connections.

    trustedCertificateGroupId: int
        Trusted Certificate Group assigned to engine listener for client certificate authentication.

    """

    def __init__(self, name: str, port: int, id: int = None, secure: bool = None, trustedCertificateGroupId: int = None) -> None:
        self.id = id
        self.name = name
        self.port = port
        self.secure = secure
        self.trustedCertificateGroupId = trustedCertificateGroupId

    def _validate(self) -> bool:
        return any(x for x in ["name", "port"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, EngineListenerView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.port, self.secure, self.trustedCertificateGroupId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "port", "secure", "trustedCertificateGroupId"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "port":
                    valid_data[k] = int(v)
                if k == "secure":
                    valid_data[k] = bool(v)
                if k == "trustedCertificateGroupId":
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
            if k in ["id", "name", "port", "secure", "trustedCertificateGroupId"]:
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
