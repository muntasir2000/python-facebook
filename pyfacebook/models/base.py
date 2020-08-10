"""
    This is the base model
"""
from typing import Dict, Type, TypeVar
from dataclasses import dataclass

from dataclasses_json import dataclass_json, DataClassJsonMixin

A = TypeVar('A', bound=DataClassJsonMixin)


@dataclass_json
@dataclass
class BaseModel:

    @classmethod
    def new_from_json_dict(cls: Type[A], data: Dict, *, infer_missing=False) -> A:
        """
        :param data: A json dict which converted from facebook API.
        :param infer_missing: if set true, will let missing filed (not have default) to None.
        :return:
        """
        c = cls.from_dict(data, infer_missing=infer_missing)
        # save the origin data for other usage
        cls._json = data
        return c
