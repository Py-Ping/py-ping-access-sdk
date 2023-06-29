from pingaccesssdk.model import Model
from enum import Enum


class HttpsListenerView(Model):
    """An HTTPS listener.

    Attributes
    ----------
    keyPairId: int
        The ID of the default key pair used by the HTTPS listener.

    name: str
        (sortable) The name of the HTTPS listener.

    restartRequired: bool
        Indicates whether an admin or engine restart is required to update the HTTPS listener. Cannot be True for the ENGINE listener.

    useServerCipherSuiteOrder: bool
        (sortable) Enable server cipher suite ordering for the HTTPS listener.

    id: int
        The ID of the HTTPS listener.

    """

    def __init__(self, keyPairId: int, name: str, restartRequired: bool, useServerCipherSuiteOrder: bool, id: int = None) -> None:
        self.keyPairId = keyPairId
        self.name = name
        self.restartRequired = restartRequired
        self.useServerCipherSuiteOrder = useServerCipherSuiteOrder
        self.id = id

    def _validate(self) -> bool:
        return any(x for x in ["keyPairId", "name", "restartRequired", "useServerCipherSuiteOrder"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, HttpsListenerView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.keyPairId, self.name, self.restartRequired, self.useServerCipherSuiteOrder, self.id]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["keyPairId", "name", "restartRequired", "useServerCipherSuiteOrder", "id"]:
                if k == "keyPairId":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "restartRequired":
                    valid_data[k] = bool(v)
                if k == "useServerCipherSuiteOrder":
                    valid_data[k] = bool(v)
                if k == "id":
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
            if k in ["keyPairId", "name", "restartRequired", "useServerCipherSuiteOrder", "id"]:
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
