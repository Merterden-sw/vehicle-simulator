from enum import Enum, auto

class VehicleStateEnum(Enum):
    OFF = auto()
    IGNITION_ON = auto()
    ENGINE_RUNNING = auto()
    DRIVING = auto()
    SHUTDOWN = auto()

class VehicleStateMachine:
    def __init__(self):
        self.current_state = VehicleStateEnum.OFF
        self.engine_speed = 0.0   # RPM
        self.vehicle_speed = 0.0  # km/h

    def update(self, ignition: bool, accelerator_pos: float, brake_pressed: bool):
        """Guard condition'lara göre durum geçişlerini ve fiziksel kuralları uygular."""
        
        # Guard Check: Kontak kapalıysa her durumda OFF'a geç ve sıfırla
        if not ignition:
            self.current_state = VehicleStateEnum.OFF
            self._exit_actions()
            return self.current_state

        # State: OFF -> IGNITION_ON
        if self.current_state == VehicleStateEnum.OFF and ignition:
            self.current_state = VehicleStateEnum.IGNITION_ON

        # State: IGNITION_ON -> ENGINE_RUNNING (Kontak açıkken frene basılarak marş basılması)
        if self.current_state == VehicleStateEnum.IGNITION_ON and brake_pressed:
            self.current_state = VehicleStateEnum.ENGINE_RUNNING
            self.engine_speed = 800.0  # Rölanti RPM

        # State: ENGINE_RUNNING veya DRIVING (Gaza veya Frene basıldığında)
        elif self.current_state in (VehicleStateEnum.ENGINE_RUNNING, VehicleStateEnum.DRIVING):
            if accelerator_pos > 0:
                self.current_state = VehicleStateEnum.DRIVING
                self.engine_speed = 800.0 + (accelerator_pos * 40.0)
                self.vehicle_speed += accelerator_pos * 0.5
            elif brake_pressed:
                self.vehicle_speed = max(0.0, self.vehicle_speed - 15.0)
                if self.vehicle_speed == 0.0:
                    self.current_state = VehicleStateEnum.ENGINE_RUNNING
                    self.engine_speed = 800.0
            else:
                self.vehicle_speed = max(0.0, self.vehicle_speed - 1.0)
                if self.vehicle_speed == 0.0:
                    self.current_state = VehicleStateEnum.ENGINE_RUNNING
                    self.engine_speed = 800.0

        return self.current_state

    def _exit_actions(self):
        """Kabul Kriteri: Motor kapalıyken RPM ve Hız sıfıra dönmelidir."""
        self.engine_speed = 0.0
        self.vehicle_speed = 0.0