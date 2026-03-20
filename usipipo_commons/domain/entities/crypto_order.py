"""Crypto order entity."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional

from usipipo_commons.domain.enums.crypto_order_status import CryptoOrderStatus

ORDER_EXPIRATION_MINUTES = 30


@dataclass
class CryptoOrder:
    """
    Entidad de orden de criptomoneda.

    Representa una orden de compra creada antes de que el usuario envíe el pago.
    """

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    package_type: str = "basic"
    amount_usdt: float = 0.0
    wallet_address: str = ""
    tron_dealer_order_id: Optional[str] = None
    status: CryptoOrderStatus = CryptoOrderStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
        + timedelta(minutes=ORDER_EXPIRATION_MINUTES)
    )
    tx_hash: Optional[str] = None
    confirmed_at: Optional[datetime] = None
    user_id: uuid.UUID = field(default_factory=uuid.uuid4)

    @property
    def is_pending(self) -> bool:
        """Verifica si la orden está pendiente."""
        return self.status == CryptoOrderStatus.PENDING

    @property
    def is_completed(self) -> bool:
        """Verifica si la orden está completada."""
        return self.status == CryptoOrderStatus.COMPLETED

    @property
    def is_expired(self) -> bool:
        """Verifica si la orden expiró."""
        return datetime.now(timezone.utc) > self.expires_at

    def mark_completed(self, tx_hash: str) -> None:
        """Marca la orden como completada."""
        self.status = CryptoOrderStatus.COMPLETED
        self.tx_hash = tx_hash
        self.confirmed_at = datetime.now(timezone.utc)

    def mark_failed(self) -> None:
        """Marca la orden como fallida."""
        self.status = CryptoOrderStatus.FAILED

    def mark_expired(self) -> None:
        """Marca la orden como expirada."""
        self.status = CryptoOrderStatus.EXPIRED

    @classmethod
    def create(
        cls,
        user_id: uuid.UUID,
        package_type: str,
        amount_usdt: float,
        wallet_address: str,
    ) -> "CryptoOrder":
        """Factory method para crear una orden."""
        return cls(
            user_id=user_id,
            package_type=package_type,
            amount_usdt=amount_usdt,
            wallet_address=wallet_address,
        )
