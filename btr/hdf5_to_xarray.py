'''Code from Simon De Kock'''

import numpy as np
import os
import pandas as pd
import pyproj
from wradlib.io import read_opera_hdf5
import xarray as xr


def read_hdf5_to_xarray(fns):
    datasets = []

    for file_name in fns:
        # Read the content
        file_content = read_opera_hdf5(file_name)

        # Extract time information
        time_str = os.path.splitext(os.path.basename(file_name))[0].split('.', 1)[0]
        time = pd.to_datetime(time_str, format='%Y%m%d%H%M%S')

        # Extract quantity information
        try:
            quantity = file_content['dataset1/data1/what']['quantity'].decode()
        except:
            quantity = file_content['dataset1/data1/what']['quantity']

        # Set variable properties based on quantity
        if quantity == 'RATE':
            short_name = 'precip_intensity'
            long_name = 'instantaneous precipitation rate'
            units = 'mm h-1'
        else:
            raise Exception(f"Quantity {quantity} not yet implemented.")

        # Create the grid
        projection = file_content.get("where", {}).get("projdef", "")
        if type(projection) is not str:
            projection = projection.decode("UTF-8")

        gridspec = file_content.get("dataset1/where", {})

        x = np.linspace(gridspec.get('UL_x', 0),
                        gridspec.get('UL_x', 0) + gridspec.get('xsize', 0) * gridspec.get('xscale', 0),
                        num=gridspec.get('xsize', 0), endpoint=False)
        x += gridspec.get('xscale', 0)
        y = np.linspace(gridspec.get('UL_y', 0),
                        gridspec.get('UL_y', 0) - gridspec.get('ysize', 0) * gridspec.get('yscale', 0),
                        num=gridspec.get('ysize', 0), endpoint=False)
        y -= gridspec.get('yscale', 0) / 2

        x_2d, y_2d = np.meshgrid(x, y)

        pr = pyproj.Proj(projection)

        lon, lat = pr(x_2d.flatten(), y_2d.flatten(), inverse=True)
        lon = lon.reshape(gridspec.get('ysize', 0), gridspec.get('xsize', 0))
        lat = lat.reshape(gridspec.get('ysize', 0), gridspec.get('xsize', 0))

        # Build the xarray dataset
        ds = xr.Dataset(
            data_vars={
                short_name: (['x', 'y'], file_content.get("dataset1/data1/data", np.nan),
                             {'long_name': long_name, 'units': units})
            },
            coords={
                'x': (['x'], x, {'axis': 'X', 'standard_name': 'projection_x_coordinate',
                                 'long_name': 'x-coordinate in Cartesian system', 'units': 'm'}),
                'y': (['y'], y, {'axis': 'Y', 'standard_name': 'projection_y_coordinate',
                                 'long_name': 'y-coordinate in Cartesian system', 'units': 'm'}),
                'lon': (['y', 'x'], lon, {'standard_name': 'longitude', 'long_name': 'longitude coordinate',
                                          'units': 'degrees_east'}),
                'lat': (['y', 'x'], lat, {'standard_name': 'latitude', 'long_name': 'latitude coordinate',
                                          'units': 'degrees_north'})
            }
        )
        ds['time'] = time

        # Append the dataset to the list
        datasets.append(ds)

    # Concatenate datasets along the time dimension
    final_dataset = xr.concat(datasets, dim='time')
    return final_dataset


