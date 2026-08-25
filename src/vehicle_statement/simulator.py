# src/vehicle_statement/simulator.py

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
from vehicle_statement.state import VehicleState


class VehicleSimulator:
    """Aracın zamana bağlı fiziksel durum güncellemelerini yöneten simülatör sınıfı."""

    def __init__(self, state: VehicleState | None = None) -> None:
        self.state = state if state is not None else VehicleState()

    def update(self, dt: float) -> VehicleState:
        """Belirtilen delta time (dt) süresince araç durumunu günceller."""
        if dt <= 0:
            return self.state

        # Motor çalışmıyorsa simülasyon hareket ettirmez
        if not self.state.engine_state or not self.state.ignition:
            self.state.speed = 0.0
            self.state.rpm = 0.0
            self.state.update_dtcs()
            self.state.validate()
            return self.state

        # Gaz ve Fren Etkisi
        throttle_effect = self.state.throttle_pedal / 100.0
        brake_effect = self.state.brake_pedal / 100.0

        # Hız Değişimi (İvme ve Frenleme)
        acceleration = throttle_effect * 30.0
        deceleration = brake_effect * 50.0 + 2.0

        new_speed = self.state.speed + (acceleration - deceleration) * dt
        self.state.speed = max(SPEED_MIN_KMH, min(SPEED_MAX_KMH, new_speed))

        # RPM Hesabı
        if self.state.speed > 0:
            calculated_rpm = 800.0 + (self.state.speed / SPEED_MAX_KMH) * (RPM_MAX - 800.0)
        else:
            calculated_rpm = 800.0 if throttle_effect > 0 else 0.0

        self.state.rpm = max(RPM_MIN, min(RPM_MAX, calculated_rpm))

        # Yakıt Tüketimi
        fuel_consumption = (throttle_effect * 0.05 + 0.005) * dt
        self.state.fuel_level = max(PERCENTAGE_MIN, min(PERCENTAGE_MAX, self.state.fuel_level - fuel_consumption))

        # Motor Sıcaklığı
        temp_change = (throttle_effect * 2.0 - 0.5) * dt
        self.state.engine_temp = max(ENGINE_TEMP_MIN_CELSIUS, min(ENGINE_TEMP_MAX_CELSIUS, self.state.engine_temp + temp_change))

        # DTC Kodlarını Güncelle ve Doğrula
        self.state.update_dtcs()
        self.state.validate()
        return self.state