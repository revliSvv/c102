import os
import shutil

source = 'c:/users/chema/downloads'
destination = 'c:/users/chema/onedrive/desktop/stuff/stuff'

files = os.listdir(source)
#print(files)

for file in files:
  name, ext = os.path.splitext(file)
  if ext == '':
   continue
  elif ext in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = source + '/' + file
    path2 = destination + '/documents'
    path3 = destination + '/documents/' + file

    if os.path.exists(path2):
      print(f'Moving {file}...')
      shutil.move(path1, path3)
    else:
      os.mkdir(path2)
      print(f'Moving {file}...')
      shutil.move(path1, path3)

