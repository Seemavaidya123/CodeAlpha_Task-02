import os
import shutil

def organize_files(directory):
    # Define folders for different file types
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar', '.tar'],
        'Others': []
    }

    # Create folders if they do not exist
    for folder in folders.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Move files into their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):  # Check if it's a file
            moved = False
            for folder, extensions in folders.items():
                if any(filename.endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    print(f'Moved: {filename} to {folder}')
                    break
            
            if not moved:
                shutil.move(file_path, os.path.join(directory, 'Others', filename))
                print(f'Moved: {filename} to Others')

if __name__ == "__main__":
    # Specify the directory to organize
    directory_path = input("Enter the directory path to organize: ")
    organize_files(directory_path)
