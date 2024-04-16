# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c
from src.lib.audio.record import *

audio = g.pa.PyAudio()

st, data = start_recording(audio)
pause_recording(st)
st, data = continue_recording(st)
stop_recording(st)

audio.terminate()
audio_data = g.np.frombuffer(b"".join(data), dtype=g.np.int16)



