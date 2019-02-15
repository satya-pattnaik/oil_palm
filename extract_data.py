import zipfile
import os
def extract_images(zip_file):
    path_to_zip_file = os.path.join(os.getcwd(),zip_file)
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(os.getcwd())
    zip_ref.close()