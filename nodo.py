"""Nodo genérico usado por la cola y la pila."""


class Nodo:
    """'dato' guarda una referencia a una solicitud."""

    def  __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        