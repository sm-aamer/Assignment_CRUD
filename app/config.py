from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", populate_by_name=True)

    app_name: str = "Patient Management System"
    database_url: str = Field(default="sqlite:///./assignment_API_crud_db", alias="DATABASE_URL")


settings = Settings()
