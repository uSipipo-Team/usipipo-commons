# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- Domain entities: `User`, `VpnKey`, `Payment`
- Domain enums: `VpnType`, `KeyStatus`, `PaymentStatus`, `PaymentMethod`
- Pydantic schemas for request/response validation
- Shared constants for plans, bonuses, and error codes
- Utility functions for validation and formatting
- Comprehensive test suite (33 tests)

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

---

## [0.3.0] - 2026-03-20

### Added
- **Crypto Payment Entities** 🎉
  - `CryptoOrder` entity with order management methods
  - `CryptoTransaction` entity with confirmation tracking
  - `WebhookToken` entity for webhook validation
- **New Enums**
  - `CryptoOrderStatus` (PENDING, COMPLETED, FAILED, EXPIRED)
  - `CryptoTransactionStatus` (PENDING, CONFIRMING, COMPLETED, FAILED)
- **Entity Methods**
  - `CryptoOrder.create()` factory method
  - `CryptoOrder.mark_completed()`, `mark_failed()`, `mark_expired()`
  - `CryptoTransaction.add_confirmation()` with completion check
  - `WebhookToken.is_valid()` for token expiration check
- **Constants**
  - `CRYPTO_CONFIRMATIONS_REQUIRED = 15` for blockchain confirmations
  - `WEBHOOK_TOKEN_EXPIRY_MINUTES = 30` for webhook security

### Changed
- Fixed `CryptoOrder` dataclass field ordering (user_id moved to end with default)

### Project Structure
```
usipipo_commons/
├── domain/
│   ├── entities/      # User, VpnKey, Payment, CryptoOrder, CryptoTransaction, WebhookToken
│   └── enums/         # VpnType, KeyStatus, PaymentStatus, PaymentMethod, CryptoOrderStatus, CryptoTransactionStatus
├── schemas/           # Pydantic request/response models
├── constants/         # Plans, bonuses, error codes, crypto constants
└── utils/             # Validators, formatters
```

---

## [0.2.0] - 2026-03-19

### Added
- **Crypto Payment Support**
  - `CryptoOrder` entity for tracking crypto orders
  - `CryptoTransaction` entity for blockchain transactions
  - `WebhookToken` entity for webhook validation
  - `CryptoOrderStatus` enum
  - `CryptoTransactionStatus` enum

---

## [0.1.0] - 2026-03-18

### Added
- **Initial Release** 🎉
- Core domain entities for the uSipipo ecosystem
- Pydantic v2 schemas for API validation
- Shared constants and error codes
- Utility validators and formatters
- Test coverage for all modules
- Python 3.13+ support
- Published to GitHub Packages

### Project Structure
```
usipipo_commons/
├── domain/
│   ├── entities/      # User, VpnKey, Payment
│   └── enums/         # VpnType, KeyStatus, PaymentStatus, PaymentMethod
├── schemas/           # Pydantic request/response models
├── constants/         # Plans, bonuses, error codes
└── utils/             # Validators, formatters
```

### Dependencies
- `pydantic>=2.12.0`

### Dev Dependencies
- `pytest>=8.0.0`
- `pytest-cov>=4.0.0`
- `mypy>=1.0.0`
- `ruff>=0.1.0`

---

## Links

- [GitHub Repository](https://github.com/uSipipo-Team/usipipo-commons)
- [PyPI Package](https://pypi.org/project/usipipo-commons/)
- [Issue Tracker](https://github.com/uSipipo-Team/usipipo-commons/issues)
