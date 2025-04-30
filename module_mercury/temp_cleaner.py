import os
import shutil

def download_delete():
    """
    Deletes all files and folders in the Downloads and Temp directories.
    """
    temp_dirs = [
        os.environ.get('TEMP', ''),
        os.environ.get('TMP', ''),
        os.path.join(os.environ.get('WINDIR', ''), 'Temp'),
        os.path.join(os.environ.get('WINDIR', ''), 'Prefetch'),
        os.path.join(os.environ.get('WINDIR', ''), 'SoftwareDistribution', 'Download'),
        os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Local', 'Temp'),
        os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads')
    ]
    

    for directory in temp_dirs:
        
        if not os.path.exists(directory): 
            continue
        try:
            files = os.listdir(directory)
        except PermissionError:
            print(f"Permission denied: {directory}")
            with open('mercurypulse\\module_mercury\\temp_cleaner_log.txt','w',encoding = 'UTF-8') as log_file:
                        log_file.write(f"Permission denied: {directory}")
            continue

        for file in files:
            file_path = os.path.join(directory, file)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
            except PermissionError:
                pass
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

