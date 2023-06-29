from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.request_matcher_view import RequestMatcherView
from pingaccesssdk.models.challenge_response_view import ChallengeResponseView


class ChallengeResponseMappingView(Model):
    """A mapping from an unauthenticated request to an authentication challenge response.

    Attributes
    ----------
    challengeResponse: ChallengeResponseView
        The response to produce when the matcher matches a request.

    requestMatcher: RequestMatcherView
        The request matcher used to identify the requests that should receive the corresponding challenge response.

    """

    def __init__(self, challengeResponse: ChallengeResponseView, requestMatcher: RequestMatcherView) -> None:
        self.challengeResponse = challengeResponse
        self.requestMatcher = requestMatcher

    def _validate(self) -> bool:
        return any(x for x in ["challengeResponse", "requestMatcher"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ChallengeResponseMappingView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.challengeResponse, self.requestMatcher]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["challengeResponse", "requestMatcher"]:
                if k == "challengeResponse":
                    valid_data[k] = ChallengeResponseView(**v) if v is not None else None
                if k == "requestMatcher":
                    valid_data[k] = RequestMatcherView(**v) if v is not None else None

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["challengeResponse", "requestMatcher"]:
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
