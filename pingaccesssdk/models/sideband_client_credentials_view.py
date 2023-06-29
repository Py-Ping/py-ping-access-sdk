from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.sideband_shared_secret_config_view import SidebandSharedSecretConfigView
from pingaccesssdk.enums import SidebandClientCredentialsType


class SidebandClientCredentialsView(Model):
    """The sideband client credentials.

    Attributes
    ----------
    created: str
        The created date of the credentials as the number of milliseconds since January 1, 1970, 00:00:00 GMT.

    credentialsType: SidebandClientCredentialsType
        Specify the credential type.

    sharedSecretConfig: SidebandSharedSecretConfigView
        Sideband client shared secret specific configuration.

    """

    def __init__(self, sharedSecretConfig: SidebandSharedSecretConfigView, created: str = None, credentialsType: SidebandClientCredentialsType = None) -> None:
        self.created = created
        self.credentialsType = credentialsType
        self.sharedSecretConfig = sharedSecretConfig

    def _validate(self) -> bool:
        return any(x for x in ["sharedSecretConfig"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SidebandClientCredentialsView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.created, self.credentialsType, self.sharedSecretConfig]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["created", "credentialsType", "sharedSecretConfig"]:
                if k == "created":
                    valid_data[k] = str(v)
                if k == "credentialsType":
                    valid_data[k] = SidebandClientCredentialsType[v]
                if k == "sharedSecretConfig":
                    valid_data[k] = SidebandSharedSecretConfigView(**v) if v is not None else None

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["created", "credentialsType", "sharedSecretConfig"]:
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
