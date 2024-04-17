# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c
from src.lib.audio.record import *

audio = g.pa.PyAudio()
data = g.np.array([])
for i in range(8):
    data_segment = multi_record(audio)
    data = g.np.concatenate([data, data_segment])
audio.terminate()



