# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c

# IF YOU'RE USING STFT THEN DELETE THE FOLLOWING FUNCTION:
def multi_record(audio):
    data = g.np.array([])
    for i in range(5):
        st, data_fraction = start_recording(audio)
        data = g.np.concatenate([data, g.np.frombuffer(b"".join(data_fraction), dtype=g.np.int16)])
    stop_recording(st)
    return data

# USING PYAUDIO:
# Beginning of the program: audio = pa.PyAudio() #In the script you want to use...
# stream, data = start_recording(audio)
# pause_recording(stream)
# stream, data = continue_recording(audio)
# pause_recording(stream)
# ...~pause and continue how many times you want, it will preserve the data while paused~...
# stop_recording(stream)
# End of the program: audio.terminate() #In the script you want to use...

# BASIC RECORDING FUNCTIONS:

def start_recording(audio):
    st = audio.open(
            format=g.pa.paInt16,
            channels=g.c.CH,
            rate=g.c.SR,
            input=True,
            frames_per_buffer=g.c.FR
        )
    frames = []
    for i in range(int(g.c.SR / g.c.FR * g.c.RECTIME)):
        frames.append(st.read(g.c.FR))
    return st, frames

def pause_recording(st):
    st.stop_stream()

def continue_recording(st):
    st.start_stream()
    frames = []
    for i in range(int(g.c.SR / g.c.FR * g.c.RECTIME)):
        frames.append(st.read(g.c.FR))
    return st, frames

def stop_recording(st):
    st.stop_stream()
    st.close()
