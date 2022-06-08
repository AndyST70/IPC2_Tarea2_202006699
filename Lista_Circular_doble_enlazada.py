from datos import Nodo
class ListaCircularDoble:
    def __init__(self):
        self.inicio = None 
        self.final = None
    def vacia(self):
        if self.inicio == None:
            return True
        else:
            return False
    def agregar_inicio(self, id):
        if self.vacia():#!verificamos si esta vaicia
            self.inicio = self.final = Nodo(id)
        else: 
            #? este va ser el primero y acceede
            temporal = Nodo(id)
            temporal.siguiente = self.inicio
            #? realizamos el enlace con el nodo aux
            self.inicio.anterior = temporal
            self.inicio = temporal
        self.__unir_nodos()
    def agregar_final(self, id):
        if self.vacia():
            self.inicio = self.final = Nodo(id)
        else:
            temporal = self.final
            self.final = temporal.siguiente = Nodo(id)
            self.final.anterior = temporal
        self.__unir_nodos()
            #! al colocar __ decimos que es un metodo privado
    def __unir_nodos(self):
        self.inicio.anterior = self.final
        self.final.siguiente = self.inicio
    def recorre_inicio_a_fin(self):
        temporal = self.inicio
        while temporal:
            print(temporal.id)
            temporal = temporal.siguiente
            if temporal == self.inicio:
                break
    def recorrer_fin_a_inicio(self):
        temporal = self.final
        while temporal:
            print(temporal.id)
            temporal = temporal.anterior
            if temporal ==self.final:
                break
    #TODO metodos de apoyo

    def eliminar_inicio(self):
        if self.vacia():
            print("Tu estructura esta vacia")
        elif self.inicio == self.final:
            self.inicio = self.final = None
        else:
            self.inicio = self.inicio.siguiente
        self.__unir_nodos()

    def eliminar_ultimo_nodo(self):
        if self.vacia():
            print("Tu estructura esta vacia")
        elif self.inicio == self.final:
            self.inicio = self.final = None
        self.__unir_nodos()

