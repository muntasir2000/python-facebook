"""
    These are some models for access token.
"""
from dataclasses import dataclass, field
from typing import List, Optional

from .base import BaseModel


@dataclass
class AuthAccessToken(BaseModel):
    """
    A class representing the auth access token response.

    Refer: https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow#confirm
    """

    access_token: Optional[str] = field(default=None)
    token_type: Optional[str] = field(default=None)
    expires_in: Optional[int] = field(default=None)
    expires_at: Optional[int] = field(default=None, repr=False, compare=False)
    machine_id: Optional[str] = field(default=None, repr=False, compare=False)


@dataclass
class Error(BaseModel):
    """
    A class representing the access token request error.

    https://developers.facebook.com/docs/graph-api/reference/v5.0/debug_token#Fields
    """
    code: Optional[int] = field(default=None)
    message: Optional[str] = field(default=None)
    sub_code: Optional[int] = field(default=None, repr=False)


@dataclass
class Metadata(BaseModel):
    """
    A class representing the access token metadata.

    https://developers.facebook.com/docs/graph-api/reference/v5.0/debug_token#Fields
    """
    sso: Optional[str] = field(default=None)
    auth_type: Optional[str] = field(default=None, repr=False)
    auth_nonce: Optional[str] = field(default=None, repr=False)


@dataclass
class GranularScope(BaseModel):
    """
    A class representing the access token granular scope.

    https://developers.facebook.com/docs/graph-api/reference/v5.0/debug_token#Fields
    """
    scope: str
    target_ids: Optional[List[str]] = field(default=None, repr=False)


@dataclass
class AccessToken(BaseModel):
    """
    A class representing the access token.

    Refer: https://developers.facebook.com/docs/graph-api/reference/v5.0/debug_token
    """

    app_id: Optional[str] = field(default=None)
    application: Optional[str] = field(default=None)
    type: Optional[str] = field(default=None)
    error: Optional[Error] = field(default=None)
    expires_at: Optional[int] = field(default=None)
    data_access_expires_at: Optional[int] = field(default=None)
    is_valid: Optional[bool] = field(default=None)
    issued_at: Optional[int] = field(default=None)
    metadata: Optional[Metadata] = field(default=None)
    profile_id: Optional[str] = field(default=None)
    scopes: Optional[List[str]] = field(default=None)
    granular_scopes: Optional[List[GranularScope]] = field(default=None)
    user_id: Optional[str] = field(default=None)

    def __repr__(self) -> str:
        if self.error is None:
            return f"AccessToken(app_id={self.app_id},application={self.application},type={self.type})"
        else:
            return f"AccessToken(Error(code={self.error.code},message={self.error.message}))"
