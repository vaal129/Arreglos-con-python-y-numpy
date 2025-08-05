#formas de controlar while
"""
Identificadores o tipo de datos primitivos 
por numeros sea reales o enteros
por booleanos
por cadenas de texto

No primitivos 
listas
tuplas 
diccionarios 
sets
rangos
arreglos : vectores, matrices 
"""
#region control letra
palabra=input("Ingrese una palabra: ")
while palabra.lower()=="s":
    palabra=input("Ingrese una palabra: ")
print("Fin del ciclo while")
#endregion
#region control por FALSE O TRUE
contador=0
while True:
    if contador ==10:
        break
        print(contador)
    else:
        print("El contador no ha llegado a 10")
    contador+=1

print("El ciclo ha terminado correctamente")
contador+=1
#endregion
    