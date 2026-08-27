import time

class BodyECU:
    def __init__(self):
        self.ecu_name = "BodyECU"
        self.period_ms = 500  # 500 ms periyot

    def generate_body_status(self, door_open: bool = False, headlights_on: bool = True) -> dict:
        return {
            "msg_id": "0x200",  # 11-bit Standard ID
            "msg_name": "BodyStatus",
            "timestamp": time.time(),
            "signals": {
                "DoorOpen": door_open,
                "HeadlightsOn": headlights_on
            }
        }