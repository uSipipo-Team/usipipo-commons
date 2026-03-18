from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..enums.vpn_type import VpnType
from ..enums.key_status import KeyStatus


@dataclass
class VpnKey:
    """Entidad de clave VPN compartida."""
    id: UUID
    user_id: UUID
    name: str
    vpn_type: VpnType
    status: KeyStatus
    config: Optional[str]
    created_at: datetime
    expires_at: Optional[datetime]
    last_used_at: Optional[datetime]
    data_used_gb: float
    data_limit_gb: float

    def to_dict(self) -> dict:
        """Convierte a diccionario para serialización."""
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "name": self.name,
            "vpn_type": self.vpn_type.value,
            "status": self.status.value,
            "config": self.config,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "last_used_at": self.last_used_at.isoformat() if self.last_used_at else None,
            "data_used_gb": self.data_used_gb,
            "data_limit_gb": self.data_limit_gb,
        }
