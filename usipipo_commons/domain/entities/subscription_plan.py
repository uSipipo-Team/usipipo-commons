"""Subscription plan entity."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel

from usipipo_commons.domain.enums.plan_type import PlanType


class SubscriptionPlan(BaseModel):
    """Entidad de plan de suscripción."""

    user_id: int
    plan_type: PlanType
    stars_paid: int
    payment_id: str
    starts_at: datetime
    expires_at: datetime
    is_active: bool = True

    @property
    def is_expired(self) -> bool:
        """Verifica si la suscripción ha expirado."""
        return datetime.now(self.starts_at.tzinfo) > self.expires_at

    def to_dict(self) -> dict[str, Any]:
        """Convierte la entidad a diccionario."""
        return {
            "user_id": self.user_id,
            "plan_type": self.plan_type.value,
            "stars_paid": self.stars_paid,
            "payment_id": self.payment_id,
            "starts_at": self.starts_at.isoformat(),
            "expires_at": self.expires_at.isoformat(),
            "is_active": self.is_active,
            "is_expired": self.is_expired,
        }
