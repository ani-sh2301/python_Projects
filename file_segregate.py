import os

#input path
#x=input("Enter the path of the directory which you want to segregate: ")
path=r'D:\test'

os.chdir(path)

list_of_cont=os.listdir()

files = []

#all_ext={'Videos':['mp4','mkv'],'Audios':['mp3','wav','ogg'],'Images':['jpg','jpeg','png','gif','webp','svg','bmp'],'Docs':['pdf','doc','docx','txt','ppt','pptx','xls','xlsx','csv']}
all_ext2={'mp4':'Videos','mkv':'Videos','mp3':'Audios','wav':'Audios','ogg':'Audios','jpg':'Images','jpeg':'Images','png':'Images','gif':'Images','webp':'Images','svg':'Images','bmp':'Images','pdf':'Docs','doc':'Docs','docx':'Docs','txt':'Docs','ppt':'Docs','pptx':'Docs','xlx':'Docs','xlsx':'Docs','csv':'Docs'}

folders = ['Videos','Audios','Images','Docs','Misc']

for name in list_of_cont:
    if os.path.isfile(name):
        files.append(name)

#files contains no folders now

#creating folders to segregate
for name in folders:
    os.mkdir(name)

for filename in files:
    source = os.path.join(path,filename)

    extension=filename.split('.')[-1]
    
    if extension in all_ext2.keys():
        destination = os.path.join(path,all_ext2.get(extension), filename)
    else:
        destination = os.path.join(path, 'Misc', filename)
  
    '''
    for ext in all_ext.keys():
        if extension in all_ext.get(ext):
            destination = os.path.join(path,ext, filename)
            flag=True
            break
    if not flag:
        destination = os.path.join(path, 'Misc', filename)
    '''
    os.rename(source, destination)


print('Operation completed')
print('Files moved successfully')



