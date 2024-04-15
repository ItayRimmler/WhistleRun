# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c
import sounddevice as sd

def record(sample_rate=c.SR, channel=c.CH, duration=c.DUR):
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channel,
                       dtype='int')
    sd.wait()
    return recording[:, 0]
