from typing import List
from modelos.dispositivo import DispositivoElectronico

class InventarioDispositivos:
    def __init__(self):
        self.__dispositivos: List[DispositivoElectronico] = []  # encapsulado

    def agregar(self, d: DispositivoElectronico) -> None:
        self.__dispositivos.append(d)

    def listar(self) -> List[DispositivoElectronico]:
        # devolvemos copia para no exponer la lista interna directamente
        return list(self.__dispositivos)

    def encender_todos(self) -> None:
        # polimorfismo: todos tienen encender(), pero cada uno actúa diferente
        for d in self.__dispositivos:
            print(d.encender())

    # "sobrecarga" simulada (según tu material): argumentos opcionales
    def buscar(self, marca: str = None, modelo: str = None):
        resultados = self.__dispositivos
        if marca is not None:
            resultados = [d for d in resultados if d.marca.lower() == marca.lower()]
        if modelo is not None:
            resultados = [d for d in resultados if d.modelo.lower() == modelo.lower()]
        return resultados