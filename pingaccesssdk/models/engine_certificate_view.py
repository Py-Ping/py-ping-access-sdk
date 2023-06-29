from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.general_name import GeneralName
from pingaccesssdk.enums import CertStatus


class EngineCertificateView(Model):
    """An engine certificate.

    Attributes
    ----------
    id: int
        The id for the engine certificate.

    alias: str
        (sortable) The alias for the engine certificate.

    chainCertificate: bool
        A flag indicating whether the engine certificate is a chain certificate.

    expires: int
        (sortable) The date at which the engine certificate expires as the number of milliseconds since January 1, 1970, 00:00:00 GMT.

    issuerDn: str
        (sortable) The issuer DN for the engine certificate.

    keyPair: bool
        A flag indicating whether the engine certificate is a key pair.

    md5sum: str
        The MD5 checksum of the engine certificate. The value will be set to "" when in FIPS mode.

    serialNumber: str
        (sortable) The Serial Number for the engine certificate.

    sha1sum: str
        The SHA1 checksum of the engine certificate.

    sha256sum: str
        The SHA256 checksum of the engine certificate.

    signatureAlgorithm: str
        (sortable) The Signature Algorithm used by the engine certificate.

    status: CertStatus
        A high-level status for the engine certificate.

    subjectAlternativeNames: list
        A collection of subject alternative names for the engine certificate.

    subjectCn: str
        (sortable) The common name (CN) identifying the certificate.

    subjectDn: str
        (sortable) The Subject DN for the engine certificate.

    trustedCertificate: bool
        A flag indicating whether the engine certificate is a trusted certificate.

    validFrom: int
        (sortable) The date at which the engine certificate is valid from as the number of milliseconds since January 1, 1970, 00:00:00 GMT.

    """

    def __init__(self, alias: str, chainCertificate: bool, issuerDn: str, keyPair: bool, md5sum: str, serialNumber: str, sha1sum: str, sha256sum: str, signatureAlgorithm: str, status: CertStatus, subjectDn: str, trustedCertificate: bool, id: int = None, expires: int = None, subjectAlternativeNames: list = None, subjectCn: str = None, validFrom: int = None) -> None:
        self.id = id
        self.alias = alias
        self.chainCertificate = chainCertificate
        self.expires = expires
        self.issuerDn = issuerDn
        self.keyPair = keyPair
        self.md5sum = md5sum
        self.serialNumber = serialNumber
        self.sha1sum = sha1sum
        self.sha256sum = sha256sum
        self.signatureAlgorithm = signatureAlgorithm
        self.status = status
        self.subjectAlternativeNames = subjectAlternativeNames
        self.subjectCn = subjectCn
        self.subjectDn = subjectDn
        self.trustedCertificate = trustedCertificate
        self.validFrom = validFrom

    def _validate(self) -> bool:
        return any(x for x in ["alias", "chainCertificate", "issuerDn", "keyPair", "md5sum", "serialNumber", "sha1sum", "sha256sum", "signatureAlgorithm", "status", "subjectDn", "trustedCertificate"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, EngineCertificateView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.alias, self.chainCertificate, self.expires, self.issuerDn, self.keyPair, self.md5sum, self.serialNumber, self.sha1sum, self.sha256sum, self.signatureAlgorithm, self.status, self.subjectAlternativeNames, self.subjectCn, self.subjectDn, self.trustedCertificate, self.validFrom]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "alias", "chainCertificate", "expires", "issuerDn", "keyPair", "md5sum", "serialNumber", "sha1sum", "sha256sum", "signatureAlgorithm", "status", "subjectAlternativeNames", "subjectCn", "subjectDn", "trustedCertificate", "validFrom"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "alias":
                    valid_data[k] = str(v)
                if k == "chainCertificate":
                    valid_data[k] = bool(v)
                if k == "expires":
                    valid_data[k] = int(v)
                if k == "issuerDn":
                    valid_data[k] = str(v)
                if k == "keyPair":
                    valid_data[k] = bool(v)
                if k == "md5sum":
                    valid_data[k] = str(v)
                if k == "serialNumber":
                    valid_data[k] = str(v)
                if k == "sha1sum":
                    valid_data[k] = str(v)
                if k == "sha256sum":
                    valid_data[k] = str(v)
                if k == "signatureAlgorithm":
                    valid_data[k] = str(v)
                if k == "status":
                    valid_data[k] = CertStatus[v]
                if k == "subjectAlternativeNames":
                    valid_data[k] = [GeneralName(**x) if x is not None else None for x in v or []]
                if k == "subjectCn":
                    valid_data[k] = str(v)
                if k == "subjectDn":
                    valid_data[k] = str(v)
                if k == "trustedCertificate":
                    valid_data[k] = bool(v)
                if k == "validFrom":
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
            if k in ["id", "alias", "chainCertificate", "expires", "issuerDn", "keyPair", "md5sum", "serialNumber", "sha1sum", "sha256sum", "signatureAlgorithm", "status", "subjectAlternativeNames", "subjectCn", "subjectDn", "trustedCertificate", "validFrom"]:
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
