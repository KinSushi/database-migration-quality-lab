"""Runtime settings for database-migration-quality-lab."""

from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Local runtime settings."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_host: str = Field(default="localhost", validation_alias="MIGRATION_QUALITY_DB_HOST")
    database_port: int = Field(default=5433, validation_alias="MIGRATION_QUALITY_DB_PORT")
    database_name: str = Field(default="migration_quality", validation_alias="MIGRATION_QUALITY_DB_NAME")
    database_user: str = Field(default="migration", validation_alias="MIGRATION_QUALITY_DB_USER")
    database_password: str = Field(default="migration_local_only", validation_alias="MIGRATION_QUALITY_DB_PASSWORD")
    data_dir: Path = Field(default=Path("data"), validation_alias="MIGRATION_QUALITY_DATA_DIR")
    report_dir: Path = Field(default=Path("reports"), validation_alias="MIGRATION_QUALITY_REPORT_DIR")

    @property
    def dsn(self) -> str:
        """Return psycopg-compatible DSN."""

        return (
            f"host={self.database_host} port={self.database_port} "
            f"dbname={self.database_name} user={self.database_user} "
            f"password={self.database_password}"
        )


def load_settings() -> Settings:
    """Load settings."""

    return Settings()
