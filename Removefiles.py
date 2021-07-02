import os
import time
import shutil

def main():

    deleted_folder=0
    deleted_files=0
    days=30
    seconds=time.time()- (days*24*3600)
    path='/Delete_path'

    if os.path.exists(path):
        for initialFolder, files, folders in os.walk(path):
            if seconds >= get_age(root_folder):
                remove_folder(initialFolder)
                deleted_folder=deleted_folder+1
                break
            else:
                for folders in folders:
                    folderPath = os.path.join(initialFolder, folder)
                    if seconds>=get_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folder=deleted_folder+1
                for file in files:
                    file_path = os.path.join(initialFolder, file)
                    if seconds>=get_age(file_path):
                        remove_file(path)
                        deleted_files=deleted_files+1

        else:
            if seconds>=get_age(path):
                remove_file(path)
                deleted_files=deleted_files+1
    else:
        print(path + "is not found")
        print("Total files deleted: " + deleted_files)
        print("Total folders deleted: " + deleted_folder)
        deleted_files=deleted_files+1
    
def remove_folder(path):
    if not shutil.rmtree(path):
        print(path + " is removed successfully")
    else:
        print("Unable to delete " + path)

def remove_file(path):
    if not os.remove(path):
        print(path + " is removed successfully")
    else:
        print("Unable to delete "+ path)

def get_age(path):
    ctime=os.stat(path).st_ctime
    return ctime





path=input('Paste your path here')
days=int(input('Input your number here'))
time=time.time(days)
if os.path.exists(path):
    os.walk(path)
    os.path.join()
    ctime=os.stat.st_ctime()
    if ctime>time:

