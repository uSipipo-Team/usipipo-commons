"""Validadores compartidos."""
import re
from typing import Optional


def validate_telegram_id(telegram_id: int) -> bool:
    """Valida que el Telegram ID sea válido."""
    return telegram_id > 0 and telegram_id < 2**63


def validate_referral_code(code: Optional[str]) -> bool:
    """Valida formato de código de referido."""
    if not code:
        return True  # Optional, puede ser None

    # Alfanumérico, 4-16 caracteres
    pattern = r'^[a-zA-Z0-9]{4,16}$'
    return bool(re.match(pattern, code))


def validate_vpn_key_name(name: str) -> bool:
    """Valida nombre de clave VPN."""
    if not name or len(name) > 50:
        return False

    # Permitir letras, números, espacios, guiones
    pattern = r'^[a-zA-Z0-9\s\-_]+$'
    return bool(re.match(pattern, name))
