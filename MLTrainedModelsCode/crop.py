import cv2
def fun4():
    from PIL import Image
    import numpy as np
    import os
    
            
    import shutil
    path='./cropped/'
    arr=os.listdir(path)
    for fold in arr:
        shutil.rmtree('cropped/'+fold)
        
    path='./words/'
    arr=os.listdir(path)
    #print(arr)
    
    for i in range(0,len(arr)):
        path = "./cropped/folder"+str(i)
        os.mkdir(path)
    
    path='./new_mnist/'
    folders=os.listdir(path)
    for fold in folders:
        paths='./new_mnist/'+fold+'/'
        arr = os.listdir(paths)
        for path in arr:
            img = Image.open(paths+path).convert("L")
            area=(115,35,332,250)
            cropped=img.crop(area)
            cropped.save('./cropped/'+fold+'/'+path)

