# Audio Signal Filtering Project

## Overview:
This project demonstrates how to generate a noisy sinusoidal signal and apply a **band-pass filter** to remove unwanted frequencies, thereby cleaning up the signal. The code consists of two parts: one to generate and save a noisy audio file, and the other to apply a band-pass filter to this noisy signal, saving the output as a filtered WAV file.

---

## **2. `dsp.py`**

### Description:
The second script, dsp.py, reads the noisy audio file generated in the previous script, applies a band-pass filter, and saves the filtered signal to a new file. This process isolates the frequencies of interest while removing noise outside the specified frequency range.

###Key Features:

- **Band-Pass Filtering**: A band-pass filter is applied to the noisy signal, with customizable cutoff frequencies for low and high frequencies (300 Hz and 3000 Hz, respectively).
- **Signal Processing**: The audio signal is processed using SciPy's butter filter and filtfilt function, which applies the filter in both forward and reverse directions for zero-phase distortion.
- **File Output**: The filtered signal is saved as filtered_output.wav.
- **Plotting**: A waveform comparison of the original and filtered signals is displayed.


## **2. `dsp.py`**

### Description:
The second script, dsp.py, reads the noisy audio file generated in the previous script, applies a band-pass filter, and saves the filtered signal to a new file. This process isolates the frequencies of interest while removing noise outside the specified frequency range.

### Key Features:

- **Band-Pass Filtering**: A band-pass filter is applied to the noisy signal, with customizable cutoff frequencies for low and high frequencies (300 Hz and 3000 Hz, respectively).
- **Signal Processing**: The audio signal is processed using SciPy's butter filter and filtfilt function, which applies the filter in both forward and reverse directions for zero-phase distortion.
- **File Output**: The filtered signal is saved as filtered_output.wav.
- **Plotting**: A waveform comparison of the original and filtered signals is displayed.




### Output:

A WAV file named filtered_output.wav containing the filtered signal.
A plot showing the original and filtered waveforms for comparison.

### How to Run the Code:

Step 1: Run the audio_generation.py script to create the noisy audio file (noisy_audio.wav).
Step 2: Run the dsp.py script to apply the band-pass filter and generate the filtered audio (filtered_output.wav).

### Technologies Used:

- **NumPy** : For signal creation and manipulation.
-**SciPy** : For signal filtering (band-pass filter).
-**Soundfile** : For reading and writing WAV audio files.
-**Matplotlib** : For plotting and visualizing the signals.

### Files in the Project:

audio_generation.py: Script to generate and save a noisy sine wave signal.
dsp.py: Script to apply a band-pass filter and save the filtered signal.


### Output:

A WAV file named filtered_output.wav containing the filtered signal.
A plot showing the original and filtered waveforms for comparison.

### How to Run the Code:

Step 1: Run the audio_generation.py script to create the noisy audio file (noisy_audio.wav).
Step 2: Run the dsp.py script to apply the band-pass filter and generate the filtered audio (filtered_output.wav).

### Technologies Used:

NumPy: For signal creation and manipulation.
SciPy: For signal filtering (band-pass filter).
Soundfile: For reading and writing WAV audio files.
Matplotlib: For plotting and visualizing the signals.

### Files in the Project:

audio_generation.py: Script to generate and save a noisy sine wave signal.
dsp.py: Script to apply a band-pass filter and save the filtered signal.


### Code Highlights:
```python

# Band-pass filter design
b, a = signal.butter(order, [low, high], btype='band')

# Apply the band-pass filter
filtered_signal = signal.filtfilt(b, a, y)

# Save filtered signal to a WAV file
sf.write(output_file, filtered_signal, sr)
