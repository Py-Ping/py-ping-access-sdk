from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.revocation_checking_view import RevocationCheckingView


class TrustedCertificateGroupView(Model):
    """A trusted certificate group.

    Attributes
    ----------
    id: int
        When creating a new TrustedCertificateGroup, this is the ID for the TrustedCertificateGroup. If not specified, an ID will be automatically assigned. When updating an existing TrustedCertificateGroup, this field is ignored and the ID is determined by the path parameter.

    certIds: list
        The IDs of the certificates that are in the trusted certificate group.

    ignoreAllCertificateErrors: bool
        (sortable) This field is read-only and is only set to true for the Trust Any certificate group.

    name: str
        (sortable) The name of the trusted certificate group.

    revocationChecking: RevocationCheckingView
        The configuration for client certificate revocation checking.

    skipCertificateDateCheck: bool
        (sortable) This field is true if certificates that have expired or are not yet valid but have passed the other certificate checks should be trusted.

    systemGroup: bool
        (sortable) This field is read-only and indicates the trusted certificate group cannot be modified.

    useJavaTrustStore: bool
        (sortable) This field is true if the certificates in the group should also include all certificates in the Java Trust Store.

    """

    def __init__(self, name: str, id: int = None, certIds: list = None, ignoreAllCertificateErrors: bool = None, revocationChecking: RevocationCheckingView = None, skipCertificateDateCheck: bool = None, systemGroup: bool = None, useJavaTrustStore: bool = None) -> None:
        self.id = id
        self.certIds = certIds
        self.ignoreAllCertificateErrors = ignoreAllCertificateErrors
        self.name = name
        self.revocationChecking = revocationChecking
        self.skipCertificateDateCheck = skipCertificateDateCheck
        self.systemGroup = systemGroup
        self.useJavaTrustStore = useJavaTrustStore

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, TrustedCertificateGroupView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.certIds, self.ignoreAllCertificateErrors, self.name, self.revocationChecking, self.skipCertificateDateCheck, self.systemGroup, self.useJavaTrustStore]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "certIds", "ignoreAllCertificateErrors", "name", "revocationChecking", "skipCertificateDateCheck", "systemGroup", "useJavaTrustStore"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "certIds":
                    valid_data[k] = [int(x) for x in v]
                if k == "ignoreAllCertificateErrors":
                    valid_data[k] = bool(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "revocationChecking":
                    valid_data[k] = RevocationCheckingView(**v) if v is not None else None
                if k == "skipCertificateDateCheck":
                    valid_data[k] = bool(v)
                if k == "systemGroup":
                    valid_data[k] = bool(v)
                if k == "useJavaTrustStore":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "certIds", "ignoreAllCertificateErrors", "name", "revocationChecking", "skipCertificateDateCheck", "systemGroup", "useJavaTrustStore"]:
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
