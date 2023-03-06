import os
from PIL import Image as im

print(os.getcwd())
with open('./cs2107assign1/body.ppm.ecb','rb') as f:
    data = f.read()

h = 900;
while(True):
    if (h > 3000):
        print("cannot find")
        break;
    
    try:
        
        with open('body.ppm', 'wb') as f:
            f.write("P6\n940 {}\n255\n".format(h).encode())
            f.write(data)

        
        file_name = "body.ppm"
        
        image = im.open(file_name)
        # isok = image.verify()
        # print(isok)
        # if(isok):
        #     break
        image.show()    
    
    except Exception as  e:
        print(e)
        if(h%10 == 0):
            print("h: {}".format(h))
        
    h+=1
    
    

print(h)
