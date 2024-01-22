from btr.params import *
from dgmr import DGMR
import os
from torch import load
import urllib

def get_pretrained():
    # If pytorch_model.bin file hasn't been download yet...
    if not os.path.isfile(MODELFILE):
        # Download from link found on https://huggingface.co/openclimatefix/dgmr/tree/main
        urllib.request.urlretrieve(MODEL_URL, MODELFILE)
        
    state_dict = load(MODELFILE)
    model = DGMR()
    model.load_state_dict(state_dict)
    
    return model
    