from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.hidden_field_view import HiddenFieldView
from pingaccesssdk.enums import CredentialsType


class OAuthClientCredentialsView(Model):
    """OAuth client credentials.

    Attributes
    ----------
    clientId: str
        Specify the client ID.

    clientSecret: HiddenFieldView
        Specify the client secret.

    credentialsType: CredentialsType
        Specify the credential type.

    keyPairId: int
        Specify the ID of a key pair to use for mutual TLS.

    """

    def __init__(self, clientId: str, clientSecret: HiddenFieldView = None, credentialsType: CredentialsType = None, keyPairId: int = None) -> None:
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.credentialsType = credentialsType
        self.keyPairId = keyPairId

    def _validate(self) -> bool:
        return any(x for x in ["clientId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OAuthClientCredentialsView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.clientId, self.clientSecret, self.credentialsType, self.keyPairId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["clientId", "clientSecret", "credentialsType", "keyPairId"]:
                if k == "clientId":
                    valid_data[k] = str(v)
                if k == "clientSecret":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None
                if k == "credentialsType":
                    valid_data[k] = CredentialsType[v]
                if k == "keyPairId":
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
            if k in ["clientId", "clientSecret", "credentialsType", "keyPairId"]:
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
