from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.public_key import PublicKey
from pingaccesssdk.models.key import Key


class JsonWebKey(Model):
    """A JSON Web Key.

    Attributes
    ----------
    algorithm: str
        The algorithm name.

    key: Key
        The key.

    keyId: str
        The key id.

    keyOps: list
        The list of key operations.

    keyType: str
        The key type.

    publicKey: PublicKey
        The public key.

    use: str
        The intended use of the key.

    """

    def __init__(self, algorithm: str, key: Key, keyId: str, keyOps: list, keyType: str, publicKey: PublicKey, use: str) -> None:
        self.algorithm = algorithm
        self.key = key
        self.keyId = keyId
        self.keyOps = keyOps
        self.keyType = keyType
        self.publicKey = publicKey
        self.use = use

    def _validate(self) -> bool:
        return any(x for x in ["algorithm", "key", "keyId", "keyOps", "keyType", "publicKey", "use"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, JsonWebKey):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.algorithm, self.key, self.keyId, self.keyOps, self.keyType, self.publicKey, self.use]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["algorithm", "key", "keyId", "keyOps", "keyType", "publicKey", "use"]:
                if k == "algorithm":
                    valid_data[k] = str(v)
                if k == "key":
                    valid_data[k] = Key(**v) if v is not None else None
                if k == "keyId":
                    valid_data[k] = str(v)
                if k == "keyOps":
                    valid_data[k] = [str(x) for x in v]
                if k == "keyType":
                    valid_data[k] = str(v)
                if k == "publicKey":
                    valid_data[k] = PublicKey(**v) if v is not None else None
                if k == "use":
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
            if k in ["algorithm", "key", "keyId", "keyOps", "keyType", "publicKey", "use"]:
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
