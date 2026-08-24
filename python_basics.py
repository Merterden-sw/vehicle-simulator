# python_basics.py - 3. Görev Çalışması
import math

# 1. Temel Veri Tipleri
vehicle_speed: float = 85.5          # Araç hızı (float)
ignition_on: bool = True             # Kontak durumu (bool)
engine_rpm: int = 2200               # Motor devri (int)
vehicle_model: str = "Sedan V6"      # Model ismi (str)

# 2. Liste (list) Örneği
signal_names: list[str] = ["speed_kph", "engine_rpm", "coolant_temp_c"]

# 3. Sözlük (dictionary) Örneği
signal_units: dict[str, str] = {
    "speed_kph": "km/h",
    "engine_rpm": "rpm",
    "coolant_temp_c": "°C"
}

# 4. Özel Değerler (None, NaN, Infinity)
sensor_reading = None                # Veri yok / Henüz okunmadı
faulty_value = float("nan")          # Not a Number (Geçersiz hesaplama)
max_limit_exceeded = float("inf")    # Pozitif sonsuzluk

# 5. Ekrana Bastırma ve Tip Gösterimi
print("--- Araç Veri Tipleri ---")
print(f"Araç Hızı: {vehicle_speed} -> Tipi: {type(vehicle_speed)}")
print(f"Kontak Açık mı?: {ignition_on} -> Tipi: {type(ignition_on)}")
print(f"Sinyal Listesi: {signal_names} -> Tipi: {type(signal_names)}")
print(f"Sinyal Birimleri: {signal_units} -> Tipi: {type(signal_units)}")
print(f"Sensör Okuması: {sensor_reading} -> Tipi: {type(sensor_reading)}")

# 6. bool - int İlişkisi
print("\n--- bool ve int İlişkisi ---")
print("True + True Değeri:", True + True)
print("isinstance(True, int):", isinstance(True, int))
