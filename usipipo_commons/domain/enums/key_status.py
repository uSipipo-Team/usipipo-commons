from enum import Enum


class KeyStatus(str, Enum):
    """Estados de una clave VPN."""
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    PENDING = "pending"
