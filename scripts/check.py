import os

for old_name in os.listdir():
    if not os.path.isfile(old_name):
        continue
    print(old_name)