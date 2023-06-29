from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.general_name import GeneralName


class NewKeyPairConfigView(Model):
    """A new key pair.

    Attributes
    ----------
    id: int
        The ID for the key pair. If not specified, an ID will be automatically assigned.

    alias: str
        A unique alias name to identify the key pair. Special characters and spaces are allowed.

    city: str
        The city or other primary location (L) where the company operates.

    commonName: str
        The common name (CN) identifying the certificate.

    country: str
        The country (C) where the company is based, using two capital letters.

    hsmProviderId: int
        The HSM Provider ID. The default value is 0 indicating an HSM is not used for this key pair.

    keyAlgorithm: str
        The key algorithm to use to generate a key.

    keySize: int
        The number of bits used in the key.  Choices depend on selected key algorithm.

    organization: str
        The organization (O) or company name creating the certificate.

    organizationUnit: str
        The specific unit within the organization (OU).

    signatureAlgorithm: str
        The Signature Algorithm to use for the key.

    state: str
        The state (ST) or other political unit encompassing the location.

    subjectAlternativeNames: list
        Any additional DNS names or IP addresses that are valid for this certificate.

    validDays: int
        The number of days the certificate is valid.

    """

    def __init__(self, alias: str, city: str, commonName: str, country: str, hsmProviderId: int, keyAlgorithm: str, keySize: int, organization: str, organizationUnit: str, state: str, validDays: int, id: int = None, signatureAlgorithm: str = None, subjectAlternativeNames: list = None) -> None:
        self.id = id
        self.alias = alias
        self.city = city
        self.commonName = commonName
        self.country = country
        self.hsmProviderId = hsmProviderId
        self.keyAlgorithm = keyAlgorithm
        self.keySize = keySize
        self.organization = organization
        self.organizationUnit = organizationUnit
        self.signatureAlgorithm = signatureAlgorithm
        self.state = state
        self.subjectAlternativeNames = subjectAlternativeNames
        self.validDays = validDays

    def _validate(self) -> bool:
        return any(x for x in ["alias", "city", "commonName", "country", "hsmProviderId", "keyAlgorithm", "keySize", "organization", "organizationUnit", "state", "validDays"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, NewKeyPairConfigView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.alias, self.city, self.commonName, self.country, self.hsmProviderId, self.keyAlgorithm, self.keySize, self.organization, self.organizationUnit, self.signatureAlgorithm, self.state, self.subjectAlternativeNames, self.validDays]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "alias", "city", "commonName", "country", "hsmProviderId", "keyAlgorithm", "keySize", "organization", "organizationUnit", "signatureAlgorithm", "state", "subjectAlternativeNames", "validDays"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "alias":
                    valid_data[k] = str(v)
                if k == "city":
                    valid_data[k] = str(v)
                if k == "commonName":
                    valid_data[k] = str(v)
                if k == "country":
                    valid_data[k] = str(v)
                if k == "hsmProviderId":
                    valid_data[k] = int(v)
                if k == "keyAlgorithm":
                    valid_data[k] = str(v)
                if k == "keySize":
                    valid_data[k] = int(v)
                if k == "organization":
                    valid_data[k] = str(v)
                if k == "organizationUnit":
                    valid_data[k] = str(v)
                if k == "signatureAlgorithm":
                    valid_data[k] = str(v)
                if k == "state":
                    valid_data[k] = str(v)
                if k == "subjectAlternativeNames":
                    valid_data[k] = [GeneralName(**x) if x is not None else None for x in v or []]
                if k == "validDays":
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
            if k in ["id", "alias", "city", "commonName", "country", "hsmProviderId", "keyAlgorithm", "keySize", "organization", "organizationUnit", "signatureAlgorithm", "state", "subjectAlternativeNames", "validDays"]:
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
