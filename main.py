import sys
from Lista_Circular_doble_enlazada import ListaCircularDoble
from os import system
system("cls")
#! Lista circuilar doblemente enlazada

lista = ListaCircularDoble()

lista.agregar_final(12)
lista.agregar_final(10)
lista.agregar_final(1)
lista.agregar_final(2)
lista.agregar_final(52)
lista.agregar_final(3)
lista.recorre_inicio_a_fin()
print("*" * 25)
lista.recorrer_fin_a_inicio()