import os
import shutil

def organize_files(directory, move_files=False):
    """
    Organizes files within a given directory into subfolders based on their file extensions.

    Args:
        directory: The path to the directory containing the files to organize.
        move_files: If True, moves files to subfolders. If False, copies files. 
                    Defaults to False (copying).
    """

    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audios': ['.mp3', '.wav'],
    }

    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        for filename in os.listdir(directory):
            file_ext = os.path.splitext(filename)[1].lower()
            for folder_name, ext_list in extensions.items():
                if file_ext in ext_list:
                    folder_path = os.path.join(directory, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    source_file = os.path.join(directory, filename)
                    destination_file = os.path.join(folder_path, filename)

                    if move_files:
                        shutil.move(source_file, destination_file)
                        print(f'Moved: {filename} to {folder_name}')
                    else:
                        shutil.copy2(source_file, destination_file)
                        print(f'Copied: {filename} to {folder_name}')
                    break
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    source_directory = r"C:\Users\91879\Desktop\organised_files"  # Use raw string for Windows path
    organize_files(source_directory, move_files=False)  # Set move_files=True to move files