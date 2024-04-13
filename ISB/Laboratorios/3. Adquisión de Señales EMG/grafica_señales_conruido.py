import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de cambiar esta ruta por la ruta real donde se encuentra tu archivo.
file_path = 'nuestraseñal.txt'

try:
    # Omitir las líneas del encabezado y cargar los datos
    df = pd.read_csv(file_path, delimiter='\t', header=None, skiprows=10)

    # Asumir que el tiempo está en segundos y que la frecuencia de muestreo es de 1000 Hz
    sampling_rate = 1000  # Hz
    df['Time'] = df.index / sampling_rate

    # Seleccionar la sexta columna de datos que corresponde a 'A1'
    plt.figure(figsize=(12, 6))
    plt.plot(df['Time'], df.iloc[:, 5], label='A1')  # La sexta columna es la número 5 en indexación basada en cero
    plt.title('Signal from A1')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()

except Exception as e:
    print(f"Se produjo un error: {e}")
