from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.hidden_field_view import HiddenFieldView


class SidebandSharedSecretConfigView(Model):
    """A configuration for sideband client shared secret.

    Attributes
    ----------
    secret: HiddenFieldView
        The permitted shared secret used to authenticate the sideband clients.

    sharedSecretHeaderName: str
        The name of the HTTP header presented in the request by the sideband client. The default value is "CLIENT-TOKEN".

    """

    def __init__(self, secret: HiddenFieldView = None, sharedSecretHeaderName: str = None) -> None:
        self.secret = secret
        self.sharedSecretHeaderName = sharedSecretHeaderName

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SidebandSharedSecretConfigView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.secret, self.sharedSecretHeaderName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["secret", "sharedSecretHeaderName"]:
                if k == "secret":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None
                if k == "sharedSecretHeaderName":
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
            if k in ["secret", "sharedSecretHeaderName"]:
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
