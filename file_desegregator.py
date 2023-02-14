import os
import shutil


def deseg(folder,source,destination):
    while len(folder)!=0:
            new_source=os.path.join(source,folder[0])
            x=[]
            files=os.listdir(new_source)
            for names in files:
                if not os.path.isfile(os.path.join(new_source,names)):
                    x.append(names)
                else:
                    os.rename(os.path.join(new_source,names),os.path.join(destination,names))
            deseg(x,new_source,destination)
            folder.pop(0)
            

path=r'D:\test'
os.chdir(path)

contents=os.listdir()
folders=[]
for names in contents:
    if not os.path.isfile(names):
        folders.append(names)

copy_folders=folders[:]

destination=path
deseg(folders,destination,destination)

#deleting the empty directories
for i in copy_folders:
    shutil.rmtree(os.path.join(path,i))


print("Successful")




