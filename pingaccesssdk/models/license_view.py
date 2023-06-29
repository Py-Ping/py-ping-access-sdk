from pingaccesssdk.model import Model
from enum import Enum


class LicenseView(Model):
    """A Ping Identity license.

    Attributes
    ----------
    id: int
        The ID value from the license file.

    enforcementType: int
        The enforcement type value from the license file.

    expirationDate: str
        The expiration date value from the license file.

    issueDate: str
        The issue date value from the license file.

    maxApplications: int
        The maximum number of applications from the license file.

    name: str
        The name value from the license file.  Name is required if the organization value is not set.

    organization: str
        The organization value from the license file.

    product: str
        The Ping Identity product value from the license file.

    tier: str
        The tier value from the license file.

    version: str
        The Ping Identity product version from the license file.

    """

    def __init__(self, id: int, enforcementType: int, expirationDate: str, issueDate: str, maxApplications: int, name: str, organization: str, product: str, tier: str, version: str) -> None:
        self.id = id
        self.enforcementType = enforcementType
        self.expirationDate = expirationDate
        self.issueDate = issueDate
        self.maxApplications = maxApplications
        self.name = name
        self.organization = organization
        self.product = product
        self.tier = tier
        self.version = version

    def _validate(self) -> bool:
        return any(x for x in ["id", "enforcementType", "expirationDate", "issueDate", "maxApplications", "name", "organization", "product", "tier", "version"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LicenseView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.enforcementType, self.expirationDate, self.issueDate, self.maxApplications, self.name, self.organization, self.product, self.tier, self.version]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "enforcementType", "expirationDate", "issueDate", "maxApplications", "name", "organization", "product", "tier", "version"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "enforcementType":
                    valid_data[k] = int(v)
                if k == "expirationDate":
                    valid_data[k] = str(v)
                if k == "issueDate":
                    valid_data[k] = str(v)
                if k == "maxApplications":
                    valid_data[k] = int(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "organization":
                    valid_data[k] = str(v)
                if k == "product":
                    valid_data[k] = str(v)
                if k == "tier":
                    valid_data[k] = str(v)
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
            if k in ["id", "enforcementType", "expirationDate", "issueDate", "maxApplications", "name", "organization", "product", "tier", "version"]:
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
