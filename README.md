# Audio Signal Filtering Project

## Overview:
This project demonstrates how to generate a noisy sinusoidal signal and apply a **band-pass filter** to remove unwanted frequencies, thereby cleaning up the signal. The code consists of two parts: one to generate and save a noisy audio file, and the other to apply a band-pass filter to this noisy signal, saving the output as a filtered WAV file.

---

## **1. `audio_generation.py`**

### Description:
The first script, `audio_generation.py`, generates a sinusoidal signal (a pure tone) and adds **white Gaussian noise** to it, creating a noisy audio signal. The signal is then saved as a WAV file.

### Key Features:
- **Signal Generation**: A clean sine wave is generated at a frequency of 440 Hz (A4 note), with adjustable amplitude and duration.
- **Noise Addition**: White Gaussian noise is added to the clean signal to simulate a noisy environment.
- **File Output**: The noisy signal is saved as `noisy_audio.wav`, which can be used for further processing or analysis.
- **Plotting**: The clean and noisy signals are plotted over time for visual comparison.

### Output:

A WAV file named noisy_audio.wav containing the noisy signal.
A plot showing the clean and noisy signals.


### Code Highlights:
```python

# Generate a clean sine wave signal
clean_signal = amplitude * np.sin(2 * np.pi * freq * t)

# Add white Gaussian noise
noise = noise_amplitude * np.random.normal(0, 1, clean_signal.shape)

# Save noisy signal to a WAV file
sf.write("noisy_audio.wav", noisy_signal, sampling_rate)



