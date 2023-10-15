# Google Camera (GCam) Portrait Merger

This script takes a directory containing folders of photos bundled by old versions (< v7.5) of Google Camera (GCam) when taking portrait snapshots and moves the photos to a new directory with a unique filename for each photo depending on whether it's a portrait or not. The portrait photos are renamed to "IMG_yyyymmdd_hhmmss.PORTRAIT.jpg" and the non-portrait photos are renamed to "IMG_yyyymmdd_hhmmss.jpg". The script also checks if the file already exists in the destination directory and adds a number to the filename until it's unique.

The script assumes that the portrait folders are named with the format "IMG_yyyymmdd_hhmmss" and are located in the directory specified by the variable `portrait_dir`. The script also assumes that the destination directory specified by the variable `dest_dir` already exists.

It is recommended to run the script on a copy of the portrait folders:
1. Connect your phone to your computer, copy the portrait folders to the path `portrait_dir` in your computer
2. Edit the variables `portrait_dir` and `dest_dir` in the script to point to the copied folders and the destination directory
3. Run the python script: `python gcam-portrait-merger.py`
4. Copy the renamed photos from the destination directory back to your phone
5. Delete the portrait folders from your phone and the copied folders from your computer