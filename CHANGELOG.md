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

## [0.2.0] - 2026-03-19

### ✨ Added

#### Code Quality
- Pre-commit hooks configuration (ruff, mypy, bandit)
- GitHub Actions CI/CD pipeline for automated testing
- Mypy type checking configuration
- Comprehensive documentation structure

### 🔧 Changed

#### Pydantic v2 Migration
- **Migrated from `class Config` to `model_config`** - Updated all schemas to use Pydantic v2 syntax
- `UserResponse` - Updated to use `ConfigDict(from_attributes=True)`
- `VpnKeyResponse` - Updated to use `ConfigDict(from_attributes=True)`
- `PaymentResponse` - Updated to use `ConfigDict(from_attributes=True)`

#### Dependencies
- Updated `pydantic>=2.12.0` (from v1 to v2)
- Added `pydantic-core` for v2 compatibility

### 📝 Documentation

- Added `docs/` directory structure
- API documentation templates
- Development guidelines

### 🔒 Security

- Added bandit for security scanning in CI/CD
- Pre-commit hooks for automated security checks

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

- [GitHub Repository](https://github.com/usipipo/usipipo-commons)
- [GitHub Packages](https://github.com/orgs/usipipo/packages)
- [Issue Tracker](https://github.com/usipipo/usipipo-commons/issues)
