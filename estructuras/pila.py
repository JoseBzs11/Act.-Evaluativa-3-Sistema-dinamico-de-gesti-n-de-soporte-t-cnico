"""Pila LIFO implementada con nodos  (historial de atención)."""
from modelos.nodo import Nodo


class Pila:
    def  __init__(self):
        self.cima = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cima is None

    def apilar(self, solicitud):
        """O(1)."""
        nuevo = Nodo(solicitud)
        nuevo.siguiente = self.cima
        self.cima = nuevo
        self.tamano += 1

    def desapilar(self):
        """O(1)."""
        if self.esta_vacia():
            return None
        nodo = self.cima
        self.cima = nodo.siguiente
        nodo.siguiente = None
        self.tamano -= 1
        return nodo.dato

    def tope(self):
        """O(1)."""
        if self.esta_vacia():
            return None
        return self.cima.dato

    def buscar(self, codigo):
        """O(n)."""
        actual = self.cima
        while actual is not None:
            if actual.dato.codigo ==  codigo:
                return actual.dato
            actual = actual.siguiente
        return None

    def contar_prioridad(self, prioridad):
        """O(n)."""
        total = 0
        actual = self.cima
        while actual is not None:
            if actual.dato.prioridad == prioridad:
                total += 1
            actual = actual.siguiente
        return total

    def mostrar(self):
        """D la ultima atendda a la primera (LIFO). O(n)."""
        print("\n HISTORIAL DE ATENCIONES")
        print("-" * 40)
        if self.esta_vacia():
            print(" (Historial vacío)")
            return
        actual = self.cima
        posicion = 1
        while actual is not None:
            s = actual.dato
            print(f"{posicion} . Solicitud {s.codigo} - {s.usuario}"
              f"(Técnico: {s.tecnico})")
            actual = actual.siguiente
            posicion += 1

             
