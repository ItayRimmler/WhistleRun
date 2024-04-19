# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c
import subprocess as sp
def save_data(data):
    data.astype('int16').tofile("../data/audio/data.bin")

def process_in_cpp(size):
    sp.run(["../lib/audio/STFT.exe", str(size)])

def read_data():
    return g.np.fromfile("../data/audio/data.bin", dtype=g.np.int16)
