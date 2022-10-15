import os
import shutil
from_dir = "C:/Users/laiba/Downloads" 
to_dir = "C:/Users/laiba/OneDrive/Desktop/coding class"
list_of_files= os.listdir(from_dir)
for file_name in list_of_files:
 name,extension= os.path.splitext(file_name) 
 if extension == '':
    continue
    if extension in ['gif','png,''ipg','ipeg','jfif']:
        path1=from_dir+ '/'+"file_name"
        path2=to_dir+'/' +"image_files"
        path3=to_dir+'/'+ "image_files"+'/'+ file_name
        if os.path.exists(path2):
           print ("moving"+file_name+".....")
           shutil.move(path1,path3)
        else: 
           os.makedirs(path2) 
           print("moving"+file_name+".....")
           shutil.move(path1,path3)  
