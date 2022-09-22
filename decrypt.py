import os
from cryptography.fernet import Fernet


files = []
for file in os.listdir():
        if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" or file == "requirements.txt":
                continue
        if os.path.isfile(file):
                files.append(file)

with open("key.txt","rb") as thefile:
    secretkey = thefile.read()

print(secretkey)

for file in files:
        with open(file,"rb") as thefile:
            content = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(content)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
