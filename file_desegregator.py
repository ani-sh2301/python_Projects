import os
import shutil


#recursive method to desegregate files, using a folder list which contains list of folders to be desegregated
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
            folder.pop(0)             # removing the folders from list folder which are scanned
            

#input paths of source and destination
path=input("Enter the path of the directory which you want to desegregte from (with //): ")
destination=input("Enter the path of the directory were you want to move the desegregted files (with //): ")

#changing directory of work
os.chdir(path)

#listing the contents of the folder in contents
contents=os.listdir()

#adding all the 'folders' which are in the 'source folder' in folders list
folders=[]
for names in contents:
    if not os.path.isfile(names):
        folders.append(names)

#making a deep copy of folders list to delete the empty folders after desegregating
copy_folders=folders[:]
try:
    #calling the desegregator method
    deseg(folders,destination,destination)

    #deleting the empty directories
    for i in copy_folders:
        shutil.rmtree(os.path.join(path,i))

    print("Successful")

except:
    print("Desegregation was Unsuccessful")





