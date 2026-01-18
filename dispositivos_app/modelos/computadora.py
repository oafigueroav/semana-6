from modelos.dispositivo import DispositivoElectronico

class Computadora(DispositivoElectronico):
    def __init__(self, marca: str, modelo: str, ram_gb: int):
        super().__init__(marca, modelo)
        self.ram_gb = ram_gb

    def encender(self) -> str:  # sobreescritura (polimorfismo)
        self._cambiar_estado(True)
        return f"Computadora {self.marca} {self.modelo} encendida con {self.ram_gb}GB RAM"