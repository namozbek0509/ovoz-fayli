# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RnLn7mLepWHuB3yaYOLIWQ2bjYQDxck8
"""

!pip install pydub librosa

import requests
import librosa
import librosa.display
import matplotlib.pyplot as plt
from pydub import AudioSegment
from io import BytesIO

url = "https://www2.cs.uic.edu/~i101/SoundFiles/CantinaBand3.wav"
response = requests.get(url)
audio = AudioSegment.from_file(BytesIO(response.content))

samples = audio.get_array_of_samples()
y, sr = librosa.load(BytesIO(audio.export(format='wav').read()), sr=None)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')
plt.show()