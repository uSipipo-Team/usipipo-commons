"""Consumption invoice domain entity."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from enum import Enum
from typing import Optional


class InvoiceStatus(str, Enum):
    """Estados posibles de una factura de consumo."""

    PENDING = "pending"  # Factura generada, esperando pago
    PAID = "paid"  # Factura pagada exitosamente
    EXPIRED = "expired"  # Factura vencida (30 minutos)
    CANCELLED = "cancelled"  # Factura cancelada manualmente


class PaymentMethod(str, Enum):
    """Métodos de pago soportados."""

    STARS = "stars"  # Pago con Telegram Stars
    CRYPTO = "crypto"  # Pago con USDT (BSC)


@dataclass
class ConsumptionInvoice:
    """
    Entidad que representa una factura de pago por consumo.

    Cada factura tiene un tiempo límite de 30 minutos para ser pagada.
    Se asocia con un ciclo de facturación (ConsumptionBilling).
    """

    billing_id: uuid.UUID
    user_id: int
    amount_usd: Decimal
    wallet_address: str  # Dirección de wallet para recibir el pago (solo crypto)
    payment_method: PaymentMethod = PaymentMethod.CRYPTO
    status: InvoiceStatus = InvoiceStatus.PENDING
    id: Optional[uuid.UUID] = None
    expires_at: Optional[datetime] = None
    paid_at: Optional[datetime] = None
    transaction_hash: Optional[str] = None
    telegram_payment_id: Optional[str] = None  # Para pagos con Stars
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    # Tiempo de expiración: 30 minutos
    EXPIRATION_MINUTES: int = field(default=30, repr=False)

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4()
        if self.expires_at is None:
            self.expires_at = datetime.now(timezone.utc) + timedelta(
                minutes=self.EXPIRATION_MINUTES
            )

    @property
    def is_pending(self) -> bool:
        """Verifica si la factura está pendiente de pago."""
        return self.status == InvoiceStatus.PENDING

    @property
    def is_paid(self) -> bool:
        """Verifica si la factura está pagada."""
        return self.status == InvoiceStatus.PAID

    @property
    def is_expired(self) -> bool:
        """Verifica si la factura ha expirado."""
        if self.status == InvoiceStatus.EXPIRED:
            return True
        if self.expires_at is None:
            return False
        return datetime.now(timezone.utc) > self.expires_at

    @property
    def is_usdt_payment(self) -> bool:
        """Verifica si es un pago en USDT (basado en la dirección)."""
        # Las direcciones BSC comienzan con 0x
        return self.wallet_address.startswith("0x")

    @property
    def time_remaining_seconds(self) -> int:
        """Retorna los segundos restantes para pagar la factura."""
        if self.status != InvoiceStatus.PENDING or self.expires_at is None:
            return 0
        remaining = (self.expires_at - datetime.now(timezone.utc)).total_seconds()
        return max(0, int(remaining))

    @property
    def time_remaining_formatted(self) -> str:
        """Retorna el tiempo restante formateado (MM:SS)."""
        seconds = self.time_remaining_seconds
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"

    def mark_as_paid(
        self,
        transaction_hash: Optional[str] = None,
        telegram_payment_id: Optional[str] = None,
    ) -> None:
        """
        Marca la factura como pagada.

        Args:
            transaction_hash: Hash de la transacción blockchain (para crypto)
            telegram_payment_id: ID de pago de Telegram (para Stars)
        """
        if self.status != InvoiceStatus.PENDING:
            raise ValueError("Solo se pueden pagar facturas pendientes")

        if self.is_expired:
            raise ValueError("La factura ha expirado")

        self.status = InvoiceStatus.PAID
        self.paid_at = datetime.now(timezone.utc)
        self.transaction_hash = transaction_hash
        self.telegram_payment_id = telegram_payment_id

    def mark_expired(self) -> None:
        """Marca la factura como expirada."""
        self.status = InvoiceStatus.EXPIRED

    def mark_cancelled(self) -> None:
        """Marca la factura como cancelada."""
        if self.status != InvoiceStatus.PENDING:
            raise ValueError("Solo se pueden cancelar facturas pendientes")

        self.status = InvoiceStatus.CANCELLED

    def __repr__(self) -> str:
        return (
            f"<ConsumptionInvoice(id={self.id}, user_id={self.user_id}, "
            f"status={self.status.value}, amount=${self.amount_usd})>"
        )
