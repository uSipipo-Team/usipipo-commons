# uSipipo Commons

> Librería compartida para el ecosistema uSipipo

## Instalación

```bash
# Desde PyPI (privado, requiere token)
pip install usipipo-commons --index-url https://usipipo:${TOKEN}@pypi.pkg.github.com

# Desde GitHub (desarrollo)
pip install git+https://github.com/usipipo/usipipo-commons.git
```

## Uso

```python
from usipipo_commons.domain.entities import User, VpnKey, Payment
from usipipo_commons.schemas import CreateVpnKeyRequest, PaymentResponse
from usipipo_commons.constants import FREE_GB, REFERRAL_BONUS_GB
from usipipo_commons.utils import validate_telegram_id, format_bytes
```

## Estructura

```
usipipo_commons/
├── domain/
│   ├── entities/      # Entidades del dominio
│   └── enums/         # Enums compartidos
├── schemas/           # Pydantic schemas
├── constants/         # Constantes compartidas
└── utils/             # Utilitarios
```

## Desarrollo

```bash
# Clonar
git clone https://github.com/usipipo/usipipo-commons.git
cd usipipo-commons

# Instalar dependencias
uv sync --dev

# Ejecutar tests
uv run pytest
```

## Publicación

```bash
# Build
uv build

# Publicar a GitHub Packages
uv publish --publish-url https://pypi.pkg.github.com
```

## License

MIT © uSipipo
