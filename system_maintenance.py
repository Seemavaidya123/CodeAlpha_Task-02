import os
import time

def delete_temp_files(directory):
    # Define the age of files to delete (in seconds)
    age_limit = 7 * 24 * 60 * 60  # 7 days in seconds

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            # Check the last modified time
            if time.time() - os.path.getmtime(file_path) > age_limit:
                os.remove(file_path)
                print(f'Deleted: {filename}')

if __name__ == "__main__":
    # Specify the directory to clean
    directory_path = input("Enter the directory path to clean temporary files: ")
    delete_temp_files(directory_path)
