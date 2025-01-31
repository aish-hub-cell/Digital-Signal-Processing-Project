import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Parameters
duration = 5  # seconds
sampling_rate = 44100  # Hz (standard for audio)
freq = 440  # Hz (A4 note)
amplitude = 0.5  # Volume of the signal

# Generate a clean sine wave
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
clean_signal = amplitude * np.sin(2 * np.pi * freq * t)

# Generate white Gaussian noise
noise_amplitude = 0.3  # Adjust noise level
noise = noise_amplitude * np.random.normal(0, 1, clean_signal.shape)

# Create a noisy signal
noisy_signal = clean_signal + noise

# Save the noisy signal as a WAV file
sf.write("noisy_audio.wav", noisy_signal, sampling_rate)
print("Noisy audio file 'noisy_audio.wav' has been created!")

# Plot the signals
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], clean_signal[:1000], label="Clean Signal")
plt.plot(t[:1000], noisy_signal[:1000], label="Noisy Signal", alpha=0.7)
plt.title("Generated Clean and Noisy Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
