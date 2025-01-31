import numpy as np
import scipy.signal as signal
import soundfile as sf
import matplotlib.pyplot as plt


file_path = "noisy_audio.wav"  
y, sr = sf.read(file_path)  

if len(y.shape) > 1:
    y = y.mean(axis=1) 


def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs 
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = signal.butter(order, [low, high], btype='band')
    return signal.filtfilt(b, a, data)

low_cutoff = 300  
high_cutoff = 3000 

filtered_signal = bandpass_filter(y, low_cutoff, high_cutoff, sr)


output_file = "filtered_output.wav"
sf.write(output_file, filtered_signal, sr)


plt.figure(figsize=(10, 4))
plt.plot(y, label="Original Signal", alpha=0.7)
plt.plot(filtered_signal, label="Filtered Signal", alpha=0.7, linestyle='dashed')
plt.legend()
plt.title("Waveform Before and After Band-Pass Filtering")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

print(f"Filtered audio saved as {output_file}")
