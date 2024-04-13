import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Definición de las funciones de filtro
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Parámetros del filtro
order = 6
fs = 1000       # frecuencia de muestreo, Hz
cutoff = 10     # frecuencia de corte deseada del filtro, Hz

# Asegúrate de que esta ruta sea correcta
file_path = 'nuestraseñal.txt'

# Carga los datos desde el archivo
df = pd.read_csv(file_path, delimiter='\t', header=None, skiprows=10)
df['Time'] = df.index / fs  # Crea una columna de tiempo asumiendo una frecuencia de muestreo constante

# Aplicar el filtro
filtered_signal = butter_lowpass_filter(df.iloc[:, 5], cutoff, fs, order)

# Graficar la señal filtrada
plt.figure(figsize=(12, 6))
plt.plot(df['Time'], filtered_signal, label='Señal Filtrada A1')
plt.title('Signal from A1 after Lowpass Filtering')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()


