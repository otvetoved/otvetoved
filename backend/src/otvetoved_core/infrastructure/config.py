from dishka import Provider, provide, Scope
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    driver: str
    user: str
    password: str
    host: str
    port: int
    database: str

    @property
    def url(self):
        return '{}://{}:{}@{}:{}/{}'.format(
            self.driver,
            self.user,
            self.password,
            self.host,
            self.port,
            self.database,
        )


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_prefix="APP__",
        extra='ignore',
        env_file=".env",
    )

    database: DatabaseConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def provide_config(self) -> Config:
        return Config()
