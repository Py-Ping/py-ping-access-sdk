from pingaccesssdk.model import Model
from enum import Enum


class ApiErrorView(Model):
    """An API error used by the PingAccess Administrative UI.

    Attributes
    ----------
    flash: list
        The flash message displayed in the UI.

    form: dict
        The specific errors related to the current form.

    """

    def __init__(self, flash: list, form: dict) -> None:
        self.flash = flash
        self.form = form

    def _validate(self) -> bool:
        return any(x for x in ["flash", "form"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ApiErrorView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.flash, self.form]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["flash", "form"]:
                if k == "flash":
                    valid_data[k] = [str(x) for x in v]
                if k == "form":
                    valid_data[k] = {str(x): [str(z) for z in y] for x, y in v.items()}

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["flash", "form"]:
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
