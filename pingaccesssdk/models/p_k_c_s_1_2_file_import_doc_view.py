from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.hidden_field_view import HiddenFieldView


class PKCS12FileImportDocView(Model):
    """A PKCS#12 or PEM file import.

    Attributes
    ----------
    alias: str
        A unique alias name to identify the key pair. Special characters and spaces are allowed.

    chainCertificates: list
        An array of chain certificates.

    fileData: str
        Base-64 encoded PKCS12 or PEM file data. In BCFIPS mode, only PEM with PBES2 and AES or Triple DES encryption is accepted and 128-bit salt is required.

    hsmProviderId: int
        The HSM Provider ID. The default value is 0 indicating an HSM is not used for this key pair.

    password: HiddenFieldView
        The password used to protect the private key. In FIPS mode, the password must be at least 14 characters.

    """

    def __init__(self, alias: str, chainCertificates: list, fileData: str, hsmProviderId: int, password: HiddenFieldView) -> None:
        self.alias = alias
        self.chainCertificates = chainCertificates
        self.fileData = fileData
        self.hsmProviderId = hsmProviderId
        self.password = password

    def _validate(self) -> bool:
        return any(x for x in ["alias", "chainCertificates", "fileData", "hsmProviderId", "password"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PKCS12FileImportDocView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.alias, self.chainCertificates, self.fileData, self.hsmProviderId, self.password]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["alias", "chainCertificates", "fileData", "hsmProviderId", "password"]:
                if k == "alias":
                    valid_data[k] = str(v)
                if k == "chainCertificates":
                    valid_data[k] = [str(x) for x in v]
                if k == "fileData":
                    valid_data[k] = str(v)
                if k == "hsmProviderId":
                    valid_data[k] = int(v)
                if k == "password":
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
            if k in ["alias", "chainCertificates", "fileData", "hsmProviderId", "password"]:
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
