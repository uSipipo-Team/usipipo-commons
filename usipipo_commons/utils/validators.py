"""Validadores compartidos."""
import re
from typing import Optional, Tuple


# VPN key name validation constants
VPN_KEY_NAME_MIN_LENGTH = 3
VPN_KEY_NAME_MAX_LENGTH = 50
VPN_KEY_NAME_PATTERN = r'^[a-zA-Z0-9\s\-_]{3,50}$'


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
    """
    Valida nombre de clave VPN con reglas estrictas.
    
    Reglas:
    - Longitud: 3-50 caracteres
    - Permitidos: alfanuméricos (a-zA-Z0-9), espacios, guiones (-), guiones bajos (_)
    - Bloqueados: Emoji, unicode confusables, caracteres especiales de shell
    
    Args:
        name: Nombre a validar
        
    Returns:
        True si es válido, False en caso contrario
    """
    if not name:
        return False
    
    # Check length
    if len(name) < VPN_KEY_NAME_MIN_LENGTH or len(name) > VPN_KEY_NAME_MAX_LENGTH:
        return False
    
    # Check pattern (strict alphanumeric + spaces, hyphens, underscores only)
    pattern = re.compile(VPN_KEY_NAME_PATTERN)
    return bool(pattern.match(name))


def get_vpn_key_name_validation_error(name: str) -> Optional[str]:
    """
    Obtiene mensaje de error detallado para validación de nombre de clave VPN.
    
    Args:
        name: Nombre a validar
        
    Returns:
        Mensaje de error descriptivo, o None si es válido
    """
    if not name:
        return "VPN key name cannot be empty"
    
    # Check length
    if len(name) < VPN_KEY_NAME_MIN_LENGTH:
        return f"VPN key name must be at least {VPN_KEY_NAME_MIN_LENGTH} characters (got {len(name)})"
    
    if len(name) > VPN_KEY_NAME_MAX_LENGTH:
        return f"VPN key name must be at most {VPN_KEY_NAME_MAX_LENGTH} characters (got {len(name)})"
    
    # Check for blocked characters
    # Check for emoji (basic emoji unicode range)
    emoji_pattern = re.compile(
        '['
        '\U0001F600-\U0001F64F'  # emoticons
        '\U0001F300-\U0001F5FF'  # symbols & pictographs
        '\U0001F680-\U0001F6FF'  # transport & map symbols
        '\U0001F1E0-\U0001F1FF'  # flags
        '\U00002702-\U000027B0'  # dingbats
        '\U000024C2-\U0001F251'  # enclosed characters
        ']'
    )
    if emoji_pattern.search(name):
        return "VPN key name cannot contain emoji characters"
    
    # Check for shell special characters (beyond allowed ones)
    shell_chars_pattern = re.compile(r'[;&|`$(){}!<>\'"\\*?#\[\]~]')
    if shell_chars_pattern.search(name):
        return "VPN key name cannot contain special shell characters"
    
    # Check for unicode confusables (common ones that look like ASCII)
    confusables_pattern = re.compile(
        '['
        '\u0400-\u04FF'  # Cyrillic
        '\u0370-\u03FF'  # Greek
        '\u0590-\u05FF'  # Hebrew
        ']'
    )
    if confusables_pattern.search(name):
        return "VPN key name cannot contain unicode confusable characters"
    
    # Generic pattern mismatch (should catch any other invalid chars)
    pattern = re.compile(VPN_KEY_NAME_PATTERN)
    if not pattern.match(name):
        return "VPN key name can only contain letters (a-z, A-Z), numbers (0-9), spaces, hyphens (-), and underscores (_)"
    
    return None
