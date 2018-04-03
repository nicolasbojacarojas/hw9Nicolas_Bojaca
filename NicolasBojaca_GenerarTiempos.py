#Ayuda para calcular los tiempos para poder generar los numeros de la serie de fibonacci
import time
t0 = time.time()
t1 = time.time() - t0
#Funcion que genera los numeros de la serie de fibonacci dado un numero
def fibonacci(N):
	if (N == 0 or N == 1):
		return (N)
	else:
		return (fibonacci(N-1) + fibonacci(N-2))
N = 35 #Variable que guarda la cantidad de numeros que necesito de la serie de fibonacci
for i in range(N): #Iteraciones sobre la funcion fibonacci para imprimir los tiempos y los numeros de la serie.
	print (fibonacci(i), t1)
