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
def check_file_name_validity(file_name):
    # chech if there is atleast two number in file name
    numbers_in_file_name = get_number_in_text(file_name)
    if len(numbers_in_file_name) < 2:
        print(f'Error: There is not enough number in {file_name}\n\n')
        return False
    # elif len(numbers_in_file_name) >3:
    #     print(f'Error: There are too many number in {file_name}\n\n')
    #     return False
    # elif len(numbers_in_file_name) != len (words_in_filename):
    #     print(f'Error: Number of words in {file_name} does not match number of Numbers! (make sure if u use - as your seperator)')
    #     return False

   
    # check if format of file is jpg
    file_extetion = file_name.split('.')[-1]
    if not (file_extetion == 'jpg' or file_extetion == 'jpeg' or file_extetion == 'png' or file_extetion == 'pdf'):
        print(f'Error: {file_extetion} Format in file {file_name} is not Valid!!\n\n')
        return False
    else:
        return True

# Function that check "odc" in file name
def create_odc_subdirectory(file_name,words_in_filename):
    if 'odc' in words_in_filename[1].lower():
        reversed_dir = os.path.join(branch_to_odc_dir, f"Branch {int(numbers_in_file_name[1]):02d} ODC {int(numbers_in_file_name[2]):02d}" )
        if os.path.exists(new_dir):
            new_dir = reversed_dir
        else:
            new_dir = os.path.join(branch_to_odc_dir, f"ODC {int(numbers_in_file_name[1]):02d} Branch {int(numbers_in_file_name[2]):02d}" )
        if not os.path.exists(new_dir):
            # If it doesn't exist, create the directory
            os.makedirs(new_dir)
        return new_dir
    elif 'odc' in words_in_filename[2].lower():
        reversed_dir = os.path.join(branch_to_odc_dir, f"ODC {int(numbers_in_file_name[1]):02d} Branch {int(numbers_in_file_name[2]):02d}" )
        if os.path.exists(new_dir):
            new_dir = reversed_dir
        else:
            new_dir = os.path.join(branch_to_odc_dir, f"Branch {int(numbers_in_file_name[1]):02d} ODC {int(numbers_in_file_name[2]):02d}" )
        if not os.path.exists(new_dir):
            # If it doesn't exist, create the directory
            os.makedirs(new_dir)
        return new_dir
    else:
        print(f'Error: Invalid name for file{file_name}\n\n')
        new_dir = ''
        return new_dir

# Function that check "oac" in file name
def create_oac_subdirectory(file_name,words_in_filename):
    if 'oac' in words_in_filename[1].lower():
        reversed_dir = os.path.join(branch_to_odc_dir, f"Branch {int(numbers_in_file_name[1]):02d} OAC {int(numbers_in_file_name[2]):02d}" )
        if os.path.exists(new_dir):
            new_dir = reversed_dir
        else:
            new_dir = os.path.join(branch_to_odc_dir, f"OAC {int(numbers_in_file_name[1]):02d} Branch {int(numbers_in_file_name[2]):02d}" )
        if not os.path.exists(new_dir):
            # If it doesn't exist, create the directory
            os.makedirs(new_dir)
        return new_dir
    elif 'oac' in words_in_filename[2].lower():
        reversed_dir = os.path.join(branch_to_odc_dir, f"OAC {int(numbers_in_file_name[1]):02d} Branch {int(numbers_in_file_name[2]):02d}" )
        if os.path.exists(new_dir):
            new_dir = reversed_dir
        else:
            new_dir = os.path.join(branch_to_odc_dir, f"Branch {int(numbers_in_file_name[1]):02d} OAC {int(numbers_in_file_name[2]):02d}" )
        if not os.path.exists(new_dir):
            # If it doesn't exist, create the directory
            os.makedirs(new_dir)
        return new_dir
    else:
        print(f'Error: Invalid name for file{file_name}\n\n')
        new_dir = ''
        return new_dir

# Function that check "HH" in file name
def create_hh_subdirectory(file_name, words_in_filename):
    if 'hh' in words_in_filename[1].lower():
        new_dir = os.path.join(hh_dir, f"HH {int(numbers_in_file_name[1]):02d}" )
        if not os.path.exists(new_dir):
            # If it doesn't exist, create the directory
            os.makedirs(new_dir)
        return new_dir
    else:
        new_dir = ''
        return new_dir

def create_mtnhh_subdirectory(file_name, words_in_filename):
    if 'mtnhh' in words_in_filename[1].lower() or 'mtn.hh' in words_in_filename[1].lower():
        reversed_dir = os.path.join(mtn_dir, f"Branch {int(numbers_in_file_name[1]):02d} MTN {int(numbers_in_file_name[2]):02d}" )
        if os.path.exists(reversed_dir):
            new_dir = reversed_dir
        else:
            new_dir = os.path.join(mtn_dir, f"MTN {int(numbers_in_file_name[1]):02d} Branch {int(numbers_in_file_name[2]):02d}" )
        if not os.path.exists(new_dir):
            # If it doesn't exist, create the directory
            os.makedirs(new_dir)
        return new_dir
    elif 'mtnhh' in words_in_filename[2].lower() or 'mtn.hh' in words_in_filename[2].lower():
        reversed_dir = os.path.join(mtn_dir, f"MTN {int(numbers_in_file_name[1]):02d} Branch {int(numbers_in_file_name[2]):02d}" )
        if os.path.exists(reversed_dir):
            new_dir = reversed_dir
        else:
            new_dir = os.path.join(mtn_dir, f"Branch {int(numbers_in_file_name[1]):02d} MTN {int(numbers_in_file_name[2]):02d}" )
        if not os.path.exists(new_dir):
            # If it doesn't exist, create the directory
            os.makedirs(new_dir)
        return new_dir
    else:
        print(f'Error: Invalid name for file{file_name}\n\n')
        new_dir = ''
        return new_dir
    
