"""Lógica del sistema: coordibna list, cola, pila."""
from modelos.solicitud import Solicitud
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.cola import Cola
from estructuras.pila import Pila
from utilidades.entrada import leer_texto, leer_prioridad, confirmar

class SistemaSoporte:
    def  __init__(self):
        self.pendientes = ListaEnlazada()  # lista enlazada de pendientes
        self.cola = Cola()                 # Orden FIFO de atención
        self.historial = Pila()            # pila de atendidos
        self.canceladas = ListaEnlazada()  # lista de canceladas

    def buscar_en_todo(self,codigo):
        """Busca pendientes, historial, y cfanceladas."""
        encontrada = self.pendientes.buscar(codigo) 
        if encontrada is None:
            encontrada = self.historial.buscar(codigo) 
        if encontrada is None:
            encontrada = self.canceladas.buscar(codigo)
        return encontrada

    # Opción 1
    def registrar(self):
        print("\n --- REGISTRAR SOLICITUD ---")
        codigo = leer_texto("codigo:")
        if self.buscar_en_todo(codigo) is not None:
            print("Error: ya existe una solicitud con ese codigo.")
            return
        usuario = leer_texto("Usuario: ")
        descripcion = leer_texto("Descripcion del problema: ")
        prioridad = leer_prioridad()


        nueva = Solicitud(codigo, usuario, descripcion, prioridad)
        self.pendientes.insertar_final(nueva)
        self.cola.encolar(nueva)
        print("Solicitud registrada correctamente.")

    # Opcion 2
    def mostrar_pendientes(self):
        self.pendientes.mostrar("SOLICITUDES PENDIENTES")

    # oPCION 3
    def buscar(self):
        print("\n--- BUSCAR SOLICITUD ---")
        codigo = leer_texto("Código a buscar: ")
        s = self.buscar_en_todo(codigo)
        if s is None:
            print("Solicitud no encontrada.")
        else:
            print("\n Solicitud encontrada: ")
            s.mostrar()

    # Opcion 4
    def atender(self):
        print("\n--- ATENDER SIGUIENTE SOLICITUD ---")
        if self.cola.esta_vacia():
            print("No hay solicitudes pendientes por atender.")
            return
        tecnico = leer_texto("Nombre del técnico que atiente: ")

        solicitud = self.cola.desencolar()            #1. Sale de la cola
        self.pendientes.eliminar(solicitud.codigo)    #2. sale de pendientes
        solicitud.estado = "ATENDIDA"                 #3. actualizar estado
        solicitud.tecnico = tecnico                   #4. registrar técnico
        self.historial.apilar(solicitud)              #5. pila de historial

        print("\nAtendiendo solicitud...")
        print(f"Código: {solicitud.codigo}")
        print(f"Usuario: {solicitud.usuario}")
        print(f"Prioridad: {solicitud.prioridad}")
        print(f"Técnico: {solicitud.tecnico}")
        print("Solicitud atendida correctamente.")

    # Opcion 5
    def cancelar(self):
        print("\n--- CANCELAR SOLICITUD ---")
        codigo = leer_texto("Código de la solicitud pendiente:")
        solicitud = self.pendientes.buscar(codigo)
        if solicitud is None:
            print("No existe una solicitud pendiente con este codigo.")
            return
        print("\nSolicitud encontrada.")
        solicitud.mostrar()
        if not confirmar("\n¿Desea cancelarla? S/N: "):
            print("Operación cancelada por el usuario.")
            return

        self.pendientes.eliminar(codigo)     # manipulando enlaces
        self.cola.eliminar(codigo)
        solicitud.estado = "CANCELADA"
        self.canceladas.insertar_final(solicitud)
        print(f"L solicitud {codigo} fue CANCEADA.")

    # Opcion 6
    def mostrar_historial(self):
        self.historial.mostrar()

    # Opcion 7
    def deshacer(self):
        print("\n--- DESHACER ÚLTIMA ATENDCIÓN---")
        if self.historial.esta_vacia():
            print("No hay atenciones para deshacer.")
            return
        ultima = self.historial.tope()
        print("Última atencion: ")
        print(f"Código: {ultima.codigo}")
        print(f"Usuario: {ultima.usuario}")
        if not confirmar("¿Desea deshacer esta atencion? S/N"):
            print("No se deshizo ninguna atencion.")
            return

        solicitud = self.historial.desapilar()
        solicitud.estado = "PENDIENTE"
        solicitud.tecnico = "Sin asignar"
        self.pendientes.insertar_inicio(solicitud)
        self.cola.encolar_al_frente(solicitud)
        print(f"La solicitud fue deshecha.")
        print(f"La solicitud {solicitud.codigo} regreso a pendientes.") 

    # Opcion 8
    def estadisticas(self):
        pend = self.pendientes.tamano
        aten = self.historial.tamano
        canc = self.canceladas.tamano
        total = pend + aten + canc

        print("\n" + "+" * 33)
        print(" ESTADÍSTICAS")
        print("+" * 33) 
        print(f"Total registradas:  {total}") 
        print(f"Pendientes:         {pend}")
        print(f"Atendidas:          {aten}")
        print(f"Canceladas:         {canc}")
        print(f"Prioridad alta:  {self._contar('Alta')}")
        print(f"Prioridad media: {self._contar('Media')}")
        print(f"Prioridad baja:  {self._contar('Baja')}")

    def _contar(self, prioridad):
        return (self.pendientes.contar_prioridad(prioridad) 
                + self.historial.contar_prioridad(prioridad)
                + self.canceladas.contar_prioridad(prioridad))
    
