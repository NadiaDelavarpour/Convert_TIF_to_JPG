from osgeo import gdal
import os
    
options_list = [
    '-ot Byte',
    '-of JPEG',
    '-b 1',
    '-b 2',
    '-b 3',
    '-scale'
]           

options_string = " ".join(options_list)

directory = "H:/Ortho_Data/UAV2022/Rest"
for filename in os.listdir(directory):
    if filename.endswith('.tif'):
        name, ext = os.path.splitext(filename)
        tif_path = os.path.join(directory, filename)
        jpg_path = os.path.join(directory, name) + ".jpg"
        gdal.Translate(
        jpg_path,
        tif_path,
        options=options_string
)
