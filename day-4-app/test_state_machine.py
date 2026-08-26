import pytest
from state_machine import VehicleStateMachine, VehicleStateEnum

def test_engine_off_rpm_zero():
    """Kabul Kriteri 1: Motor kapalıyken RPM sıfıra dönmelidir."""
    vsm = VehicleStateMachine()
    vsm.update(ignition=True, accelerator_pos=0, brake_pressed=True)  # Motor çalıştı
    assert vsm.engine_speed == 800.0
    
    vsm.update(ignition=False, accelerator_pos=0, brake_pressed=False) # Kontak kapandı
    assert vsm.current_state == VehicleStateEnum.OFF
    assert vsm.engine_speed == 0.0
    assert vsm.vehicle_speed == 0.0

def test_accelerator_increases_speed_and_rpm():
    """Kabul Kriteri 2: Gaz artışı hız ve RPM üzerinde tutarlı etki oluşturmalıdır."""
    vsm = VehicleStateMachine()
    vsm.update(ignition=True, accelerator_pos=0, brake_pressed=True)  # Start
    
    initial_rpm = vsm.engine_speed
    vsm.update(ignition=True, accelerator_pos=25.0, brake_pressed=False) # Gaza bas
    
    assert vsm.current_state == VehicleStateEnum.DRIVING
    assert vsm.engine_speed > initial_rpm
    assert vsm.vehicle_speed > 0.0

def test_deterministic_simulation():
    """Kabul Kriteri 3: Aynı senaryo her çalıştırmada tekrar üretilebilir olmalıdır."""
    vsm1 = VehicleStateMachine()
    vsm2 = VehicleStateMachine()
    
    inputs = [(True, 0, True), (True, 50, False), (True, 50, False)]
    
    results1 = [vsm1.update(*inp) for inp in inputs]
    results2 = [vsm2.update(*inp) for inp in inputs]
    
    assert results1 == results2
    assert vsm1.engine_speed == vsm2.engine_speed
    assert vsm1.vehicle_speed == vsm2.vehicle_speed