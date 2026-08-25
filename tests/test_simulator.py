# tests/test_simulator.py

from vehicle_statement.simulator import VehicleSimulator
from vehicle_statement.state import VehicleState


def test_simulator_acceleration():
    state = VehicleState(throttle_pedal=50.0, brake_pedal=0.0)
    simulator = VehicleSimulator(state)

    updated_state = simulator.update(dt=1.0)
    assert updated_state.speed > 0.0


def test_simulator_braking():
    state = VehicleState(speed=50.0, brake_pedal=100.0)
    simulator = VehicleSimulator(state)

    updated_state = simulator.update(dt=1.0)
    assert updated_state.speed < 50.0