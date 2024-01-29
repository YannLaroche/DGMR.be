import netCDF4
import numpy as np
from torch import from_numpy, Tensor
from xarray import DataArray

def prep(field: DataArray) -> Tensor:
    '''
    - Crop xarray data to required dimensions (700x700 to 256x256)
    - Reshape it to:
        [B, T, C, H, W] - Batch, Time, Channel, Heigh, Width
    - Turn it into a torch.tensor
    args:
        - field: xarray.DataArray
            The precipitation data variable from the xarray
    '''
    # Crop the center of the field and get a 256x256 image
    # Intervals of +/- 256/2 around the center (which is 700/2)
    low = (700//2) - (256//2)
    high = (700//2) + (256//2)
    cropped = field[:, low:high, low:high]
    
    # Passing a tuple to expand_dims leads to
    # two dimensions of 1 added at those indeces in the array.shape
    expanded = np.expand_dims(cropped.to_numpy(), (0,2))
    
    input_tensor = from_numpy(expanded)
    
    return input_tensor

def create_necdf(in_fn, model_name, n_members,
                 out_dir='/home/yann/Documents/BTR/DGMR.be/outputs/ensembles/'):
    output = np.load(in_fn)
    out_fn = f'{out_dir}ensemble_{model_name}_{n_members}.nc'
    
    ds = netCDF4.Dataset(out_fn, 'w')
    if model_name.lower() == 'dgmr':
        output = np.expand_dims(output, 0)
        dim_sample = ds.createDimension('sample', output.shape[0])
        dim_member = ds.createDimension('member', output.shape[1])
        dim_time = ds.createDimension('time', output.shape[2])
        dim_channel = ds.createDimension('channel', output.shape[3])
        dim_lon = ds.createDimension('lon', output.shape[4])
        dim_lat = ds.createDimension('lat', output.shape[5])
    
    if model_name.lower() == 'ldcast':
        output = np.expand_dims(output, 0)
        shape = output.shape
        output = np.reshape(output, 
                            (shape[1], shape[5], shape[2],
                                shape[0], shape[3], shape[4]))
        dim_sample = ds.createDimension('sample', output.shape[0])
        dim_member = ds.createDimension('member', output.shape[1])
        dim_time = ds.createDimension('time', output.shape[2])
        dim_channel = ds.createDimension('channel', output.shape[3])
        dim_lon = ds.createDimension('lon', output.shape[4])
        dim_lat = ds.createDimension('lat', output.shape[5])
        
    var = ds.createVariable(
            'precip_intensity', output.dtype,
            ('sample', 'member', 'time', 
             'channel', 'lon', 'lat')
        )
        
    var[:] = output
    ds.close()