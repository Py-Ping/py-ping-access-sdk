from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.hidden_field_view import HiddenFieldView
from pingaccesssdk.models.public_key_view import PublicKeyView


class AcmeAccountView(Model):
    """An ACME Account associated with a CA.

    Attributes
    ----------
    id: str
        When creating a new AcmeAccount, this is the ID for the AcmeAccount. If not specified, an ID will be automatically assigned. When updating an existing AcmeAccount, this field is ignored and the ID is determined by the path parameter.

    acmeServerId: str
        The associated ACME Server.

    keyAlgorithm: str
        The key algorithm used to generate a key.

    privateKey: HiddenFieldView
        The account's private key data.

    publicKey: PublicKeyView
        The account's public key data.

    url: str
        The URL the CA uses to reference the account.

    """

    def __init__(self, id: str = None, acmeServerId: str = None, keyAlgorithm: str = None, privateKey: HiddenFieldView = None, publicKey: PublicKeyView = None, url: str = None) -> None:
        self.id = id
        self.acmeServerId = acmeServerId
        self.keyAlgorithm = keyAlgorithm
        self.privateKey = privateKey
        self.publicKey = publicKey
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AcmeAccountView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.acmeServerId, self.keyAlgorithm, self.privateKey, self.publicKey, self.url]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "acmeServerId", "keyAlgorithm", "privateKey", "publicKey", "url"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "acmeServerId":
                    valid_data[k] = str(v)
                if k == "keyAlgorithm":
                    valid_data[k] = str(v)
                if k == "privateKey":
                    valid_data[k] = HiddenFieldView(**v) if v is not None else None
                if k == "publicKey":
                    valid_data[k] = PublicKeyView(**v) if v is not None else None
                if k == "url":
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
            if k in ["id", "acmeServerId", "keyAlgorithm", "privateKey", "publicKey", "url"]:
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
