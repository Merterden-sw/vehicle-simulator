# src/vehicle_statement/validation.py

from vehicle_statement.constants import (
    ENGINE_TEMP_MAX_CELSIUS,
    ENGINE_TEMP_MIN_CELSIUS,
    PERCENTAGE_MAX,
    PERCENTAGE_MIN,
    RPM_MAX,
    RPM_MIN,
    SPEED_MAX_KMH,
    SPEED_MIN_KMH,
)
from vehicle_statement.exceptions import VehicleValidationError


def validate_speed(speed: float) -> None:
    if not (SPEED_MIN_KMH <= speed <= SPEED_MAX_KMH):
        raise VehicleValidationError(
            f"Speed must be between {SPEED_MIN_KMH} and {SPEED_MAX_KMH} km/h."
        )


def validate_rpm(rpm: float) -> None:
    if not (RPM_MIN <= rpm <= RPM_MAX):
        raise VehicleValidationError(
            f"RPM must be between {RPM_MIN} and {RPM_MAX}."
        )


def validate_temperature(temp: float) -> None:
    if not (ENGINE_TEMP_MIN_CELSIUS <= temp <= ENGINE_TEMP_MAX_CELSIUS):
        raise VehicleValidationError(
            f"Engine temperature must be between {ENGINE_TEMP_MIN_CELSIUS} and {ENGINE_TEMP_MAX_CELSIUS} °C."
        )


def validate_percentage(name: str, value: float) -> None:
    if not (PERCENTAGE_MIN <= value <= PERCENTAGE_MAX):
        raise VehicleValidationError(
            f"{name} must be between {PERCENTAGE_MIN} and {PERCENTAGE_MAX}%."
        )


def validate_signal_consistency(
    ignition: bool, engine_state: bool, rpm: float
) -> None:
    """Araç sinyalleri arasındaki mantıksal tutarlılığı kontrol eder."""
    # Kural 1: Kontak kapalıysa motor çalışamaz
    if not ignition and engine_state:
        raise VehicleValidationError(
            "Engine cannot be running while ignition is OFF."
        )

    # Kural 2: Motor çalışmıyorsa devir (RPM) 0 olmalıdır
    if not engine_state and rpm > 0.0:
        raise VehicleValidationError(
            "Engine RPM must be 0.0 when engine is not running."
        )