from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.challenge_response_view import ChallengeResponseView
from pingaccesssdk.models.challenge_response_mapping_view import ChallengeResponseMappingView


class AuthenticationChallengePolicyView(Model):
    """An authentication challenge policy.

    Attributes
    ----------
    id: str
        The UUID for the authentication challenge policy. If not specified during creation, an ID will be automatically be assigned. When updating an existing authentication challenge policy, this field is ignored and the ID is determined from the URL path parameter.

    challengeResponseChain: list
        An array of challenge response mappings, ordered by the precedence of each mapping. When no challengeResponseChain is needed for the policy, this field must be set to an empty array.

    defaultChallengeResponse: ChallengeResponseView
        The challenge response sent to the client when the challenge response chain does not produce a response.

    description: str
        (sortable) A description of the authentication challenge policy. The number of characters in the description is limited to 1000.

    name: str
        (sortable) The name of this authentication challenge policy. The number of characters in the name is limited to 64.

    system: bool
        (sortable) This field is read-only and indicates this authentication challenge policy cannot be modified.

    """

    def __init__(self, challengeResponseChain: list, defaultChallengeResponse: ChallengeResponseView, name: str, id: str = None, description: str = None, system: bool = None) -> None:
        self.id = id
        self.challengeResponseChain = challengeResponseChain
        self.defaultChallengeResponse = defaultChallengeResponse
        self.description = description
        self.name = name
        self.system = system

    def _validate(self) -> bool:
        return any(x for x in ["challengeResponseChain", "defaultChallengeResponse", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationChallengePolicyView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.challengeResponseChain, self.defaultChallengeResponse, self.description, self.name, self.system]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "challengeResponseChain", "defaultChallengeResponse", "description", "name", "system"]:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "challengeResponseChain":
                    valid_data[k] = [ChallengeResponseMappingView(**x) if x is not None else None for x in v or []]
                if k == "defaultChallengeResponse":
                    valid_data[k] = ChallengeResponseView(**v) if v is not None else None
                if k == "description":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "system":
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
            if k in ["id", "challengeResponseChain", "defaultChallengeResponse", "description", "name", "system"]:
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
