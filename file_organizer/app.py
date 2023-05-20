from pathlib import Path
import os
import shutil

extensions = []

path = Path("codes\\file_organizer")
for file in path.glob('*.*'):
    file = str(file)
    file_name = file.removeprefix('codes\\file_organizer\\')
    file_extension = file_name.split('.')[1]

    if (not file_extension in extensions):
        extensions.insert(-1, file_extension)

for ext in extensions:
    if ext == 'py':
        continue
    
    new_folder_path = '\\'.join([str(os.getcwd()), str(path), ext.upper()])
    os.mkdir(new_folder_path)

    for file in path.glob(f'*.{ ext }'):
        shutil.move(file, new_folder_path)
