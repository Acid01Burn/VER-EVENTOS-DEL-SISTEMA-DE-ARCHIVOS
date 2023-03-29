import os
import shutil

from_dir="C:/Users/Ivonne/Downloads"
todir="C:/Users/Ivonne/Mains"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    if extension=="":
        continue
    
    if extension in ['.mp4']:
        path_1=from_dir+'/'+filename
        path_2=todir+'/'+'Mains'
        path_3=todir+'/'+'Mains'+'/'+filename
        print("path_1: ",path_1)
        print("path_3: ",path_3)
        if os.path.exists(path_2):
            print("Moviendo ._. "+filename+'......')
            shutil.move(path_1,path_3)
        else:
            os.makedirs(path_2)
            print("Moviendo ._. "+filename+'......')
            shutil.move(path_1,path_3)