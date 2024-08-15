from PIL import Image
import os
import glob
from pathlib import Path




renaming = 0
changing_sizes = 0
changing_extensions = 0

#renaming
extension = "png"
name_form ="frame_"

#changing sizes
WIDTH = 50#75
HEIGHT = 50#75

#cahnging extensions
old_extension = "webp"
new_extension = "png"

if renaming:
    i=0
    for file in glob.glob(f"D://Something from desktop/Renaming/For_rename/*.{extension}"):
        filename = glob.glob(f'D://Something from desktop/Renaming/For_rename/*.{extension}')[0]

        os.rename(f'{filename}',f'D://Something from desktop/Renaming/Renamed/{name_form}{i}.{extension}')

        i+=1


if changing_sizes:
    i=0
    for file in glob.glob(f"D://Something from desktop/Changing_sizes/For_change/*.{extension}"):
        filename = glob.glob(f'D://Something from desktop/Changing_sizes/For_change/*.{extension}')[0]
        
        for_open = filename.removeprefix('D://Something from desktop/Changing_sizes/For_change')
        img = Image.open(f"D://Something from desktop/Changing_sizes/For_change/{for_open}")
        resized_img = img.resize((WIDTH, HEIGHT))
        resized_img.save(f"D://Something from desktop/Changing_sizes/Changed/{i}.{extension}")

        i+=1
        os.remove(filename)



if changing_extensions:

    for file in glob.glob(f"D://Something from desktop/Changing_extension/{old_extension}/*.{old_extension}"):
        filename = glob.glob(f'D://Something from desktop/Changing_extension/{old_extension}/*.{old_extension}')[0]
        name = filename.removeprefix(f'D://Something from desktop/Changing_extension/{old_extension}')
        name = name.removesuffix(f'.{old_extension}')    
        p = Path(f'D://Something from desktop/Changing_extension/{old_extension}/{name}.{old_extension}')
        p.rename(p.with_suffix(f'.{new_extension}'))

