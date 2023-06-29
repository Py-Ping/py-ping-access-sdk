from pingaccesssdk.model import Model
from enum import Enum


class UserView(Model):
    """A user.

    Attributes
    ----------
    email: str
        (sortable) The Administrative account's email.

    firstLogin: bool
        (sortable) The Administrative account's first login indicator.

    showTutorial: bool
        (sortable) The Administrative account's show tutorial indicator.

    slaAccepted: bool
        (sortable) The Administrative account's sla acceptance indicator.

    username: str
        (sortable) The Administrative users's username.

    """

    def __init__(self, username: str, email: str = None, firstLogin: bool = None, showTutorial: bool = None, slaAccepted: bool = None) -> None:
        self.email = email
        self.firstLogin = firstLogin
        self.showTutorial = showTutorial
        self.slaAccepted = slaAccepted
        self.username = username

    def _validate(self) -> bool:
        return any(x for x in ["username"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, UserView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.email, self.firstLogin, self.showTutorial, self.slaAccepted, self.username]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["email", "firstLogin", "showTutorial", "slaAccepted", "username"]:
                if k == "email":
                    valid_data[k] = str(v)
                if k == "firstLogin":
                    valid_data[k] = bool(v)
                if k == "showTutorial":
                    valid_data[k] = bool(v)
                if k == "slaAccepted":
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
            if k in ["email", "firstLogin", "showTutorial", "slaAccepted", "username"]:
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
