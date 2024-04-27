import os
import shutil
import re

# Define the source and destination directories
source_dir = os.path.join(os.path.curdir,'Sample files')


# this function create basic direcotries for Zones
def make_def_dir():
    for i in range(1,30):
        current_zone_dir = os.path.join(source_dir,f'Zone {i:02d}')
        if not os.path.exists(current_zone_dir):
            os.makedirs(current_zone_dir)
        
        branch_to_branch_dir = os.path.join(current_zone_dir,'Branch To Branch')
        branch_to_fat_dir = os.path.join(current_zone_dir,'Branch To FAT')
        fat_dir = os.path.join(current_zone_dir,'FAT')
        # Check if the destination directory exists
        if not os.path.exists(branch_to_branch_dir):
            # If it doesn't exist, create the directory
            os.makedirs(branch_to_branch_dir)
        if not os.path.exists(branch_to_fat_dir):
            # If it doesn't exist, create the directory
            os.makedirs(branch_to_fat_dir)
        if not os.path.exists(fat_dir):
            # If it doesn't exist, create the directory
            os.makedirs(fat_dir)

