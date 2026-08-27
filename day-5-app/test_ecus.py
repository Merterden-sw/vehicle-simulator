import time
from ecus.powertrain_ecu import PowertrainECU
from ecus.body_ecu import BodyECU
from ecus.diagnostic_ecu import DiagnosticECU

def test_mert_info_message_and_age_signal():
    """Kişisel CAN mesajı (MERT_INFO) ve Age sinyali doğrulaması"""
    p_ecu = PowertrainECU(age=22)
    msg = p_ecu.generate_mert_info()
    
    assert msg["msg_name"] == "MERT_INFO"
    assert msg["msg_id"] == "0x123"
    assert msg["signals"]["Age"] == 22
    assert msg["signals"]["Developer"] == "Mert"

def test_ecu_message_periods():
    """ECU mesaj periyotları ve canlılık sayacı kontrolü"""
    p_ecu = PowertrainECU()
    msg1 = p_ecu.generate_powertrain_status()
    time.sleep(0.1)
    msg2 = p_ecu.generate_powertrain_status()

    assert msg2["timestamp"] > msg1["timestamp"]
    assert msg2["signals"]["AliveCounter"] == (msg1["signals"]["AliveCounter"] + 1) % 16

def test_diagnostic_extended_id():
    """Diagnostic ECU'nun 29-bit Extended ID kullanım testi"""
    d_ecu = DiagnosticECU()
    msg = d_ecu.generate_diagnostic_status()

    assert msg["msg_id"] == "0x18DAF110"