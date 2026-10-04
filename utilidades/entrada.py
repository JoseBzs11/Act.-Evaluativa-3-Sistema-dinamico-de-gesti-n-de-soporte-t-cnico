def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("No puede quedar vacío")


def leer_prioridad(mensaje="Prioridad (Alta/Media/Baja): "):
    while True:
        p = input(mensaje).strip().capitalize()
        if p in ["Alta", "Media", "Baja"]:
            return p
        print("Escribe: Alta, Media o Baja")


def confirmar(mensaje="¿Confirmar? (S/N): "):
    while True:
        r = input(mensaje).strip().upper()
        if r in ["S", "N"]:
            return r == "S"
        print("Responde S o N")


def pausar(mensaje):
    input("\nPresiona Enter para continuar...")

def mostrar_menú():
    print("\n" + "=" * 40)
    print("    SISTEMA DE SOPORTE TÉCNICO")
    print("=" * 40)
    print(" 1. Registrar solicitud")
    print(" 2. Mostrar pendientes")
    print(" 3. Buscar solicitud")
    print(" 4. Atender solicitud")
    print(" 5. Cancelar solicitud")
    print(" 6. Ver historial")
    print(" 7. Deshacer última atención")
    print(" 8. Ver estadísticas")
    print(" 9. Salir")
    print("=" * 40)
