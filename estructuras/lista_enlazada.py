"""Lista enlazada simple (pendientes y canceladas).
n = cantidad de nodos. """


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_final(self,nodo):
        """O(1) gracias a la referencia 'ultimo'."""
        nodo.siguiente = None
        if self.cabeza is None:
            self.cabeza = nodo 
            self.ultimo = nodo
        else:
            self.ultimo.siguiente =  nodo
            self.ultimo = nodo
        self.tamano += 1

    def insertar_inicio(self, nodo):
        """O(1)."""
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        if self.ultimo is None :
            self.ultimo = nodo
        self.tamano += 1

    def buscar(self,codigo):
        """Busqueda Secuencial. O(n)."""
        actual = self.cabeza
        while actual is not None:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def eliminar(self, codigo):
        """Elimina manipulando los enlaces. O(n).
        Devuelve el nodo eliminado o None."""
        anterior = None
        actual = self.cabeza
        while actual is not None:
            if  actual.codigo == codigo:
                if anterior is None:                # eliminar la cabeza
                    self.cabeza = actual.siguiente
                else:                                #medio/final
                    anterior.siguiente = actual.siguiente
                if actual == self.ultimo:
                   self.ultimo = anterior
                self.tamano -= 1
                return actual
            anterior = actual
            actual = actual.siguiente
        return None

    def mostrar(self, titulo):
        """Recorrido completo. O(n). """
        print(f"\n{titulo}")
        print("-" * 40)
        if self.cabeza is None:
            print(" (No hay solicitudes)")
            return
        actual = self.cabeza
        while actual is not None:
            print(f"Código: {actual.codigo}")
            print(f"Usuario: {actual.usuario}")
            print(f"Problema: {actual.descripcion}")
            print(f"Prioridad: {actual.prioridad}")
            print()
            actual = actual.siguiente

    def contar_prioridad(self, prioridad):
        """O(n)."""
        total = 0
        actual = self.cabeza
        while actual is not None:
            if actual.prioridad == prioridad:
                total += 1
            actual = actual.siguiente
        return total


