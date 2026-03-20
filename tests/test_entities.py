"""Tests para entidades del dominio."""
import pytest
from datetime import datetime
from uuid import uuid4

from usipipo_commons.domain.entities import User, VpnKey, Payment
from usipipo_commons.domain.enums import KeyType, KeyStatus, PaymentStatus, PaymentMethod


class TestUser:
    """Tests para la entidad User."""

    def test_user_creation(self):
        """Test para crear un usuario válido."""
        user = User(
            id=uuid4(),
            telegram_id=123456789,
            username="testuser",
            first_name="Test",
            last_name="User",
            is_admin=False,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            balance_gb=5.0,
            total_purchased_gb=10.0,
            referral_code="REF1234",
            referred_by=None,
        )

        assert user.telegram_id == 123456789
        assert user.username == "testuser"
        assert user.balance_gb == 5.0
        assert user.is_admin is False

    def test_user_to_dict(self):
        """Test para convertir usuario a diccionario."""
        user_id = uuid4()
        user = User(
            id=user_id,
            telegram_id=123456789,
            username="testuser",
            first_name="Test",
            last_name="User",
            is_admin=False,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            balance_gb=5.0,
            total_purchased_gb=10.0,
            referral_code="REF1234",
            referred_by=None,
        )

        user_dict = user.to_dict()

        assert user_dict["telegram_id"] == 123456789
        assert user_dict["username"] == "testuser"
        assert user_dict["balance_gb"] == 5.0
        assert isinstance(user_dict["id"], str)


class TestVpnKey:
    """Tests para la entidad VpnKey."""

    def test_vpn_key_creation(self):
        """Test para crear una clave VPN válida."""
        vpn_key = VpnKey(
            id="test-key-id",
            user_id=123456789,  # telegram_id
            name="My VPN",
            key_type=KeyType.WIREGUARD,
            key_data="wg-config...",
            external_id="peer-123",
            is_active=True,
            created_at=datetime.now(),
            expires_at=None,
            last_seen_at=None,
            used_bytes=0,
            data_limit_bytes=5 * 1024**3,
            billing_reset_at=datetime.now(),
        )

        assert vpn_key.name == "My VPN"
        assert vpn_key.key_type == KeyType.WIREGUARD
        assert vpn_key.is_active is True
        assert vpn_key.data_limit_gb == 5.0

    def test_vpn_key_to_dict(self):
        """Test para convertir clave VPN a diccionario."""
        vpn_key = VpnKey(
            id="test-key-id",
            user_id=123456789,  # telegram_id
            name="My VPN",
            key_type=KeyType.OUTLINE,
            key_data="ss://config...",
            external_id="key-456",
            is_active=True,
            created_at=datetime.now(),
            expires_at=None,
            last_seen_at=None,
            used_bytes=0,
            data_limit_bytes=10 * 1024**3,
            billing_reset_at=datetime.now(),
        )

        vpn_dict = vpn_key.to_dict()

        assert vpn_dict["name"] == "My VPN"
        assert vpn_dict["key_type"] == "outline"
        assert vpn_dict["is_active"] is True


class TestPayment:
    """Tests para la entidad Payment."""

    def test_payment_creation(self):
        """Test para crear un pago válido."""
        payment = Payment(
            id=uuid4(),
            user_id=uuid4(),
            amount_usd=5.0,
            gb_purchased=10.0,
            method=PaymentMethod.TELEGRAM_STARS,
            status=PaymentStatus.PENDING,
            crypto_address=None,
            crypto_network=None,
            telegram_star_invoice_id=None,
            created_at=datetime.now(),
            expires_at=None,
            paid_at=None,
            transaction_hash=None,
        )

        assert payment.amount_usd == 5.0
        assert payment.gb_purchased == 10.0
        assert payment.method == PaymentMethod.TELEGRAM_STARS
        assert payment.status == PaymentStatus.PENDING

    def test_payment_to_dict(self):
        """Test para convertir pago a diccionario."""
        payment = Payment(
            id=uuid4(),
            user_id=uuid4(),
            amount_usd=10.0,
            gb_purchased=20.0,
            method=PaymentMethod.CRYPTO_USDT,
            status=PaymentStatus.COMPLETED,
            crypto_address="0x123abc",
            crypto_network="BSC",
            telegram_star_invoice_id=None,
            created_at=datetime.now(),
            expires_at=None,
            paid_at=datetime.now(),
            transaction_hash="0xabc123",
        )

        payment_dict = payment.to_dict()

        assert payment_dict["amount_usd"] == 10.0
        assert payment_dict["method"] == "crypto_usdt"
        assert payment_dict["status"] == "completed"
        assert payment_dict["transaction_hash"] == "0xabc123"
