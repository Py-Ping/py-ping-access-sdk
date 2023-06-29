from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.hidden_field_view import HiddenFieldView


class HttpClientProxyView(Model):
    """A proxy.

    Attributes
    ----------
    id: int
        When creating a new HttpClientProxy, this is the ID for the HttpClientProxy. If not specified, an ID will be automatically assigned. When updating an existing HttpClientProxy, this field is ignored and the ID is determined by the path parameter.

    description: str
        (sortable) A description of the proxy.

    host: str
        (sortable) The proxy host.

    name: str
        (sortable) The name of the proxy.

    password: HiddenFieldView
        (sortable) The password used for proxy authentication.

    port: int
        (sortable) The proxy port.

    requiresAuthentication: bool
        (sortable) True if the proxy requires authentication.

    username: str
        (sortable) The username used for proxy authentication.

    """

    def __init__(self, host: str, name: str, port: int, id: int = None, description: str = None, password: HiddenFieldView = None, requiresAuthentication: bool = None, username: str = None) -> None:
        self.id = id
        self.description = description
        self.host = host
        self.name = name
        self.password = password
        self.port = port
        self.requiresAuthentication = requiresAuthentication
        self.username = username

    def _validate(self) -> bool:
        return any(x for x in ["host", "name", "port"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, HttpClientProxyView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.description, self.host, self.name, self.password, self.port, self.requiresAuthentication, self.username]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "description", "host", "name", "password", "port", "requiresAuthentication", "username"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "host":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "password":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None
                if k == "port":
                    valid_data[k] = int(v)
                if k == "requiresAuthentication":
                    valid_data[k] = bool(v)
                if k == "username":
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
            if k in ["id", "description", "host", "name", "password", "port", "requiresAuthentication", "username"]:
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
