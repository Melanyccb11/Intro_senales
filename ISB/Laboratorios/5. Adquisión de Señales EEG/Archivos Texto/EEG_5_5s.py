import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Given parameters
Fs = 1000  # Sampling frequency
n = 10 * Fs  # Number of points (10s of data)

# Butterworth filter parameters
lowcut = 13.0  # Low cut frequency in Hz for Beta band (13-30Hz)
highcut = 30.0  # High cut frequency in Hz for Beta band (13-30Hz)
order = 5  # Filter order

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Load the EEG signal from the uploaded file
filename = 'EEG_5_5s.txt'
array = np.genfromtxt(filename, delimiter='\t', skip_header=3)

# Extract the EEG signal column
signal = array[:, 5]  # Assume column index 5 contains EEG data

# Trim the signal to the first 10 seconds
signal = signal[:n]

# Center the signal around 0 by subtracting the mean
signal_centered = signal - np.mean(signal)

# Apply the Butterworth bandpass filter to get Beta band
filtered_signal = butter_bandpass_filter(signal_centered, lowcut, highcut, Fs, order)

# Time vector
t = np.arange(0, n) / Fs

# Plot the filtered signal
plt.figure(figsize=(12, 6))
plt.plot(t, filtered_signal, label='Beta band (13-30Hz) - EEG Signal')
plt.grid(linestyle=':')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (uV)')
plt.legend(loc='upper right')
plt.title('Filtered EEG Signal from 0 to 10 seconds')
plt.show()

