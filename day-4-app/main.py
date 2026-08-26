import json
import time
from pathlib import Path
from state_machine import VehicleStateMachine

def run_simulation():
    # 1. Senaryo (JSON) dosyasının yolunu belirle
    base_dir = Path(__file__).parent
    config_path = base_dir / "config" / "normal_drive.json"
    
    if not config_path.exists():
        print(f"Hata: {config_path} senaryo dosyası bulunamadı!")
        return

    # 2. JSON dosyasını oku
    with open(config_path, "r", encoding="utf-8") as f:
        scenario_steps = json.load(f)

    # 3. State Machine nesnesini başlat
    vsm = VehicleStateMachine()

    print("=" * 70)
    print(" 🚗 ARAÇ NORMAL SÜRÜŞ SİMÜLASYONU BAŞLATILDI (4. GÜN) ")
    print("=" * 70)
    print(f"{'Adım':<6} | {'Eylem':<13} | {'Durum (State)':<16} | {'RPM':<8} | {'Hız (km/h)':<10}")
    print("-" * 70)

    # 4. Adım adım senaryoyu çalıştır
    for step_data in scenario_steps:
        step_num = step_data.get("step")
        action = step_data.get("action")
        ignition = step_data.get("ignition")
        accelerator = step_data.get("accelerator")
        brake = step_data.get("brake")

        # State Machine'i güncelle
        current_state = vsm.update(
            ignition=ignition,
            accelerator_pos=accelerator,
            brake_pressed=brake
        )

        # Sonuçları ekrana yazdır
        print(
            f"{step_num:<6} | "
            f"{action:<13} | "
            f"{current_state.name:<16} | "
            f"{vsm.engine_speed:<8.1f} | "
            f"{vsm.vehicle_speed:<10.1f}"
        )

        # Görsel izlenebilirlik için kısa gecikme
        time.sleep(0.4)

    print("=" * 70)
    print(" ✅ SİMÜLASYON BAŞARIYLA TAMAMLANDI")
    print("=" * 70)

if __name__ == "__main__":
    run_simulation()