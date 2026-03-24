BaseSettings是讀取環境變數的一項偉大創新，但為整個應用使用單個BaseSettings隨著時間的推移可能會變得混亂。為了提高可維護性和組織性，我們將BaseSettings拆分到不同的模組和領域中。

```python
# src.auth.config
from datetime import timedelta

from pydantic_settings import BaseSettings

class AuthConfig(BaseSettings):
    JWT_ALG: str
    JWT_SECRET: str
    JWT_EXP: int = 5  # 分鐘

    REFRESH_TOKEN_KEY: str
    REFRESH_TOKEN_EXP: timedelta = timedelta(days=30)

    SECURE_COOKIES: bool = True

auth_settings = AuthConfig()

# src.config
from pydantic import PostgresDsn, RedisDsn, model_validator
from pydantic_settings import BaseSettings

from src.constants import Environment

class Config(BaseSettings):
    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn

    SITE_DOMAIN: str = "myapp.com"

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1.0"

settings = Config()
```
