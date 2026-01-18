from modelos.telefono import Telefono
from modelos.computadora import Computadora
from servicios.inventario import InventarioDispositivos

def main():
    inventario = InventarioDispositivos()

    t1 = Telefono("Samsung", "A54", "0999999999")
    c1 = Computadora("Dell", "Inspiron", 16)

    inventario.agregar(t1)
    inventario.agregar(c1)

    print("== Encendiendo todos (polimorfismo) ==")
    inventario.encender_todos()

    print("\n== Buscar por marca (simulación de sobrecarga con opcionales) ==")
    encontrados = inventario.buscar(marca="Dell")
    for d in encontrados:
        print(f"- {d.marca} {d.modelo} (encendido={d.esta_encendido()})")

if __name__ == "__main__":
    main()