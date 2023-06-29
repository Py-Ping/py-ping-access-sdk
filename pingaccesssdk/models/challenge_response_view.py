from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.challenge_response_filter_view import ChallengeResponseFilterView
from pingaccesssdk.models.challenge_response_generator_view import ChallengeResponseGeneratorView


class ChallengeResponseView(Model):
    """An authentication challenge response.

    Attributes
    ----------
    filter: ChallengeResponseFilterView
        The response filter that operates on the challenge response headers from the generator response.

    generator: ChallengeResponseGeneratorView
        The response generator that produces the baseline authentication challenge response.

    """

    def __init__(self, generator: ChallengeResponseGeneratorView, filter: ChallengeResponseFilterView = None) -> None:
        self.filter = filter
        self.generator = generator

    def _validate(self) -> bool:
        return any(x for x in ["generator"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ChallengeResponseView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.filter, self.generator]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["filter", "generator"]:
                if k == "filter":
                    valid_data[k] = ChallengeResponseFilterView(**v) if v is not None else None
                if k == "generator":
                    valid_data[k] = ChallengeResponseGeneratorView(**v) if v is not None else None

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["filter", "generator"]:
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
