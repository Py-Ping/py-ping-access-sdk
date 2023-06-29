from pingaccesssdk.model import Model
from enum import Enum


class KeyAlgorithm(Model):
    """A key algorithm.

    Attributes
    ----------
    defaultKeySize: int
        The default key size value to use.

    defaultSignatureAlgorithm: str
        The default signature algorithm to use.

    keySizes: list
        The list of available key sizes.

    name: str
        The algorithm name.

    signatureAlgorithms: list
        The list of available signature algorithms.

    """

    def __init__(self, defaultKeySize: int, defaultSignatureAlgorithm: str, keySizes: list, name: str, signatureAlgorithms: list) -> None:
        self.defaultKeySize = defaultKeySize
        self.defaultSignatureAlgorithm = defaultSignatureAlgorithm
        self.keySizes = keySizes
        self.name = name
        self.signatureAlgorithms = signatureAlgorithms

    def _validate(self) -> bool:
        return any(x for x in ["defaultKeySize", "defaultSignatureAlgorithm", "keySizes", "name", "signatureAlgorithms"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, KeyAlgorithm):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.defaultKeySize, self.defaultSignatureAlgorithm, self.keySizes, self.name, self.signatureAlgorithms]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["defaultKeySize", "defaultSignatureAlgorithm", "keySizes", "name", "signatureAlgorithms"]:
                if k == "defaultKeySize":
                    valid_data[k] = int(v)
                if k == "defaultSignatureAlgorithm":
                    valid_data[k] = str(v)
                if k == "keySizes":
                    valid_data[k] = [int(x) for x in v]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "signatureAlgorithms":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["defaultKeySize", "defaultSignatureAlgorithm", "keySizes", "name", "signatureAlgorithms"]:
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
