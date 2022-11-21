from confident import BaseConfig
from pydantic import SecretStr


class BotConfig(BaseConfig):
    bot_token: SecretStr
    use_webhook: bool = False
    webhook_host: str = "0.0.0.0"
    webhook_port: int = 3978
    webhook_url: str
