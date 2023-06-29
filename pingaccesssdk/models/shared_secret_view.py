from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.hidden_field_view import HiddenFieldView


class SharedSecretView(Model):
    """A shared secret.

    Attributes
    ----------
    id: int
        When creating a new SharedSecret, this is the ID for the SharedSecret. If not specified, an ID will be automatically assigned. When updating an existing SharedSecret, this field is ignored and the ID is determined by the path parameter.

    created: str
        (sortable) The created date of the secret as the number of milliseconds since January 1, 1970, 00:00:00 GMT.

    secret: HiddenFieldView
        (sortable) The generated shared secrets used to authenticate the agents.

    """

    def __init__(self, secret: HiddenFieldView, id: int = None, created: str = None) -> None:
        self.id = id
        self.created = created
        self.secret = secret

    def _validate(self) -> bool:
        return any(x for x in ["secret"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SharedSecretView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.created, self.secret]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "created", "secret"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "created":
                    valid_data[k] = str(v)
                if k == "secret":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "created", "secret"]:
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
