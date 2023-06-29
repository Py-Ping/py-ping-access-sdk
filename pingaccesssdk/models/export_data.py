from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.master_keys_view import MasterKeysView
from pingaccesssdk.models.json_web_key import JsonWebKey


class ExportData(Model):
    """A JSON backup file.

    Attributes
    ----------
    data: dict
        The entities being exported.

    encryptionKey: JsonWebKey
        The randomly-generated export encryption key to be included with the data.

    masterKeys: MasterKeysView
        The encrypted master keys.

    version: str
        The version of PingAccess that was exported.

    """

    def __init__(self, data: dict, encryptionKey: JsonWebKey, masterKeys: MasterKeysView, version: str) -> None:
        self.data = data
        self.encryptionKey = encryptionKey
        self.masterKeys = masterKeys
        self.version = version

    def _validate(self) -> bool:
        return any(x for x in ["data", "encryptionKey", "masterKeys", "version"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ExportData):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.data, self.encryptionKey, self.masterKeys, self.version]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["data", "encryptionKey", "masterKeys", "version"]:
                if k == "data":
                    valid_data[k] = dict(v) if v is not None else dict()
                if k == "encryptionKey":
                    valid_data[k] = JsonWebKey(**v) if v is not None else None
                if k == "masterKeys":
                    valid_data[k] = MasterKeysView(**v) if v is not None else None
                if k == "version":
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
            if k in ["data", "encryptionKey", "masterKeys", "version"]:
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
