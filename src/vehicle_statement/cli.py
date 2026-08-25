# src/vehicle_statement/cli.py

import time
from vehicle_statement.simulator import VehicleSimulator
from vehicle_statement.state import VehicleState


def run_cli() -> None:
    """Simülatörü terminal üzerinden canlı çalıştıran döngü."""
    print("--- Araç Telemetri Simülatörü Başlatılıyor ---")

    state = VehicleState(throttle_pedal=30.0, brake_pedal=0.0)
    simulator = VehicleSimulator(state)

    try:
        for step in range(1, 6):
            time.sleep(0.1)
            updated_state = simulator.update(dt=0.5)

            dtc_str = (
                ", ".join([d.value for d in updated_state.active_dtcs])
                if updated_state.active_dtcs
                else "YOK"
            )

            print(
                f"[Adım {step}] Hız: {updated_state.speed:.1f} km/h | "
                f"RPM: {updated_state.rpm:.0f} | "
                f"Sıcaklık: {updated_state.engine_temp:.1f}°C | "
                f"Yakıt: %{updated_state.fuel_level:.1f} | "
                f"DTC: {dtc_str}"
            )

    except Exception as e:
        print(f"Simülasyon Hatası: {e}")

    print("--- Simülasyon Tamamlandı ---")


if __name__ == "__main__":
    run_cli()