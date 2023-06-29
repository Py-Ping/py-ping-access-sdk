from pingaccesssdk.model import Model
from enum import Enum


class RevocationCheckingView(Model):
    """The client certificate revocation checking configuration.

    Attributes
    ----------
    crlChecking: bool
        This field is true if CRL client certificate revocation checking is enabled.

    denyRevocationStatusUnknown: bool
        This field is true if client certificates should be denied when the revocation status cannot be determined.

    ocsp: bool
        This field is true if OCSP client certificate revocation checking is enabled.

    skipTrustAnchors: bool
        When set to true, PA will skip validation of any certificates configured in the trusted certificate group as well as their subsequent chain of issuers when trusted certificates are found in the client certificate chain.

    supportDisorderedChain: bool
        When set to true, PA can validate client certificate chains that are not in the standard order of leaf -> intermediate(s) -> root. When false, validation may fail on client certificate chains that are not in the standard order.

    """

    def __init__(self, crlChecking: bool = None, denyRevocationStatusUnknown: bool = None, ocsp: bool = None, skipTrustAnchors: bool = None, supportDisorderedChain: bool = None) -> None:
        self.crlChecking = crlChecking
        self.denyRevocationStatusUnknown = denyRevocationStatusUnknown
        self.ocsp = ocsp
        self.skipTrustAnchors = skipTrustAnchors
        self.supportDisorderedChain = supportDisorderedChain

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RevocationCheckingView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.crlChecking, self.denyRevocationStatusUnknown, self.ocsp, self.skipTrustAnchors, self.supportDisorderedChain]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["crlChecking", "denyRevocationStatusUnknown", "ocsp", "skipTrustAnchors", "supportDisorderedChain"]:
                if k == "crlChecking":
                    valid_data[k] = bool(v)
                if k == "denyRevocationStatusUnknown":
                    valid_data[k] = bool(v)
                if k == "ocsp":
                    valid_data[k] = bool(v)
                if k == "skipTrustAnchors":
                    valid_data[k] = bool(v)
                if k == "supportDisorderedChain":
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
            if k in ["crlChecking", "denyRevocationStatusUnknown", "ocsp", "skipTrustAnchors", "supportDisorderedChain"]:
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
