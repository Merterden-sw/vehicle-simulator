import pytest
from vehicle_statement.exceptions import VehicleValidationError
from vehicle_statement.state import VehicleState
from vehicle_statement.validation import (
    validate_percentage,
    validate_rpm,
    validate_speed,
    validate_temperature,
)


def test_valid_speed():
    validate_speed(0.0)
    validate_speed(100.0)
    validate_speed(250.0)


def test_invalid_speed_raises_error():
    with pytest.raises(VehicleValidationError):
        validate_speed(-1.0)
    with pytest.raises(VehicleValidationError):
        validate_speed(301.0)


def test_valid_rpm():
    validate_rpm(0.0)
    validate_rpm(4000.0)
    validate_rpm(8000.0)


def test_invalid_rpm_raises_error():
    with pytest.raises(VehicleValidationError):
        validate_rpm(-500.0)
    with pytest.raises(VehicleValidationError):
        validate_rpm(8500.0)


def test_valid_temperature():
    validate_temperature(-40.0)
    validate_temperature(90.0)
    validate_temperature(150.0)


def test_invalid_temperature_raises_error():
    with pytest.raises(VehicleValidationError):
        validate_temperature(-41.0)
    with pytest.raises(VehicleValidationError):
        validate_temperature(151.0)


def test_valid_percentage():
    validate_percentage("throttle_pedal", 0.0)
    validate_percentage("throttle_pedal", 50.0)
    validate_percentage("throttle_pedal", 100.0)


def test_invalid_percentage_raises_error():
    with pytest.raises(VehicleValidationError):
        validate_percentage("throttle_pedal", -10.0)
    with pytest.raises(VehicleValidationError):
        validate_percentage("throttle_pedal", 105.0)


def test_vehicle_state_validate_success():
    state = VehicleState(
        speed=50.0,
        rpm=2500.0,
        engine_temp=90.0,
        fuel_level=80.0,
        brake_pedal=0.0,
        throttle_pedal=20.0,
    )
    # Doğrulama hatasız geçmeli
    state.validate()


def test_vehicle_state_validate_failure():
    state = VehicleState(speed=-20.0)
    with pytest.raises(VehicleValidationError):
        state.validate()