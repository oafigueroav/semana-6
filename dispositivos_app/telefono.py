from modelos.dispositivo import DispositivoElectronico

class Telefono(DispositivoElectronico):
    def __init__(self, marca: str, modelo: str, numero: str):
        super().__init__(marca, modelo)  # herencia + reutilización
        self.numero = numero

    def encender(self) -> str:  # sobreescritura (polimorfismo)
        self._cambiar_estado(True)
        return f"Teléfono {self.marca} {self.modelo} encendido. Línea: {self.numero}"