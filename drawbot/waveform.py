path = '/Users/michiel/Downloads/human-zoo-3-side-a.wav'

from scipy.io.wavfile import read
#import matplotlib.pyplot as plt

# read audio samples
input_data = read(path)
#print(input_data)
audio = input_data[1]
print(audio[0:12])