import zipfile
import os
def extract_images():
    path_to_zip_file = os.getcwd() + '/widsdatathon2019.zip'
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(os.getcwd())
    zip_ref.close()