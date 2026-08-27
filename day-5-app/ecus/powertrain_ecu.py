import time

class PowertrainECU:
    def __init__(self, age: int = 22):
        self.ecu_name = "PowertrainECU"
        self.period_ms = 100  # 100 ms periyot
        self.counter = 0
        self.age = age

    def generate_powertrain_status(self, engine_speed: float = 800.0, vehicle_speed: float = 0.0) -> dict:
        self.counter = (self.counter + 1) % 16
        return {
            "msg_id": "0x100",  # 11-bit Standard ID
            "msg_name": "PowertrainStatus",
            "timestamp": time.time(),
            "signals": {
                "EngineSpeed": engine_speed,
                "VehicleSpeed": vehicle_speed,
                "AliveCounter": self.counter
            }
        }

    def generate_pedal_status(self, accelerator_pos: float = 0.0, brake_pressed: bool = False) -> dict:
        return {
            "msg_id": "0x101",  # 11-bit Standard ID
            "msg_name": "PedalStatus",
            "timestamp": time.time(),
            "signals": {
                "AcceleratorPos": accelerator_pos,
                "BrakePressed": brake_pressed
            }
        }

    def generate_mert_info(self) -> dict:
        """Kendi adınıza mesaj ve Age sinyali"""
        return {
            "msg_id": "0x123",  # 11-bit Standard ID
            "msg_name": "MERT_INFO",
            "timestamp": time.time(),
            "signals": {
                "Age": self.age,
                "Developer": "Mert"
            }
        }