import time

class DiagnosticECU:
    def __init__(self):
        self.ecu_name = "DiagnosticECU"
        self.period_ms = 1000  # 1000 ms periyot

    def generate_diagnostic_status(self, dtc_code: str = "P0000") -> dict:
        return {
            "msg_id": "0x18DAF110",  # 29-bit Extended ID (OBD-II)
            "msg_name": "DiagnosticStatus",
            "timestamp": time.time(),
            "signals": {
                "DTC_Code": dtc_code,
                "ECU_Health": "OK"
            }
        }