import zipfile
import os

def zip_dir_for_layer_and_style(zip_path, layer_path, style_path):
    zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    zipf.write(style_path, os.path.basename(style_path))
    zipf.write(layer_path, os.path.basename(layer_path))
    zipf.close()
    os.remove(layer_path)