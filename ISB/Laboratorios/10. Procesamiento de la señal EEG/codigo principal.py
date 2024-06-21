# -*- coding: utf-8 -*-


A4:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import mne
import pywt

# Define la ruta completa del archivo EEG
eeg_file_path = 'D:/2024-1/Introduccion a Señales Biomedicas/LABS/LAB 11/brain_signals/brain_signals2/Experiment_1/A4/EEG_recording.csv'

# Cargar el archivo de EEG utilizando punto y coma como delimitador
eeg_data = pd.read_csv(eeg_file_path, sep=';')

# Ajustar los valores del eje x para que comiencen en 0
eeg_data['timestamps'] -= eeg_data['timestamps'].min()

# Definir el filtro pasa banda
def bandpass_filter(data, lowcut, highcut, fs, order=2):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

# Función para normalizar la señal usando MNE
def normalize_signal_mne(signal):
    info = mne.create_info(ch_names=['EEG'], sfreq=fs, ch_types=['eeg'])
    raw = mne.io.RawArray(signal.reshape(1, -1), info)
    raw.filter(None, 30., fir_design='firwin')
    return raw.get_data().flatten()

# Función para calcular la FFT y su magnitud en dB
def calculate_fft(signal, fs):
    N = len(signal)
    signal_fft = np.fft.fft(signal, N)
    signal_fft = np.abs(signal_fft)[:N//2] * (2/N)
    signal_fft_db = 20 * np.log10(signal_fft / np.max(signal_fft))
    freqs = np.fft.fftfreq(N, 1/fs)[:N//2]
    return freqs, signal_fft_db

def calculate_snr(signal, noise):
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr


# Parámetros del filtro
fs = 256.0  # Frecuencia de muestreo (Hz)
lowcut = 3.0  # Frecuencia de corte baja (Hz)
highcut = 30.0  # Frecuencia de corte alta (Hz)

# Aplicar los filtros a las señales EEG
signals = ['TP9', 'AF7', 'AF8', 'TP10', 'Right AUX']
filtered_data = {}
raw_data = {}

for signal in signals:
    eeg_signal = eeg_data[signal].values
    filtered_signal = bandpass_filter(eeg_signal, lowcut, highcut, fs)
    normalized_signal = normalize_signal_mne(filtered_signal)
    filtered_data[signal] = normalized_signal
    raw_data[signal] = eeg_signal

# Crear la figura y los subplots para las señales sin filtrar
fig_raw, axs_raw = plt.subplots(len(signals), 1, figsize=(15, 20), sharex=True)

# Graficar cada señal sin filtrar en un subplot diferente
for i, signal in enumerate(signals):
    axs_raw[i].plot(eeg_data['timestamps'] / fs, raw_data[signal], label=f'{signal} (Raw)')
    axs_raw[i].set_ylabel('EEG Signal (uV)')
    axs_raw[i].set_xlabel('Time (s)')
    axs_raw[i].set_title(f'Raw EEG Signal from {signal}')
    axs_raw[i].legend()
    axs_raw[i].grid(True)

axs_raw[-1].set_xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Crear la figura y los subplots para las señales filtradas y normalizadas
fig_filtered, axs_filtered = plt.subplots(len(signals), 1, figsize=(15, 20), sharex=True)

# Graficar cada señal filtrada y normalizada en un subplot diferente
for i, signal in enumerate(signals):
    axs_filtered[i].plot(eeg_data['timestamps'] / fs, filtered_data[signal], label=f'{signal} (Filtered)')
    axs_filtered[i].set_ylabel('EEG Signal (uV)')
    axs_filtered[i].set_xlabel('Time (s)')
    axs_filtered[i].set_title(f'Filtered and Normalized EEG Signal from {signal}')
    axs_filtered[i].legend()
    axs_filtered[i].grid(True)

axs_filtered[-1].set_xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Crear la figura y los subplots para las FFT
fig_fft, axs_fft = plt.subplots(len(signals), 1, figsize=(15, 20), sharex=True)

for i, signal in enumerate(signals):
    freqs, fft_db = calculate_fft(filtered_data[signal], fs)
    axs_fft[i].plot(freqs, fft_db, label=signal, color='red')
    axs_fft[i].set_ylabel('Magnitude (dB)')
    axs_fft[i].set_xlabel('Frequency (Hz)')
    axs_fft[i].set_title(f'FFT of Filtered and Normalized EEG Signal from {signal}')
    axs_fft[i].legend()
    axs_fft[i].grid(True)

axs_fft[-1].set_xlabel('Frequency (Hz)')
plt.tight_layout()
plt.show()

# Detección de ERP (Event-Related Potentials)
# Simulación de carga de datos para detección de ERP
signal_eeg_1 = raw_data['TP9']
signal_eeg_2 = raw_data['AF7']
signal_eeg_3 = raw_data['AF8']
signal_eeg_4 = raw_data['TP10']

# Generando los ejes de tiempo
time_eeg_1 = np.arange(len(signal_eeg_1)) / fs
time_eeg_2 = np.arange(len(signal_eeg_2)) / fs
time_eeg_3 = np.arange(len(signal_eeg_3)) / fs
time_eeg_4 = np.arange(len(signal_eeg_4)) / fs

# Detección de ERP
fig_erp, axs_erp = plt.subplots(4, 1, figsize=(15, 20), sharex=True)

axs_erp[0].plot(time_eeg_1/1000, signal_eeg_1, label="Acoustic Stimuli RAW", color="pink")
axs_erp[0].set_ylabel("Value RAW")
axs_erp[0].set_xlabel("Time (s)")
axs_erp[0].set_title("ERP of TP9")
axs_erp[0].legend()
axs_erp[0].grid(True)

axs_erp[1].plot(time_eeg_2/1000, signal_eeg_2, label="Acoustic Stimuli RAW", color="pink")
axs_erp[1].set_ylabel("Value RAW")
axs_erp[1].set_xlabel("Time (s)")
axs_erp[1].set_title("ERP of AF7")
axs_erp[1].legend()
axs_erp[1].grid(True)

axs_erp[2].plot(time_eeg_3/1000, signal_eeg_3, label="Acoustic Stimuli RAW", color="pink")
axs_erp[2].set_ylabel("Value RAW")
axs_erp[2].set_xlabel("Time (s)")
axs_erp[2].set_title("ERP of AF8")
axs_erp[2].legend()
axs_erp[2].grid(True)

axs_erp[3].plot(time_eeg_4/1000, signal_eeg_4, label="Acoustic Stimuli RAW", color="pink")
axs_erp[3].set_ylabel("Value RAW")
axs_erp[3].set_xlabel("Time (s)")
axs_erp[3].set_title("ERP of TP10")
axs_erp[3].legend()
axs_erp[3].grid(True)

axs_erp[-1].set_xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Obtener coeficientes usando Wavelets
def wavelet_transform(signal, wavelet='db4', level=5):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    return coeffs

# Visualizar los coeficientes de wavelet
for signal in signals:
    coeffs = wavelet_transform(filtered_data[signal])
    coeffs = [(c - np.mean(c)) / np.std(c) for c in coeffs]  # Normalización de coeficientes
    fig_wavelet, ax_wavelet = plt.subplots(len(coeffs), 1, figsize=(10, 12))
    for i in range(len(coeffs)):
        ax_wavelet[i].plot(np.arange(len(coeffs[i])) / 1000, coeffs[i])
        ax_wavelet[i].set_ylabel('Coefficient value (Normalized)')
        ax_wavelet[i].set_xlabel('Number of coefficients')
        ax_wavelet[i].set_title(f'Level {i+1} - Normalized Coefficients of {signal}')
    plt.tight_layout()
    plt.show()

# Calcular el SNR de las señales filtradas
snr_values = {}
for signal in signals:
    noise = raw_data[signal] - filtered_data[signal]  # Estimación del ruido
    snr = calculate_snr(filtered_data[signal], noise)
    snr_values[signal] = snr
    print(f'SNR for {signal}: {snr:.2f} dB')