import os
import shutil
import datetime
import time

source_dir = "/Users/sylviadrake-gill/Desktop/SDG"
destination_dir = "/Users/sylviadrake-gill/Desktop/Projects/backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest_dir}")
        
copy_folder_to_directory(source_dir, destination_dir)