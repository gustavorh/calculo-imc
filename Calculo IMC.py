# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:27:37 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# Función que calculará el IMC según el peso y altura entregados por el usuario


def imc(p, a):  # Parametros 'p' (peso) y 'a' (altura)
    return p / (a**2)


peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Se entregan los valores del usuario a la función para calcular el IMC
resultado = imc(peso, altura)
print(f"Tu IMC es de: {resultado}")

# Serie de condiciones que determinará si tiene un peso normal o no, según el resultado obtenido
# de la función para calcular el IMC
if (resultado < 16):
    print("Tienes una delgadez severa")
elif (resultado < 17):
    print("Tienes una delgadez moderada")
elif (resultado < 18.5):
    print("Tienes una delgadez aceptable")
elif (resultado < 25):
    print("Tienes un peso normal")
elif (resultado < 30):
    print("Tienes sobrepeso")
elif (resultado < 35):
    print("Tienes obesidad")
else:
    print("Tienes obesidad morbida")
