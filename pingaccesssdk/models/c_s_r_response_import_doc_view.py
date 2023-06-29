from pingaccesssdk.model import Model
from enum import Enum


class CSRResponseImportDocView(Model):
    """A CSR response.

    Attributes
    ----------
    chainCertificates: list
        A list of base64-encoded certificates to add to the key pair certificate chain.

    fileData: str
        The CSR response data.

    hsmProviderId: int
        The HSM Provider ID. The default value is 0 indicating an HSM is not used for this key pair.

    trustedCertGroupId: int
        The ID of the trusted certificate group associated with the CSR response.

    """

    def __init__(self, chainCertificates: list, fileData: str, hsmProviderId: int, trustedCertGroupId: int) -> None:
        self.chainCertificates = chainCertificates
        self.fileData = fileData
        self.hsmProviderId = hsmProviderId
        self.trustedCertGroupId = trustedCertGroupId

    def _validate(self) -> bool:
        return any(x for x in ["chainCertificates", "fileData", "hsmProviderId", "trustedCertGroupId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, CSRResponseImportDocView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.chainCertificates, self.fileData, self.hsmProviderId, self.trustedCertGroupId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["chainCertificates", "fileData", "hsmProviderId", "trustedCertGroupId"]:
                if k == "chainCertificates":
                    valid_data[k] = [str(x) for x in v]
                if k == "fileData":
                    valid_data[k] = str(v)
                if k == "hsmProviderId":
                    valid_data[k] = int(v)
                if k == "trustedCertGroupId":
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
            if k in ["chainCertificates", "fileData", "hsmProviderId", "trustedCertGroupId"]:
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
