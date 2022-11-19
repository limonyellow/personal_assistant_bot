from confident import BaseConfig
from pydantic import SecretStr


class BotConfig(BaseConfig):
    bot_token: SecretStr
