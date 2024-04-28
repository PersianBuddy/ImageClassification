import os
import shutil
import re

# Define the source and destination directories
categorized_dir = os.path.join(os.path.abspath(os.path.pardir),'Categorized')
# define direction variables
# create this directory if it doesn't exist
if not os.path.exists(categorized_dir):
    os.makedirs(categorized_dir)

# get source category
source_dir = os.path.curdir

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
        print(f'Error: There is not enough number in {file_name}\n\n')
        return False
    elif len(numbers_in_file_name) >3:
        print(f'Error: There are too many number in {file_name}\n\n')
        return False
   
    # check if format of file is jpg
    file_extetion = file_name.split('.')[-1]
    if not (file_extetion == 'jpg' or file_extetion == 'jpeg' or file_extetion == 'png'):
        print(f'Error: {file_extetion} Format in file {file_name} is not Valid!!\n\n')
        return False
    else:
        return True


# List all files in the source directory
files = os.listdir(os.path.curdir)

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
        current_zone_dir = os.path.join(categorized_dir,f'Zone {current_zone:02d}')
        branch_to_branch_dir = os.path.join(current_zone_dir,'Branch To Branch')
        branch_to_fat_dir = os.path.join(current_zone_dir,'Branch To FAT')
        fat_dir = os.path.join(current_zone_dir,'FAT')

        # Create subdirecoties
        if branch_count ==1:
            # Branch To FAT
            if len(numbers_in_file_name) == 3:
                if 'odc' in file_name:
                    if 'odc' in words_in_filename[1]:
                        new_dir = os.path.join(branch_to_fat_dir, f"ODC {int(numbers_in_file_name[1]):02d} Branch {int(numbers_in_file_name[2]):02d}" )
                        if not os.path.exists(new_dir):
                            # If it doesn't exist, create the directory
                            os.makedirs(new_dir)
                    elif 'odc' in words_in_filename[2]:
                        new_dir = os.path.join(branch_to_fat_dir, f"Branch {int(numbers_in_file_name[1]):02d} ODC {int(numbers_in_file_name[2]):02d}" )
                        if not os.path.exists(new_dir):
                            # If it doesn't exist, create the directory
                            os.makedirs(new_dir)
                    else:
                        continue
                else:
                    new_dir = os.path.join(branch_to_fat_dir, f"Br {int(numbers_in_file_name[1]):02d} FAT {int(numbers_in_file_name[2]):02d}" )
                    if not os.path.exists(new_dir):
                        # If it doesn't exist, create the directory
                        os.makedirs(new_dir)

                print(f'Moving {file_name} to {new_dir}\n')
                shutil.move(os.path.join(source_dir,file_name),new_dir )
                print(f'{file_name} has been moved successfully\n\n')

        elif branch_count ==2:
            # Branch To Branch
            if len(numbers_in_file_name) ==3:
                new_dir = os.path.join(branch_to_branch_dir, f"Br {int(numbers_in_file_name[1]):02d} Br {int(numbers_in_file_name[2]):02d}" )
                if not os.path.exists(new_dir):
                    # If it doesn't exist, create the directory
                    os.makedirs(new_dir)
                print(f'Moving {file_name} to {new_dir}\n')
                shutil.move(os.path.join(source_dir,file_name),new_dir )
                print(f'{file_name} has been moved successfully\n\n')

        else:
            # Just FAT
            if numbers_in_file_name:
                new_dir = os.path.join(fat_dir, f"FAT {int(numbers_in_file_name[1]):02d}" )
                if not os.path.exists(new_dir):
                    # If it doesn't exist, create the directory
                    os.makedirs(new_dir)
                print(f'Moving {file_name} to {new_dir}\n')
                shutil.move(os.path.join(source_dir,file_name),new_dir )
                print(f'{file_name} has been moved successfully\n\n')