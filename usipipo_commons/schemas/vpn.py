from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..domain.enums.key_type import KeyType  # ← Changed from VpnType
from ..domain.enums.key_status import KeyStatus
from ..utils.validators import (
    VPN_KEY_NAME_MIN_LENGTH,
    VPN_KEY_NAME_MAX_LENGTH,
    VPN_KEY_NAME_PATTERN,
    get_vpn_key_name_validation_error,
)


class VpnKeyResponse(BaseModel):
    """Respuesta de clave VPN."""
    id: UUID
    user_id: UUID
    name: str
    key_type: KeyType  # ← Changed from vpn_type: VpnType
    status: KeyStatus
    config: Optional[str] = None
    external_id: Optional[str] = Field(None, description="External ID on VPN server (public key or Outline ID)")
    server_id: Optional[UUID] = Field(None, description="UUID of the VPN server")
    server_name: Optional[str] = Field(None, description="Name of the VPN server")
    created_at: datetime
    expires_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    data_used_gb: float = Field(ge=0)
    data_limit_gb: float = Field(ge=0)

    class Config:
        from_attributes = True


class CreateVpnKeyRequest(BaseModel):
    """Solicitud para crear clave VPN."""
    name: str = Field(
        ...,
        min_length=VPN_KEY_NAME_MIN_LENGTH,
        max_length=VPN_KEY_NAME_MAX_LENGTH,
        pattern=VPN_KEY_NAME_PATTERN,
        description="VPN key name (3-50 chars, alphanumeric, spaces, hyphens, underscores)",
    )
    key_type: KeyType  # ← Changed from vpn_type: VpnType
    data_limit_gb: float = Field(default=5.0, ge=0.1, le=100.0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate VPN key name and provide user-friendly error message."""
        error = get_vpn_key_name_validation_error(v)
        if error:
            raise ValueError(error)
        return v


class UpdateVpnKeyRequest(BaseModel):
    """Solicitud para actualizar clave VPN."""
    name: Optional[str] = Field(
        None,
        min_length=VPN_KEY_NAME_MIN_LENGTH,
        max_length=VPN_KEY_NAME_MAX_LENGTH,
        pattern=VPN_KEY_NAME_PATTERN,
        description="VPN key name (3-50 chars, alphanumeric, spaces, hyphens, underscores)",
    )
    data_limit_gb: Optional[float] = Field(None, ge=0.1, le=100.0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: Optional[str]) -> Optional[str]:
        """Validate VPN key name and provide user-friendly error message."""
        if v is None:
            return None
        error = get_vpn_key_name_validation_error(v)
        if error:
            raise ValueError(error)
        return v
