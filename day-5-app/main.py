import time
from ecus.powertrain_ecu import PowertrainECU
from ecus.body_ecu import BodyECU
from ecus.diagnostic_ecu import DiagnosticECU

def run_ecu_simulation(duration_seconds: int = 3):
    powertrain = PowertrainECU(age=22)
    body = BodyECU()
    diagnostic = DiagnosticECU()

    print("=" * 80)
    print(" 🚗 SANAL ECU PERİYODİK CAN MESAJ ÜRETİM SİMÜLASYONU (5. GÜN) ")
    print("=" * 80)
    print(f"{'Geçen Süre':<12} | {'CAN ID':<12} | {'Mesaj Adı':<18} | {'Sinyal Verileri'}")
    print("-" * 80)

    start_time = time.time()
    last_100ms = 0
    last_500ms = 0
    last_1000ms = 0

    while (time.time() - start_time) < duration_seconds:
        current_time = time.time()
        elapsed_ms = int((current_time - start_time) * 1000)

        # 100 ms Periyot (Powertrain ECU + MERT_INFO)
        if elapsed_ms - last_100ms >= 100:
            last_100ms = elapsed_ms
            p_msg = powertrain.generate_powertrain_status(engine_speed=1500.0, vehicle_speed=45.0)
            pedal_msg = powertrain.generate_pedal_status(accelerator_pos=25.0)
            mert_msg = powertrain.generate_mert_info()

            print(f"{elapsed_ms} ms{'':<6} | {p_msg['msg_id']:<12} | {p_msg['msg_name']:<18} | {p_msg['signals']}")
            print(f"{elapsed_ms} ms{'':<6} | {mert_msg['msg_id']:<12} | {mert_msg['msg_name']:<18} | {mert_msg['signals']}")

        # 500 ms Periyot (Body ECU)
        if elapsed_ms - last_500ms >= 500:
            last_500ms = elapsed_ms
            b_msg = body.generate_body_status()
            print(f"{elapsed_ms} ms{'':<6} | {b_msg['msg_id']:<12} | {b_msg['msg_name']:<18} | {b_msg['signals']}")

        # 1000 ms Periyot (Diagnostic ECU)
        if elapsed_ms - last_1000ms >= 1000:
            last_1000ms = elapsed_ms
            d_msg = diagnostic.generate_diagnostic_status()
            print(f"{elapsed_ms} ms{'':<6} | {d_msg['msg_id']:<12} | {d_msg['msg_name']:<18} | {d_msg['signals']}")

        time.sleep(0.01)  # CPU kullanımını dengelemek için kısa uyku

    print("=" * 80)
    print(" ✅ SİMÜLASYON TAMAMLANDI")
    print("=" * 80)

if __name__ == "__main__":
    run_ecu_simulation()