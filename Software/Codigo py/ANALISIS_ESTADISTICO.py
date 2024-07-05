import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# Función para leer y convertir la señal EMG desde un archivo TXT
def leer_convertir_emg(archivo_txt):
    datos_emg = np.loadtxt(archivo_txt)
    emg = datos_emg[:, 5]  # Sexta columna
    
    # Convertir a milivoltios (mV)
    emg_mV = emg * (3.3 / 1024)  # Suponiendo que la señal esté en un rango de 0-3.3V y se use un ADC de 10 bits

    # Aplicar un offset para centrar la señal
    emg_mV = emg_mV - np.mean(emg_mV)
    return emg_mV

# Función para calcular el RMS de una señal
def calcular_rms(signal):
    return np.sqrt(np.mean(np.square(signal)))

# Ruta al archivo TXT
ruta_archivo_txt = 'PROYECTO/Sujeto1.txt'  # Cambia esta ruta a la ubicación de tu archivo

# Leer y convertir la señal EMG
emg_data = leer_convertir_emg(ruta_archivo_txt)

# Dividir la señal en segmentos (por ejemplo, 10 segmentos)
n_segmentos = 10
segment_length = len(emg_data) // n_segmentos

rms_values = []
for i in range(n_segmentos):
    segment = emg_data[i*segment_length:(i+1)*segment_length]
    rms_value = calcular_rms(segment)
    rms_values.append(rms_value)

# Crear un DataFrame con los valores RMS
df_rms = pd.DataFrame({'RMS': rms_values})

# Generar el diagrama de caja y bigotes
plt.figure(figsize=(12, 6))
df_rms.boxplot(column=['RMS'])
plt.title('Diagrama de Caja y Bigotes de Valores RMS de Señales EMG')
plt.ylabel('Valores RMS')
plt.xlabel('Segmentos')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Calcular estadísticas descriptivas
estadisticas = df_rms.describe().transpose()
estadisticas['Coeficiente de Variación'] = estadisticas['std'] / estadisticas['mean']
print("\nEstadísticas Descriptivas de los Valores RMS:")
print(estadisticas)

# Realizar la prueba de Shapiro-Wilk para verificar la normalidad
stat, p_value = shapiro(df_rms['RMS'])
print(f"\nPrueba de Shapiro-Wilk para la Normalidad de los Valores RMS:")
print(f"Estadístico: {stat}, Valor-p: {p_value}")

# Interpretar los resultados de la prueba de Shapiro-Wilk
alpha = 0.05
if p_value > alpha:
    print("Los datos siguen una distribución normal (no se rechaza H0).")
else:
    print("Los datos no siguen una distribución normal (se rechaza H0).")

# Crear una tabla con las estadísticas descriptivas
fig, ax = plt.subplots(figsize=(12, 3))  # ajustar el tamaño de la tabla
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=np.round(estadisticas.values, 5), colLabels=estadisticas.columns, rowLabels=estadisticas.index, loc='center')

# Ajustar el tamaño de la fuente de la tabla
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1)  # ajustar la escala de la tabla

plt.show()
