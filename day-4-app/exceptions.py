class SignalValidationError(Exception):
    """Araç sinyali doğrulama hataları için temel istisna sınıfı."""
    pass

class SignalOutOfRangeError(SignalValidationError):
    """Sinyal değeri tanımlı min/max sınırlarının dışına çıktığında fırlatılır."""
    pass

class InvalidSignalValueError(SignalValidationError):
    """Sinyal değeri NaN veya geçersiz veri tipi olduğunda fırlatılır."""
    pass