from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..enums.payment_status import PaymentStatus
from ..enums.payment_method import PaymentMethod


@dataclass
class Payment:
    """Entidad de pago compartida."""
    id: UUID
    user_id: UUID
    amount_usd: float
    gb_purchased: float
    method: PaymentMethod
    status: PaymentStatus
    crypto_address: Optional[str]
    crypto_network: Optional[str]
    telegram_star_invoice_id: Optional[str]
    created_at: datetime
    expires_at: Optional[datetime]
    paid_at: Optional[datetime]
    transaction_hash: Optional[str]

    def to_dict(self) -> dict:
        """Convierte a diccionario para serialización."""
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "amount_usd": self.amount_usd,
            "gb_purchased": self.gb_purchased,
            "method": self.method.value,
            "status": self.status.value,
            "crypto_address": self.crypto_address,
            "crypto_network": self.crypto_network,
            "telegram_star_invoice_id": self.telegram_star_invoice_id,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "paid_at": self.paid_at.isoformat() if self.paid_at else None,
            "transaction_hash": self.transaction_hash,
        }
