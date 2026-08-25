# tests/test_dtc.py

from vehicle_statement.dtc import DTC
from vehicle_statement.state import VehicleState


def test_high_temperature_dtc():
    state = VehicleState(engine_temp=115.0)
    state.update_dtcs()
    assert DTC.HIGH_ENGINE_TEMP in state.active_dtcs


def test_low_fuel_dtc():
    state = VehicleState(fuel_level=10.0)
    state.update_dtcs()
    assert DTC.LOW_FUEL_LEVEL in state.active_dtcs