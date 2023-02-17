import os
import hashlib

currpath = os.getcwd()
print(currpath)
directory = "./cs2107assign1/dist"
for filename in os.listdir(directory) :
    path = os.path.join(directory, filename)
    with open(path, "rb") as image:
        f = image.read()
        md5 = hashlib.md5(f).hexdigest()
        if(md5 == '8ac8fb3045e78a65a9df5685fe715dff'):
            sha1 = hashlib.sha1(f).hexdigest()
            print(type(filename))
            print("CS2107{{{0}_{1}}}".format(filename, sha1))
            
    
    