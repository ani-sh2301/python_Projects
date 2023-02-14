import os

#input path
x=input("Enter the path of the directory which you want to segregate (with //): ")
path=x

#change directory
os.chdir(path)

#list of files
list_of_cont=os.listdir()

files = []

#creating a dictionary of extension key and type value
all_ext2={'mp4':'Videos','mkv':'Videos','mp3':'Audios','wav':'Audios','ogg':'Audios','jpg':'Images','jpeg':'Images','png':'Images','gif':'Images','webp':'Images','svg':'Images','bmp':'Images','pdf':'Docs','doc':'Docs','docx':'Docs','txt':'Docs','ppt':'Docs','pptx':'Docs','xlx':'Docs','xlsx':'Docs','csv':'Docs'}

#all folder to be created
folders = ['Videos','Audios','Images','Docs','Misc']

#seperating files and adding to files list
for name in list_of_cont:
    if os.path.isfile(name):
        files.append(name)

#creating folders to segregate
for name in folders:
    os.mkdir(name)

try:
    for filename in files:
        source = os.path.join(path,filename)

        extension=filename.split('.')[-1]
        
        if extension in all_ext2.keys():
            destination = os.path.join(path,all_ext2.get(extension), filename)
        else:
            destination = os.path.join(path, 'Misc', filename)

        os.rename(source, destination)
    
    print('Operation Completed')
    print('Files moved successfully')

except:
    print('Operation Unsuccesssful')
    print('Files were not moved')






