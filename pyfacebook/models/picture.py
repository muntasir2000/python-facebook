"""
   These some models for facebook picture entity.
"""
from dataclasses import dataclass, field
from typing import Optional

from .base import BaseModel


@dataclass
class CoverPhoto(BaseModel):
    """
    A class representing the cover photo info.

    Refer: https://developers.facebook.com/docs/graph-api/reference/cover-photo/
    """
    id: Optional[str] = field(default=None)
    source: Optional[str] = field(default=None)
    cover_id: Optional[str] = field(default=None, repr=False)
    offset_x: Optional[float] = field(default=None, repr=False)
    offset_y: Optional[float] = field(default=None, repr=False)


@dataclass
class ProfilePictureSource(BaseModel):
    """
    A class representing the profile picture source info

    Refer: https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/
    """

    height: Optional[str] = field(default=None)
    width: Optional[int] = field(default=None)
    url: Optional[int] = field(default=None)
    cache_key: Optional[str] = field(default=None, repr=False)
    is_silhouette: Optional[str] = field(default=None, repr=False)


@dataclass
class ImageSource(BaseModel):
    """
    A class representing the image source info.

    Structure will be {"height": 10, "width": 10, "src": "https://xxxx"}
    """
    height: Optional[int] = field(default=None)
    width: Optional[int] = field(default=None)
    src: Optional[str] = field(default=None)
