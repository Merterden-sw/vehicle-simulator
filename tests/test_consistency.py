# tests/test_consistency.py

import pytest
from vehicle_statement.exceptions import VehicleValidationError
from vehicle_statement.state import VehicleState


def test_ignition_off_with_engine_running_fails():
    """Kontak kapalıyken motorun çalışamayacağını doğrular."""
    state = VehicleState(ignition=False, engine_state=True, rpm=1000.0)
    with pytest.raises(VehicleValidationError):
        state.validate()


def test_engine_off_with_nonzero_rpm_fails():
    """Motor kapalıyken RPM'in 0'dan büyük olamayacağını doğrular."""
    state = VehicleState(ignition=True, engine_state=False, rpm=800.0)
    with pytest.raises(VehicleValidationError):
        state.validate()