from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.enums import ListValueLocation


class IpMultiValueSourceView(Model):
    """Configuration for the IP source.

    Attributes
    ----------
    fallbackToLastHopIp: bool
        Indicator if the upstream IP address should be used as the client address if none of the expected headers is returned.

    headerNameList: list
        An array of header names used to identify the source IP address.

    listValueLocation: ListValueLocation
        The location in a matching header value list to use as the source.

    """

    def __init__(self, headerNameList: list, listValueLocation: ListValueLocation, fallbackToLastHopIp: bool = None) -> None:
        self.fallbackToLastHopIp = fallbackToLastHopIp
        self.headerNameList = headerNameList
        self.listValueLocation = listValueLocation

    def _validate(self) -> bool:
        return any(x for x in ["headerNameList", "listValueLocation"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IpMultiValueSourceView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.fallbackToLastHopIp, self.headerNameList, self.listValueLocation]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["fallbackToLastHopIp", "headerNameList", "listValueLocation"]:
                if k == "fallbackToLastHopIp":
                    valid_data[k] = bool(v)
                if k == "headerNameList":
                    valid_data[k] = [str(x) for x in v]
                if k == "listValueLocation":
                    valid_data[k] = ListValueLocation[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["fallbackToLastHopIp", "headerNameList", "listValueLocation"]:
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
