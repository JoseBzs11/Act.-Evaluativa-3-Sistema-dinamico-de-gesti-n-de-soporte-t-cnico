"""Nodo de la lista enlazada: contiene los datos de la solicitud
y la referencia al siguiente nodo."""


class Solicitud:
    def __init__(self, codigo, usuario, descripcion, prioridad):
        self.codigo = codigo
        self.usuario = usuario
        self.descripcion = descripcion
        self.prioridad = prioridad           #Alta Media o Baja
        self.estado = "PENDIENTE"            #PENDIENTE, ATENDIDA, CANCELADA
        self.tecnico = "Sin asignar"
        self.siguiente = None                # Referenciaal siguiente nodo

    def mostrar(self):
        print(f"   código:     {self.codigo}")
        print(f"   Usuario:    {self.usuario}")
        print(f"   Problema:   {self.descripcion}")
        print(f"   Prioridad:  {self.prioridad}")
        print(f"   Estado:     {self.estado}")
        print(f"   Técnico:    {self.tecnico}")