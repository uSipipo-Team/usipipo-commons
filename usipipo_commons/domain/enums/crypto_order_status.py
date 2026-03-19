"""Crypto order status enum."""

from enum import Enum


class CryptoOrderStatus(str, Enum):
    """Estado de una orden de criptomoneda."""

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    EXPIRED = "expired"
