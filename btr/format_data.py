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
    low = (700/2) - (256/2)
    high = (700/2) - (256/2)
    cropped = field[:, low:high, low:high]
    
    # Passing a tuple to expand_dims leads to
    # two dimensions of 1 added at those indeces in the array.shape
    expanded = np.expand_dims(cropped.to_numpy(), (0,2))
    
    input_tensor = from_numpy(expanded)
    
    return input_tensor