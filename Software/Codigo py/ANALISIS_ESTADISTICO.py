import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import shapiro
import os

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

# Ruta a la carpeta donde están los archivos .txt
carpeta = 'PROYECTO'  # Cambia esta ruta según la ubicación de tu carpeta

# Listar todos los archivos .txt en la carpeta
archivos_txt = [f for f in os.listdir(carpeta) if f.endswith('.txt')]

# Diccionario para almacenar los valores RMS y las estadísticas descriptivas
rms_values = {}
estadisticas_dict = {}

for archivo in archivos_txt:
    ruta_archivo = os.path.join(carpeta, archivo)
    emg_data = leer_convertir_emg(ruta_archivo)
    
    # Dividir la señal en segmentos (por ejemplo, 10 segmentos)
    n_segmentos = 10
    segment_length = len(emg_data) // n_segmentos

    rms_values[archivo] = []
    for i in range(n_segmentos):
        segment = emg_data[i*segment_length:(i+1)*segment_length]
        rms_value = calcular_rms(segment)
        rms_values[archivo].append(rms_value)

    # Calcular estadísticas descriptivas
    df_rms = pd.DataFrame({'RMS': rms_values[archivo]})
    estadisticas = df_rms.describe().transpose()
    estadisticas['Coef de Variación'] = estadisticas['std'] / estadisticas['mean']
    estadisticas = estadisticas.applymap(lambda x: f'{x:.5g}')  # Formatear a cinco cifras significativas
    estadisticas_dict[archivo] = estadisticas

# Crear DataFrame con todos los valores RMS
df_rms_total = pd.DataFrame(rms_values)

# Generar el diagrama de caja y bigotes para todos los archivos
plt.figure(figsize=(12, 6))
df_rms_total.boxplot()
plt.title('Diagrama de Caja y Bigotes de Valores RMS de Señales EMG')
plt.ylabel('Valores RMS')
plt.xlabel('Archivos')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Crear una tabla con las estadísticas descriptivas
estadisticas_completas = pd.concat(estadisticas_dict, keys=estadisticas_dict.keys())
print("\nEstadísticas Descriptivas de los Valores RMS:")
print(estadisticas_completas)


# Crear una tabla visual con las estadísticas descriptivas
fig, ax = plt.subplots(figsize=(12, 6))  # ajustar el tamaño de la tabla
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=estadisticas_completas.values, colLabels=estadisticas_completas.columns, rowLabels=estadisticas_completas.index, loc='center')

# Ajustar el tamaño de la fuente de la tabla
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.2)  # ajustar la escala de la tabla

plt.show()
