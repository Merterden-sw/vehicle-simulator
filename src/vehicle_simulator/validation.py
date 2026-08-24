# src/vehicle_simulator/validation.py

from vehicle_simulator.constants import (
    MAX_PERCENTAGE,
    MAX_RPM,
    MAX_SPEED,
    MAX_TEMPERATURE,
    MIN_PERCENTAGE,
    MIN_RPM,
    MIN_SPEED,
    MIN_TEMPERATURE,
)
from vehicle_simulator.exceptions import VehicleValidationError


def validate_speed(speed: float) -> None:
    """Araç hızını doğrular."""
    if not isinstance(speed, (int, float)):
        raise VehicleValidationError(
            f"Geçersiz hız veri tipi: {type(speed).__name__}"
        )

    if not (MIN_SPEED <= speed <= MAX_SPEED):
        raise VehicleValidationError(
            f"Hız sınırı ihlali: {speed} km/h (Beklenen: [{MIN_SPEED}, {MAX_SPEED}])"
        )


def validate_percentage(signal_name: str, value: float) -> None:
    """Yüzde tabanlı sinyalleri (Gaz, Fren, Depo) doğrular."""
    if not isinstance(value, (int, float)):
        raise VehicleValidationError(
            f"Geçersiz '{signal_name}' veri tipi: {type(value).__name__}"
        )

    if not (MIN_PERCENTAGE <= value <= MAX_PERCENTAGE):
        raise VehicleValidationError(
            f"Yüzde sınırı ihlali '{signal_name}': %{value} (Beklenen: [%{MIN_PERCENTAGE}, %{MAX_PERCENTAGE}])"
        )


def validate_temperature(temp_c: float) -> None:
    """Motor soğutma sıvısı sıcaklığını doğrular."""
    if not isinstance(temp_c, (int, float)):
        raise VehicleValidationError(
            f"Geçersiz sıcaklık veri tipi: {type(temp_c).__name__}"
        )

    if not (MIN_TEMPERATURE <= temp_c <= MAX_TEMPERATURE):
        raise VehicleValidationError(
            f"Sıcaklık sınırı ihlali: {temp_c} °C (Beklenen: [{MIN_TEMPERATURE}, {MAX_TEMPERATURE}])"
        )


def validate_rpm(rpm: float) -> None:
    """Motor devrini doğrular."""
    if not isinstance(rpm, (int, float)):
        raise VehicleValidationError(
            f"Geçersiz RPM veri tipi: {type(rpm).__name__}"
        )

    if not (MIN_RPM <= rpm <= MAX_RPM):
        raise VehicleValidationError(
            f"Motor devri sınırı ihlali: {rpm} RPM (Beklenen: [{MIN_RPM}, {MAX_RPM}])"
        )