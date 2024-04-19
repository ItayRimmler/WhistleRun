# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c
from src.lib.audio.record import *
from src.lib.audio.bin import save_data, process_in_cpp, read_data

audio = g.pa.PyAudio()
data = g.np.array([])
for i in range(8):
    data_segment = multi_record(audio)
    data = g.np.concatenate([data, data_segment])
audio.terminate()

save_data(data)

process_in_cpp(data.shape[0])

data = read_data()

