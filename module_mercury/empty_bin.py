import os 
import shutil

def empty_bin():
    
    recycle_root = 'C:\\$Recycle.Bin'
    sid_list = []
        
    for sid_temp in os.listdir(recycle_root):
        if sid_temp.startswith('S-1-5-21'):
            sid_list.append(sid_temp)

    
    for sid in sid_list:
        recycle_bin_path = os.path.join('C:\\$Recycle.Bin', sid)
        
        try:
            bin_temp = os.listdir(recycle_bin_path)
        except PermissionError:
            print(f"Permission denied: {recycle_bin_path}")
            with open('mercurypulse\\module_mercury\\temp_cleaner_log.txt','w',encoding = 'UTF-8') as log_file:
                        log_file.write(f"Permission denied: {recycle_bin_path}")
            continue


        for file in bin_temp:
            file_path = os.path.join(recycle_bin_path, file)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
            except PermissionError:
                pass
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")