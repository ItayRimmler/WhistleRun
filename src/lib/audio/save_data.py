# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.all import constants as c

def save_data(data):
    data.tofile("../data/audio/data.bin")
