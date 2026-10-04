"""Cola FIFO implementada con nodos. """
from modelos.nodo import Nodo


class Cola:
    def  __init__(self):
        self.inicio = None
        self.final = None
        self.tamano = 0
    
    def esta_vacia(self):
        return self.inicio is None

    def encolar(self,solicitud):
        """inserta al final O(1)."""
        nuevo = Nodo(solicitud)
        if self.final is None:
            self.inicio = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamano += 1

    def encolar_al_frente(self,solicitud):
        """Usado al deshacer una atencion. O(1)."""
        nuevo = Nodo(solicitud)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo
        if self.final is None:
            self.final =nuevo
        self.tamano += 1

    def desencolar(self):
        """Retirar del frente. O(1)."""
        if self.esta_vacia():
            return None
        nodo = self.inicio
        self.inicio =  nodo.siguiente
        if self.inicio is None:
            self.final = None
        nodo.siguiente = None
        self.tamano -= 1
        return nodo.dato

    def frente(self):
        """Consulta el primero sin retirarlo. O(1). """
        if self.esta_vacia():
            return None
        return self.inicio.dato

    def eliminar(self, codigo):
        """Elimina por codigo ( al cancelar) cambiando enlaces. O(n)."""
        anterior = None
        actual = self.inicio
        while actual is not None:
            if actual.dato.codigo == codigo:
                if anterior is None:
                    self.inicio = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                if actual is self.final:
                    self.final = anterior
                actual.siguiente = None
                self.tamano -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar(self):
        """O(n)."""
        print("\nCOLA DE ATENCIÓN (frente -> final)")
        print("-" * 40)
        if  self.esta_vacia():
            print(" (Cola vacía)")
            return
        actual = self.inicio
        posicion = 1
        while actual is not None:
            s = actual.dato
            print(f"{posicion}. solicitud{s.codigo} - {s.usuario}" 
                  f"({s.prioridad})")
            actual = actual.siguiente
            posicion += 1
            