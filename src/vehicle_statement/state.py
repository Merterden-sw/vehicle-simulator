from dataclasses import dataclass

from vehicle_statement.validation import (
    validate_percentage,
    validate_rpm,
    validate_speed,
    validate_temperature,
)


@dataclass
class VehicleState:
    """Araç durumunu ve sensör verilerini tutan veri sınıfı."""

    speed: float = 0.0
    rpm: float = 0.0
    engine_temp: float = 20.0
    fuel_level: float = 100.0
    brake_pedal: float = 0.0
    throttle_pedal: float = 0.0

    def validate(self) -> None:
        """Tüm sensör verilerini ilgili doğrulama fonksiyonlarıyla kontrol eder."""
        validate_speed(self.speed)
        validate_rpm(self.rpm)
        validate_temperature(self.engine_temp)
        validate_percentage("fuel_level", self.fuel_level)
        validate_percentage("brake_pedal", self.brake_pedal)
        validate_percentage("throttle_pedal", self.throttle_pedal)