# List all files in the source directory
files = os.listdir(os.path.curdir)

# Iterate through each file
for file_name in files:
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(source_dir, file_name)):
        # Split the file name into words
        words_in_filename = file_name.split('-')

        # check if file is a valid image
        if not check_file_name_validity(file_name):
            continue

        # count the number of branch in file name
        branch_count= 0
        for word in words_in_filename:
            if 'br' in word:
                branch_count +=1
        
        # get all numbers in file name
        numbers_in_file_name = get_number_in_text(file_name)
        # if there isn't enough number in file name show an error message
        if (len(numbers_in_file_name) < 2):
            print(f"Error: There is not enough number in file {file_name}!\n\n")
            continue
        current_zone = int(numbers_in_file_name[0])
        # Writing variables for directions
        current_zone_dir = os.path.join(categorized_dir,f'Zone {current_zone:02d}')
        branch_to_branch_dir = os.path.join(current_zone_dir,'Branch To Branch')
        branch_to_fat_dir = os.path.join(current_zone_dir,'Branch To FAT')
        fat_dir = os.path.join(current_zone_dir,'FAT')
        branch_to_odc_dir = os.path.join(current_zone_dir, 'Branch to ODC')
        hh_dir = os.path.join(current_zone_dir, 'HH')
        mtn_dir = os.path.join(current_zone_dir, 'MTN')

        # Create subdirecoties
        if branch_count ==1:
            # Branch To FAT
            if len(numbers_in_file_name) == 3 or len(numbers_in_file_name )== 4:
                # if there is "ODC" in file name
                if 'odc' in file_name.lower():
                    new_dir = create_odc_subdirectory(file_name, words_in_filename)
                    if new_dir == '':
                        continue
                elif 'mtnhh' in file_name.lower() or 'mtn.hh' in file_name.lower():
                    new_dir = create_mtnhh_subdirectory(file_name, words_in_filename)
                    if new_dir == '':
                        continue
                elif 'fat' in file_name.lower() or 'ft' in file_name.lower():
                    new_dir = os.path.join(branch_to_fat_dir, f"Br {int(numbers_in_file_name[1]):02d} FAT {int(numbers_in_file_name[2]):02d}" )
                    if not os.path.exists(new_dir):
                        # If it doesn't exist, create the directory
                        os.makedirs(new_dir)
                else:
                    print(f'Error: File {file_name} does not any file name rules!\n\n')
                    continue

                print(f'Moving {file_name} to {new_dir}\n')
                shutil.move(os.path.join(source_dir,file_name),new_dir )
                print(f'{file_name} has been moved successfully\n\n')

        elif branch_count ==2:
            # Branch To Branch
            if len(numbers_in_file_name) == 3 or len(numbers_in_file_name )== 4:
                reversed_dir = os.path.join(branch_to_branch_dir, f"Br {int(numbers_in_file_name[2]):02d} Br {int(numbers_in_file_name[1]):02d}" )
                if os.path.exists(reversed_dir):
                    new_dir = reversed_dir
                else:
                    new_dir = os.path.join(branch_to_branch_dir, f"Br {int(numbers_in_file_name[1]):02d} Br {int(numbers_in_file_name[2]):02d}" )
                if not os.path.exists(new_dir):
                    # If it doesn't exist, create the directory
                    os.makedirs(new_dir)
                print(f'Moving {file_name} to {new_dir}\n')
                shutil.move(os.path.join(source_dir,file_name),new_dir )
                print(f'{file_name} has been moved successfully\n\n')

        else:
            # Just FAT
            if 'fat' in file_name.lower() or 'ft' in file_name.lower():
                new_dir = os.path.join(fat_dir, f"FAT {int(numbers_in_file_name[1]):02d}" )
                if not os.path.exists(new_dir):
                    # If it doesn't exist, create the directory
                    os.makedirs(new_dir)
                print(f'Moving {file_name} to {new_dir}\n')
                shutil.move(os.path.join(source_dir,file_name),new_dir )
                print(f'{file_name} has been moved successfully\n\n')
            elif 'hh' in file_name.lower():
                new_dir = create_hh_subdirectory(file_name,words_in_filename)
                if new_dir == '':
                    continue
                print(f'Moving {file_name} to {new_dir}\n')
                shutil.move(os.path.join(source_dir,file_name),new_dir )
                print(f'{file_name} has been moved successfully\n\n')
            else:
                print(f'Error: File {file_name} does not any file name rules!\n\n')