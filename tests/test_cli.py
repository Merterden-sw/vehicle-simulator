# tests/test_cli.py

from vehicle_statement.cli import run_cli


def test_cli_execution(capsys):
    run_cli()
    captured = capsys.readouterr()
    assert "Araç Telemetri Simülatörü Başlatılıyor" in captured.out
    assert "Simülasyon Tamamlandı" in captured.out