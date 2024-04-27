import os
import shutil
import re

# Define the source and destination directories
source_dir = os.path.join(os.path.curdir,'Sample files')

# define direction variables



# this function create basic direcotries for Zones
def make_def_dir():
    for i in range(1,16):
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

# function that get all existing numbers in file name
def get_number_in_text(text_with_number ):
    # Define a regular expression pattern to match the number after the text
    pattern = r'(\d+)'

    # Search for the pattern in the string
    matched_numbers  = re.findall(pattern, text_with_number)
    return matched_numbers
        
# Function to check file name if it's based on this setting
def check_file_name(file_name):
    # chech if there is atleast two number in file name
    numbers_in_file_name = get_number_in_text(file_name)
    if len(numbers_in_file_name) < 2:
        return False
    
    # check if format of file is jpg
    file_extetion = file_name.split('.')[-1]
    if not file_extetion == 'jpg' or file_extetion == 'jpeg' or file_extetion == 'png':
        return False


# List all files in the source directory
files = os.listdir(source_dir)

# Iterate through each file
for file_name in files:
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(source_dir, file_name)):
        # check if file is a valid image
        if not check_file_name(file_name):
            continue

         # Split the file name into words
        words_in_filename = file_name.split('-')
        # count the number of branch in file name
        branch_count= 0
        for word in words_in_filename:
            if 'br' in word:
                branch_count +=1
        
        # get all numbers in file name
        numbers_in_file_name = get_number_in_text(file_name)
        current_zone = int(numbers_in_file_name[0])
        # Writing variables for directions
        current_zone_dir = os.path.join(source_dir,f'Zone {current_zone:02d}')
        branch_to_branch_dir = os.path.join(current_zone_dir,'Branch To Branch')
        branch_to_fat_dir = os.path.join(current_zone_dir,'Branch To FAT')
        fat_dir = os.path.join(current_zone_dir,'FAT')

        # Create subdirecoties
        if branch_count ==1:
            # Branch To FAT
            if len(numbers_in_file_name) ==3:
                new_dir = os.path.join(branch_to_fat_dir, f"Br {int(numbers_in_file_name[1]):02d} FAT {int(numbers_in_file_name[2]):02d}" )
                if not os.path.exists(new_dir):
                    # If it doesn't exist, create the directory
                    os.makedirs(new_dir)
                shutil.move(os.path.join(source_dir,file_name),new_dir )

        elif branch_count ==2:
            # Branch To Branch
            if len(numbers_in_file_name) ==3:
                new_dir = os.path.join(branch_to_branch_dir, f"Br {int(numbers_in_file_name[1]):02d} Br {int(numbers_in_file_name[2]):02d}" )
                if not os.path.exists(new_dir):
                    # If it doesn't exist, create the directory
                    os.makedirs(new_dir)
                shutil.move(os.path.join(source_dir,file_name),new_dir )

        else:
            # Just FAT
            if numbers_in_file_name:
                new_dir = os.path.join(fat_dir, f"FAT {int(numbers_in_file_name[1]):02d}" )
                if not os.path.exists(new_dir):
                    # If it doesn't exist, create the directory
                    os.makedirs(new_dir)
                shutil.move(os.path.join(source_dir,file_name),new_dir )