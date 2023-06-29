from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.acme_cert_status_view import AcmeCertStatusView


class AcmeCertificateRequestView(Model):
    """A reference to a Key Pair to be signed by the ACME protocol.

    Attributes
    ----------
    id: str
        When creating a new AcmeCertificateRequest, this is the ID for the AcmeCertificateRequest. If not specified, an ID will be automatically assigned. When updating an existing AcmeCertificateRequest, this field is ignored and the ID is determined by the path parameter.

    acmeAccountId: str
        The ID of the ACME Account to be used for the ACME protocol. This is read-only.

    acmeCertStatus: AcmeCertStatusView
        The status of the certificate.

    acmeServerId: str
        The ID of the ACME Server to be used for the ACME protocol. This is read-only.

    keyPairId: int
        The ID of the Key Pair for which a signed certificate will be requested.

    url: str
        The URL at the ACME server for the associated ACME order.

    """

    def __init__(self, keyPairId: int, id: str = None, acmeAccountId: str = None, acmeCertStatus: AcmeCertStatusView = None, acmeServerId: str = None, url: str = None) -> None:
        self.id = id
        self.acmeAccountId = acmeAccountId
        self.acmeCertStatus = acmeCertStatus
        self.acmeServerId = acmeServerId
        self.keyPairId = keyPairId
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in ["keyPairId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AcmeCertificateRequestView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.acmeAccountId, self.acmeCertStatus, self.acmeServerId, self.keyPairId, self.url]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "acmeAccountId", "acmeCertStatus", "acmeServerId", "keyPairId", "url"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "acmeAccountId":
                    valid_data[k] = str(v)
                if k == "acmeCertStatus":
                    valid_data[k] = AcmeCertStatusView(**v) if v is not None else None
                if k == "acmeServerId":
                    valid_data[k] = str(v)
                if k == "keyPairId":
                    valid_data[k] = int(v)
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
            if k in ["id", "acmeAccountId", "acmeCertStatus", "acmeServerId", "keyPairId", "url"]:
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
