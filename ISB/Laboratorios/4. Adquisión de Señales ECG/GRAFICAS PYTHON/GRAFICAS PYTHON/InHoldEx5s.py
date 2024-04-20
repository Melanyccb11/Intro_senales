import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Definimos la frecuencia de muestreo
Fs = 1000
Ts = 1/Fs

# Leemos el archivo excluyendo las primeras filas del archivo
# Asegúrate de tener el archivo 'NormalBreath30s.txt' en tu directorio actual de trabajo
array = np.genfromtxt('InHoldEx5s.txt', delimiter='\t', skip_header=3)

# Extraemos la columna de la señal
# Asegúrate de que estás seleccionando la columna correcta. Aquí asumimos que es la sexta columna (índice 5)
signal = array[:, 5]

# Obtenemos la longitud de la señal para 15 segundos
n = 2 * Fs  # Queremos graficar 15 segundos de la señal

# Creamos un vector tiempo conociendo n y Ts
t = np.arange(0, n * Ts, Ts)

# Ajustamos la señal para obtener los primeros 15 segundos
signal2 = signal[:n]

# Ploteamos la lectura de los primeros 15 segundos
plt.figure(figsize=(12, 6))
plt.plot(t, signal2, label='Señal 0-15s')  # Graficamos la señal de 0 a 15 segundos
plt.grid(linestyle=':')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.title('Exhaling for 5s - EKG Signal')
plt.show()
