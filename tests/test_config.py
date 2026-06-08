from migration_quality.config import Settings


def test_settings_defaults() -> None:
    settings = Settings()

    assert settings.database_host == "localhost"
    assert settings.database_port == 5433
    assert "dbname=migration_quality" in settings.dsn
    assert "user=migration" in settings.dsn
