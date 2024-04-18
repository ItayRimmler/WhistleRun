# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c
import subprocess as sp
def save_data(data):
    data.astype('int16').tofile("../data/audio/data.bin")

def print_data(size):
    sp.run(["../lib/audio/STFT.exe", str(size)])