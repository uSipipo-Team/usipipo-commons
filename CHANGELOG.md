# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.6] - 2026-03-21

### Added
- **Admin Entities**: `AdminUserInfo`, `AdminKeyInfo`, `ServerStatus`, `AdminOperationResult`
- **Balance Entity**: `Balance` with `add()`, `subtract()`, `has_sufficient()` methods
- **Data Package Entity**: `DataPackage` with `PackageType` enum (BASIC, ESTANDAR, AVANZADO, PREMIUM, UNLIMITED)
- **Subscription Transaction Entity**: `SubscriptionTransaction` with status tracking
- **Ticket System Entities**: `Ticket`, `TicketMessage` with full support workflow
- **VPN Key Enhancements**: 
  - `KeyType` enum (OUTLINE, WIREGUARD)
  - Usage tracking methods: `used_mb()`, `used_gb()`, `remaining_bytes()`
  - Billing management: `needs_reset()`, `reset_billing_cycle()`, `add_usage()`
  - Serialization: `to_dict()` method
- **New Enums**:
  - `SubscriptionTransactionStatus` (PENDING, ACTIVE, COMPLETED, FAILED, REFUNDED)
  - `BillingStatus` (PENDING, PROCESSING, COMPLETED, FAILED)
  - `InvoiceStatus` (DRAFT, ISSUED, PAID, OVERDUE, CANCELLED)
  - `ConsumptionPaymentMethod` (STRIPE, CRYPTO, MANUAL)

### Changed
- **VpnKey Entity**: Complete refactor with monorepo-aligned structure
  - Changed `user_id` from UUID to `int` (telegram_id)
  - Changed `vpn_type` to `key_type` for clarity
  - Fixed dataclass field ordering for Python 3.13 compatibility

### Fixed
- All entity tests updated and passing (33 tests)
- Dataclass field ordering issues in Python 3.13

---

## [0.5.5] - 2026-03-21

### Added
- **SubscriptionPlan Entity**: Complete subscription plan management
- **PlanType Enum**: ONE_MONTH, THREE_MONTHS, SIX_MONTHS

---

## [0.5.4] - 2026-03-21

### Added
- **CryptoOrder Entity**: Crypto payment order management with state machine
- **CryptoOrderStatus Enum**: PENDING, COMPLETED, FAILED, EXPIRED

### Changed
- Fixed `CryptoOrder` dataclass field ordering (user_id moved to end with default)

---

## [0.5.3] - 2026-03-21

### Added
- **Consumption Billing Entities**: 
  - `ConsumptionBilling` with billing cycle tracking
  - `ConsumptionInvoice` with invoice generation
- **New Enums**:
  - `BillingStatus`
  - `InvoiceStatus`
  - `ConsumptionPaymentMethod`

---

## [0.5.2] - 2026-03-20

### Added
- **Crypto Transaction Support**:
  - `CryptoTransaction` entity with blockchain confirmation tracking
  - `WebhookToken` entity for secure webhook validation
  - `CryptoTransactionStatus` enum (PENDING, CONFIRMING, COMPLETED, FAILED)

### Changed
- Added `CRYPTO_CONFIRMATIONS_REQUIRED = 15` constant
- Added `WEBHOOK_TOKEN_EXPIRY_MINUTES = 30` constant

---

## [0.5.1] - 2026-03-20

### Added
- **Core Domain Entities**:
  - `User` - User account management
  - `VpnKey` - VPN key representation
  - `Payment` - Payment transaction tracking
- **Core Enums**:
  - `VpnType` - VPN protocol types
  - `KeyStatus` - Key lifecycle status
  - `PaymentStatus` - Payment state machine
  - `PaymentMethod` - Supported payment methods
- **Pydantic Schemas**: Request/response validation models
- **Constants**: Plans, bonuses, error codes
- **Utilities**: Validators and formatters
- **Test Suite**: 33 comprehensive tests

---

## [0.4.1] - 2026-03-20

### Fixed
- **VpnKey Entity**: Added `to_dict()` method for serialization
- **Tests**: Updated VpnKey tests to match monorepo entity structure

---

## [0.4.0] - 2026-03-20

### Added
- Complete entity library port from monorepo (14 entities, 14 enums)

---

## [0.3.0] - 2026-03-20

### Added
- Crypto payment entities and enums

---

## [0.2.0] - 2026-03-19

### Added
- Initial crypto payment support

---

## [0.1.0] - 2026-03-18

### Added
- Initial release with core domain entities, schemas, and utilities

---

## Links

- [GitHub Repository](https://github.com/uSipipo-Team/usipipo-commons)
- [PyPI Package](https://pypi.org/project/usipipo-commons/)
- [Issue Tracker](https://github.com/uSipipo-Team/usipipo-commons/issues)
