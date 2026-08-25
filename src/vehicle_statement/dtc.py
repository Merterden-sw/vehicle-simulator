# src/vehicle_statement/dtc.py

from enum import Enum


class DTC(str, Enum):
    HIGH_ENGINE_TEMP = "P0217"  # Motor Aşırı Isındı
    LOW_FUEL_LEVEL = "P0230"    # Düşük Yakıt Seviyesi
    OVER_SPEED = "P0299"        # Aşırı Hız Sınırı


def evaluate_dtcs(engine_temp: float, fuel_level: float, speed: float) -> list[DTC]:
    """Araç verilerini analiz eder ve aktif arıza kodlarını (DTC) döndürür."""
    active_dtcs: list[DTC] = []

    if engine_temp > 110.0:
        active_dtcs.append(DTC.HIGH_ENGINE_TEMP)

    if fuel_level < 15.0:
        active_dtcs.append(DTC.LOW_FUEL_LEVEL)

    if speed > 180.0:
        active_dtcs.append(DTC.OVER_SPEED)

    return active_dtcs