from typing import Optional

from confident import BaseConfig
from pydantic import SecretStr


class BotConfig(BaseConfig):
    bot_token: SecretStr
    use_webhook: bool = False
    webhook_host: str = "127.0.0.1"
    webhook_port: int = 80
    webhook_url: Optional[str] = None
