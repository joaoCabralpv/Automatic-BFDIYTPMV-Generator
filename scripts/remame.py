import os
import re
import pathlib
import shutil
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

working_dir = pathlib.Path().resolve()
seasons = ["BFDI","BFDIA","IDFB","BFB","TPOT","OTHER"]
for season in seasons:
    if not os.path.exists(season):
        os.makedirs(season)

for old_name in os.listdir():
    if not os.path.isfile(old_name):
        continue
    #print(old_name)
    new_name = re.sub('\[.*?\]', '', old_name)
    new_name = new_name.replace(" .",".").replace("BFDI:TPOT ","TPOT ")
    if "BFDI：TPOT " in new_name:
        new_name = new_name.replace("BFDI：","")
    folder = new_name[0:new_name.find("：")]
    new_name = new_name.replace("：","")
    for season in seasons:
        if season+" " in new_name:
            old_path = os.path.join(working_dir,old_name)
            new_path = os.path.join(working_dir,season,folder,new_name)
            print(new_path)
            os.renames(old_path,new_path)
            break
