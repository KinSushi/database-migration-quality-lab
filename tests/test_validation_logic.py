from migration_quality.validate import get_validation_checks


def test_validation_checks_configured() -> None:
    checks = get_validation_checks()

    assert len(checks) >= 4
    assert len({check.check_id for check in checks}) == len(checks)
    for check in checks:
        assert check.check_id.startswith("VAL-")
        assert "SELECT" in check.query.upper()
