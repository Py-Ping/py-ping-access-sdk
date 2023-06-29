from pingaccesssdk.model import Model
from enum import Enum


class OAuthKeyManagementView(Model):
    """An OAuth key management configuration.

    Attributes
    ----------
    keyRollEnabled: bool
        This field is true if key rollover is enabled. When false, PingAccess will not rollover keys at the configured interval.

    keyRollPeriodInHours: int
        The interval (in hours) at which PingAccess will roll the keys. Key rollover updates keys at regular intervals to ensure the security of encrypted OAuth access tokens and encrypted OIDC id_tokens.

    signingAlgorithm: str
        The signing algorithm used when creating tokens for private key JWT OAuth client authentication. When set to null or empty, the algorithm will be selected from the OpenID Provider metadata.

    """

    def __init__(self, keyRollEnabled: bool = None, keyRollPeriodInHours: int = None, signingAlgorithm: str = None) -> None:
        self.keyRollEnabled = keyRollEnabled
        self.keyRollPeriodInHours = keyRollPeriodInHours
        self.signingAlgorithm = signingAlgorithm

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OAuthKeyManagementView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.keyRollEnabled, self.keyRollPeriodInHours, self.signingAlgorithm]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["keyRollEnabled", "keyRollPeriodInHours", "signingAlgorithm"]:
                if k == "keyRollEnabled":
                    valid_data[k] = bool(v)
                if k == "keyRollPeriodInHours":
                    valid_data[k] = int(v)
                if k == "signingAlgorithm":
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
            if k in ["keyRollEnabled", "keyRollPeriodInHours", "signingAlgorithm"]:
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
