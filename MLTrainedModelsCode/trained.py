import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw,ImageFont
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    model = load_model('letters.h5')
class_idx = ['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    model2 = load_model('digits.h5')
class_idx2 = ['0','1','2','3','4','5','6','7','8','9']

 
from segment_sentence import fun0
from segment_word import fun1
from segment_character import fun2
from rgb_to_mnist import fun3
from crop import fun4

input_image='akku.jpg'
print(' Text Address Image:')
image = Image.open('./images/'+input_image).convert("L")
plt.imshow(image,interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()

# Delete From Lines Folder 
path='./Lines/'
arr=os.listdir(path)
for line in arr:
    os.remove('./Lines/'+line)
    
fun0(input_image,'./images/')
mylist=[]
lines=os.listdir('./Lines/')
lines.sort()
l_lines=len(lines)
no=1
length = len(lines)
for i in range(length-1): 
    line = "new"+str(i+1)+".png"
    fun1(line)
    fun2()
    fun3()
    fun4()    
    ans=" "
    folders=os.listdir('./cropped/')
    l=len(folders)
    print("\n\n")
    #print("Segmented Into Characters")
    for fold in folders:
        path='./cropped/'+fold+'/'
        arr=os.listdir(path)
        j=1
        for data in arr:
            img = Image.open(path+data).convert("L")
            img = img.resize((28,28))
            im2arr = np.array(img)
            image = im2arr
            # show label for sample image
            '''
            plt.subplot(1,13,i)
            plt.imshow(image, cmap='gray', interpolation='none')
            plt.xticks([])
            plt.yticks([])
            '''
            image=np.reshape(image,(1,28,28,1))
            scores = model.predict(image)
            index = np.argmax(scores)
            #plt.title( str( class_idx[ index ] ))
            ans=ans+str(class_idx[ index ])
            ans
            j+=1
        #plt.show()
        ans+="  "
    no+=1
    mylist.append(ans)
    

line=lines[-1]
fun1(line)
fun2()
fun3()
fun4()
ans=" "
folders=os.listdir('./cropped/')
l=len(folders)
print("Line "+str(no))
print("\n\n")

#print("Segmented Into Characters")
for fold in folders:
    path='./cropped/'+fold+'/'
    arr=os.listdir(path)
    i=1
    for data in arr:
        img = Image.open(path+data).convert("L")
        img = img.resize((28,28))
        im2arr = np.array(img)
        image = im2arr
        # show label for sample image
        '''
        plt.subplot(1,13,i)
        plt.imshow(image, cmap='gray', interpolation='none')
        plt.xticks([])
        plt.yticks([])
        '''
        image=np.reshape(image,(1,28,28,1))
        scores = model2.predict(image)
        index = np.argmax(scores)
        #plt.title( str( class_idx2[ index ] ))
        ans=ans+str(class_idx2[ index ])
        i+=1
    #plt.show()
    ans+="  "
mylist.append(ans)
print(mylist)

img = Image.new('RGB', (500, 600))
d = ImageDraw.Draw(img)
d.rectangle((20, 30, 480, 570), outline='red', fill='white')
fontsize = 40 # starting font size
font = ImageFont.truetype("arial.ttf", fontsize)
d.text((25, 35), ' Digital Address', fill=(0, 255, 0),font=font)
offset=0
for item in mylist:
    _list=item.split()
    ans=""
    for i in _list[1:]:
        print(i,end=" ")
        ans+=i+" "
    d.text((35, 80+offset), ans, fill=(255, 0, 0),font=font)
    offset+=50
    print("\n")
print("\n\nFinal Result:")
plt.imshow(img, interpolation='nearest')
plt.xticks([])
plt.yticks([])

