"""Punto de entrada - Centro de Soporte Técnico
Algoritmos 2 - act.  Evaluativa 3. """
from servicios.sistema_soporte import SistemaSoporte
from utilidades.entrada import mostrar_menú


def main():
    sistema = SistemaSoporte()
    while True:
        mostrar_menú()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            sistema.registrar()
        elif opcion == "2":
            sistema.mostrar_pendientes()
        elif opcion == "3":
            sistema.buscar()
        elif opcion == "4":
            sistema.atender()
        elif opcion == "5":
            sistema.cancelar()
        elif opcion == "6":
            sistema.mostrar_historial()
        elif opcion == "7":
            sistema.deshacer()
        elif opcion == "8":
            sistema.estadisticas()
        elif opcion == "9":
            print("Saliendo del sistema.  ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if  __name__== "__main__":
    main()
            