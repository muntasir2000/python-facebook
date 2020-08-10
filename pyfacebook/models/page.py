"""
    These are models relative facebook page.

    Note:
        Some field which not common used has not include.
"""
from typing import Optional, List, Union
from dataclasses import dataclass, field

from .base import BaseModel
from .picture import CoverPhoto, ProfilePictureSource


class StoryTag(BaseModel):
    id: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)
    type: Optional[str] = field(default=None)
    offset: Optional[str] = field(default=None)
    length: Optional[str] = field(default=None)


@dataclass
class PageCategory(BaseModel):
    """
    A class representing the page category info.

    Refer: https://developers.facebook.com/docs/graph-api/reference/page-category/
    """

    id: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)
    api_enum: Optional[str] = field(default=None, repr=False)
    fb_page_categories: Optional[List["PageCategory"]] = field(default=None, repr=False)


@dataclass
class ContactAddress(BaseModel):
    """
    A class representing the mailing address info.

    Refer: https://developers.facebook.com/docs/graph-api/reference/mailing-address/
    """
    id: Optional[str] = field(default=None)
    city: Optional[str] = field(default=None)
    country: Optional[str] = field(default=None)
    postal_code: Optional[str] = field(default=None, repr=False)
    region: Optional[str] = field(default=None, repr=False)
    street1: Optional[str] = field(default=None, repr=False)
    street2: Optional[str] = field(default=None, repr=False)


@dataclass
class PageEngagement(BaseModel):
    """
    A class representing the page engagement info.

    Refer: https://developers.facebook.com/docs/graph-api/reference/engagement/
    """

    count: Optional[int] = field(default=None)
    count_string: Optional[str] = field(default=None, repr=False)
    count_string_with_like: Optional[str] = field(default=None, repr=False)
    count_string_without_like: Optional[str] = field(default=None, repr=False)
    social_sentence: Optional[str] = field(default=None)
    social_sentence_with_like: Optional[str] = field(default=None, repr=False)
    social_sentence_without_like: Optional[str] = field(default=None, repr=False)


@dataclass
class PageStartDate(BaseModel):
    """
    A class representing the page start date info.

    Refer: https://developers.facebook.com/docs/graph-api/reference/page-start-date/
    """
    day: Optional[int] = field(default=None)
    month: Optional[int] = field(default=None)
    year: Optional[int] = field(default=None)


@dataclass
class PageStartInfo(BaseModel):
    """
    A class representing the page start info.

    Refer: https://developers.facebook.com/docs/graph-api/reference/page-start-info/
    """
    date: Optional[PageStartDate] = field(default=None)
    type: Optional[str] = field(default=None)


@dataclass
class Page(BaseModel):
    """
    A class representing the page info.

    Refer: https://developers.facebook.com/docs/graph-api/reference/page/
    """

    id: str
    name: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)
    about: Optional[str] = field(default=None, repr=False)
    can_checkin: Optional[bool] = field(default=None, repr=False)
    category: Optional[str] = field(default=None, repr=False)
    category_list: Optional[List[PageCategory]] = field(default=None, repr=False)
    checkins: Optional[int] = field(default=None, repr=False)
    contact_address: Optional[str] = field(default=None, repr=False)
    cover: Optional[CoverPhoto] = field(default=None, repr=False)
    current_location: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)
    description_html: Optional[str] = field(default=None, repr=False)
    display_subtext: Optional[str] = field(default=None, repr=False)
    emails: Optional[List[str]] = field(default=None, repr=False)
    engagement: Optional[PageEngagement] = field(default=None, repr=False)
    fan_count: Optional[int] = field(default=None, repr=False)
    founded: Optional[str] = field(default=None, repr=False)
    general_info: Optional[str] = field(default=None, repr=False)
    global_brand_page_name: Optional[str] = field(default=None, repr=False)
    global_brand_root_id: Optional[str] = field(default=None, repr=False)
    link: Optional[str] = field(default=None, repr=False)
    name_with_location_descriptor: Optional[str] = field(default=None, repr=False)
    phone: Optional[str] = field(default=None, repr=False)
    picture: Optional[Union[dict, ProfilePictureSource]] = field(default=None, repr=False)
    rating_count: Optional[str] = field(default=None, repr=False)
    single_line_address: Optional[str] = field(default=None, repr=False)
    start_info: Optional[PageStartInfo] = field(default=None, repr=False)
    talking_about_count: Optional[int] = field(default=None, repr=False)
    verification_status: Optional[str] = field(default=None, repr=False)
    website: Optional[str] = field(default=None, repr=False)
    were_here_count: Optional[int] = field(default=None, repr=False)
    whatsapp_number: Optional[str] = field(default=None, repr=False)

    def __post_init__(self):
        if self.picture is not None and isinstance(self.picture, dict):
            picture = self.picture.get("data", {})
            self.picture = ProfilePictureSource.new_from_json_dict(picture)
