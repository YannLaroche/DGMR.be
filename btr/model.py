from btr.params import *
from dgmr import DGMR
from torch import load

def get_pretrained():
    state_dict = load(MODELFILE)
    model = DGMR()
    model.load_state_dict(state_dict)
    return model
    