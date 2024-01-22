from btr.format_data import prep
from btr.model import get_pretrained
from btr.read_data import get_data_as_xarray
from datetime import date
import numpy as np
from tqdm import tqdm

def create_ensemble(n_members = 50):
    data = get_data_as_xarray()
    input = prep(data['precip_intensity'])
    
    model = get_pretrained()
    ensemble = []
    print('Creating ensemble:')
    for i in tqdm(range(n_members)):
        output = model(input[:,:4])
        ensemble.append(output)
    
    ensemble = np.concatenate(ensemble)
    
    return ensemble

if __name__ == '__main__':
    ensemble = create_ensemble(5)
    datestamp = date.today()
    np.save(f'../outputs/ensembles/{datestamp}-{ensemble.shape[0]}.npy', ensemble)
    