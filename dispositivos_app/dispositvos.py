from abc import ABC, abstractmethod

class DispositivoElectronico(ABC):
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.__encendido = False  # encapsulación (estado interno)

    def esta_encendido(self) -> bool:
        return self.__encendido

    def _cambiar_estado(self, estado: bool) -> None:
        # método interno controlado (no tocar __encendido directo)
        self.__encendido = estado

    @abstractmethod
    def encender(self) -> str:
        """Polimorfismo: cada dispositivo encenderá a su manera."""
        raise NotImplementedError

    def apagar(self) -> str:
        self._cambiar_estado(False)
        return f"{self.marca} {self.modelo} apagado."
