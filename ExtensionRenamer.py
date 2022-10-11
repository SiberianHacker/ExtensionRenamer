#fileExtensionRenamer
#tested with python 3.9.x
import os

print("Extension renamer 0.1")

path = input('path to files: ')
extension = input('extension: ')

for f in os.listdir(path):
       with open(os.path.join(path, f), 'r') as file:
           if '.' in f:
               oldname = os.path.join(path, f)
               old_extension = f.split('.')[1]
               new_name = f.replace(old_extension, extension)
               newname = os.path.join(path, new_name)
               os.rename(oldname, newname)
               print(newname)
           else:
               oldname = os.path.join(path, f)
               neww = f + '.' + extension
               newname = os.path.join(path, neww)
               os.rename(oldname, newname)
               print(neww)