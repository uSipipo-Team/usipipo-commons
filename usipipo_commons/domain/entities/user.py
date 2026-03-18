from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class User:
    """Entidad de usuario compartida."""
    id: UUID
    telegram_id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_admin: bool
    created_at: datetime
    updated_at: datetime
    balance_gb: float
    total_purchased_gb: float
    referral_code: str
    referred_by: Optional[UUID]

    def to_dict(self) -> dict:
        """Convierte a diccionario para serialización."""
        return {
            "id": str(self.id),
            "telegram_id": self.telegram_id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "balance_gb": self.balance_gb,
            "total_purchased_gb": self.total_purchased_gb,
            "referral_code": self.referral_code,
            "referred_by": str(self.referred_by) if self.referred_by else None,
        }
