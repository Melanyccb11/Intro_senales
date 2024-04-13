# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:51:42 2024

@author: user
"""

#Luis Contraido

import numpy as np
import matplotlib.pyplot as plt

# Nombre de tu archivo TXT
archivo_txt = "text_EMG.txt"

# Cargar los datos desde el archivo TXT
datos_emg = np.loadtxt(archivo_txt)

# Extraer la sexta columna de datos_emg
# recordamos que el archivo txt me da informacion de todas las entradas del bitalino pero 
# la única que nos interesa es la que se encuentra en el encabezado A1
columna_sexta = datos_emg[:, 5]  # El índice 5 representa la sexta columna (0-indexed)

# Crear un arreglo de tiempo en segundos
frecuencia_muestreo = 1000  # Frecuencia de muestreo en Hz
tiempo = np.arange(len(columna_sexta)) / frecuencia_muestreo

# Definir el intervalo de tiempo que deseas graficar (segundos 6 al 7)
inicio_segundo = 6
fin_segundo = 7
inicio_muestra = int(inicio_segundo * frecuencia_muestreo)
fin_muestra = int(fin_segundo * frecuencia_muestreo)

# Extraer los datos del intervalo de tiempo especificado
tiempo_intervalo = tiempo[inicio_muestra:fin_muestra]
columna_intervalo = columna_sexta[inicio_muestra:fin_muestra]

# Crear el gráfico
plt.figure(figsize=(10, 4))  # Ajusta el tamaño del gráfico según tus necesidades
plt.plot(tiempo, columna_sexta, lw=1, color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor EMG ')
plt.title('Datos de EMG (Juan Jose contraido)')
plt.grid(True)

# Mostrar el gráfico
plt.show()


# Crear el gráfico para los datos del intervalo de tiempo especificado
plt.figure(figsize=(10, 4))  # Ajusta el tamaño del gráfico según tus necesidades
plt.plot(tiempo_intervalo, columna_intervalo, lw=1, color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor EMG (Sexta Columna)')
plt.title('Ampliacion del EMG contraido')
plt.grid(True)

# Mostrar el gráfico
plt.show()
