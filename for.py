import time 
import os,sys
inicio=time.time()
for i in range(5):
    print(i)
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecucion:", tiempoFinal)
time.sleep(5)
if sys.platform=="win32":
    os.system('cls') #limpia la consola en windowa
else:
    os.system('clear')

#ciclo mientras
inicio=time.time()
contador=0
while contador<=10:
    print(contador)
    contador+=1 # contador = contador +1
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecucion:", tiempoFinal)
"""
    contador=contador +1
    0 = 0 + 1
    1 = 1 + 1
    2 = 2 + 1
    3 = 3 + 1 
    4 = 4 + 1 
    5 = 5 + 1
    6 = 6 + 1
    7 = 7 + 1
    8 = 8 + 1
    9 = 9 + 1
"""
