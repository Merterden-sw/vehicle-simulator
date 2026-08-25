# src/vehicle_statement/state.py

from dataclasses import dataclass, field
from vehicle_statement.dtc import DTC, evaluate_dtcs
from vehicle_statement.validation import (
    validate_percentage,
    validate_rpm,
    validate_signal_consistency,
    validate_speed,
    validate_temperature,
)


@dataclass
class VehicleState:
    ignition: bool = True
    engine_state: bool = True
    speed: float = 0.0
    rpm: float = 0.0
    engine_temp: float = 90.0
    fuel_level: float = 100.0
    brake_pedal: float = 0.0
    throttle_pedal: float = 0.0
    active_dtcs: list[DTC] = field(default_factory=list)

    def update_dtcs(self) -> None:
        """Duruma göre DTC kodlarını günceller."""
        self.active_dtcs = evaluate_dtcs(
            engine_temp=self.engine_temp,
            fuel_level=self.fuel_level,
            speed=self.speed,
        )

    def validate(self) -> None:
        """Tüm araç parametrelerini geçerlilik ve tutarlılık kurallarına göre kontrol eder."""
        validate_speed(self.speed)
        validate_rpm(self.rpm)
        validate_temperature(self.engine_temp)
        validate_percentage("fuel_level", self.fuel_level)
        validate_percentage("brake_pedal", self.brake_pedal)
        validate_percentage("throttle_pedal", self.throttle_pedal)

        validate_signal_consistency(
            ignition=self.ignition,
            engine_state=self.engine_state,
            rpm=self.rpm,
        )