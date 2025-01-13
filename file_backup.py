import os
import shutil
import datetime
import time

source_dir = "/Users/sylviadrake-gill/Desktop/SDG"
destination_dir = "/Users/sylviadrake-gill/Desktop/Projects/backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))