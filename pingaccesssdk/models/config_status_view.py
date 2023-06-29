from pingaccesssdk.model import Model
from enum import Enum
from pingaccesssdk.models.api_error_view import ApiErrorView
from pingaccesssdk.models.json_node import JsonNode


class ConfigStatusView(Model):
    """An import or export configuration.

    Attributes
    ----------
    id: int
        The id of the configuration workflow.

    apiErrorView: ApiErrorView
        The API error for import or export, if there is an error. When failFast=false this will collect all API errors encountered from the import configuration.

    currentEntity: JsonNode
        The current entity being imported or exported.

    status: str
        The status of the configuration import or export.

    totalEntities: int
        The total number of entities being imported or exported.

    warnings: set
        The API warnings for import or export, if there are any warnings.

    """

    def __init__(self, warnings: set, id: int = None, apiErrorView: ApiErrorView = None, currentEntity: JsonNode = None, status: str = None, totalEntities: int = None) -> None:
        self.id = id
        self.apiErrorView = apiErrorView
        self.currentEntity = currentEntity
        self.status = status
        self.totalEntities = totalEntities
        self.warnings = warnings

    def _validate(self) -> bool:
        return any(x for x in ["warnings"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigStatusView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.apiErrorView, self.currentEntity, self.status, self.totalEntities, self.warnings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "apiErrorView", "currentEntity", "status", "totalEntities", "warnings"]:
                if k == "id":
                    valid_data[k] = int(v)
                if k == "apiErrorView":
                    valid_data[k] = ApiErrorView(**v) if v is not None else None
                if k == "currentEntity":
                    valid_data[k] = JsonNode(**v) if v is not None else None
                if k == "status":
                    valid_data[k] = str(v)
                if k == "totalEntities":
                    valid_data[k] = int(v)
                if k == "warnings":
                    valid_data[k] = set({str(x) for x in v})

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "apiErrorView", "currentEntity", "status", "totalEntities", "warnings"]:
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
