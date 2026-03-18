from enum import Enum


class VpnType(str, Enum):
    """Tipos de VPN soportados."""
    WIREGUARD = "wireguard"
    OUTLINE = "outline"
