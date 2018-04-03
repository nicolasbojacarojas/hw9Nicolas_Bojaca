import numpy as np
import matplotlib.pyplot as plt
npp = np.genfromtxt('times_cpp.csv', delimiter=" ")#Carga los archivos generados por el archivo .cpp
Npp = npp[:,0]#toma los valores de la serie de fibonacci(cpp) 
tpp = npp[:,1]#toma los valores de los tiempos en los cuales se generan(cpp)
pyt = np.genfromtxt('times_python.csv', delimiter=" ")#Carga los archivos generados por el archivo.py
Npy = pyt[:,0]#toma los valores de la serie de fibonacci(.py)
tpy = pyt[:,1]#toma los valores de los tiempos en los cuales se generan los numeros de la serie fibonacci(.py)
plt.plot(Npp, tpp, label = "datos de c++")
plt.plot(Npy, tpy, label = "datos de python")
plt.legend()
plt.show()
