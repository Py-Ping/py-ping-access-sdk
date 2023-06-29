from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.https_listener_view import HttpsListenerView


class HttpsListenersView(Model):
    """A collection of HTTPS listeners.

    Attributes
    ----------
    items: list
        An array of HTTPS listeners.

    id: int
        The ID of the HTTPS listener.

    """

    def __init__(self, items: list, id: int = None) -> None:
        self.items = items
        self.id = id

    def _validate(self) -> bool:
        return any(x for x in ["items"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, HttpsListenersView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.items, self.id]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["items", "id"]:
                if k == "items":
                    valid_data[k] = [HttpsListenerView(**x) if x is not None else None for x in v or []]
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
            if k in ["items", "id"]:
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
