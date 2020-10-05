
from attr import attrs, attrib
from typing import Dict, Optional

from .base import BaseModel


@attrs
class ObjectCreator(BaseModel):
    id = attrib(default=None, type=Optional[str], repr=False)
    name = attrib(default=None, type=Optional[str], repr=False)
