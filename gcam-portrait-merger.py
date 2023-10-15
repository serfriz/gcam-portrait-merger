import os
import shutil
import re

# Define the path to the directory containing the portrait folders "IMG_yyyymmdd_hhmmss"
portrait_dir = "/path-to-photos/bundled"

# Define the path to the destination directory
dest_dir = "/path-to-photos/individual"

# Loop through each portrait folder in the directory
for portrait_folder in os.listdir(portrait_dir):
    portrait_path = os.path.join(portrait_dir, portrait_folder)
    if os.path.isdir(portrait_path):
        # Loop through each file in the portrait folder
        for file_name in os.listdir(portrait_path):
            file_path = os.path.join(portrait_path, file_name)
            if os.path.isfile(file_path):
                # Check if the file name contains the word "COVER"
                if re.search(r'COVER', file_name):
                    # Rename the file to "IMG_yyyymmdd_hhmmss.PORTRAIT.jpg"
                    new_file_name = portrait_folder + '.PORTRAIT.jpg'
                else:
                    # Rename the file to "IMG_yyyymmdd_hhmmss.jpg"
                    new_file_name = portrait_folder + '.jpg'

                # Move the renamed file to the /individual directory without subfolders
                new_file_path = os.path.join(dest_dir, new_file_name)
                
                # Check if the file already exists in the destination directory
                if os.path.exists(new_file_path):
                    # If it does, add a number to the filename until it's unique
                    i = 1
                    while True:
                        new_file_name = re.sub(r'\.jpg$', f'_{i}.jpg', new_file_name)
                        new_file_path = os.path.join(dest_dir, new_file_name)
                        if not os.path.exists(new_file_path):
                            break
                        i += 1
                
                # Copy the file to the destination directory
                shutil.copy2(file_path, new_file_path)
