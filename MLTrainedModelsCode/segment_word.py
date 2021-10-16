def fun1(input_image): 
    import os
    import sys
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    import ntpath
    from PIL import Image
    
    def segment_word(image, directory):
        image=cv2.imread(directory+image)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # get threshold for pixel values
        ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        # dilate the image
        kernel = np.ones((5, 40), np.uint8)
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    
        # find contours
        ctrs, hier = cv2.findContours(
            img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        # sort contours
        sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
        sorted_ctrs = sorted_ctrs[0:]
    
        words = []
        j=1
        for i, ctr in enumerate(sorted_ctrs):
    
            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)
    
            # Used to remove stray elements
            if ((w*h) < 1000):
                continue
    
            # Getting ROI
            roi = thresh2[y:y+h, x:x+w]
    
            # add each segmented image to list
            words.append(roi)
            cv2.imwrite("./words/new"+str(j)+".png", roi)
            j+=1
    
        return words
    
    path='./words/'
    arr=os.listdir(path)
    for fold in arr:
        os.remove('./words/'+fold)
    # for each line
    image = Image.open('./Lines/'+input_image).convert("L")
    plt.imshow(image,interpolation = 'bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    yo=segment_word(input_image,'./Lines/')
    print("\n\n")
    print("  Segmented Into ",np.array(yo).shape[0]," Words")
    
    words=os.listdir('./words/')
    i=1
    for word in words:
        print("word",i)
        image = Image.open('./words/new'+str(i)+'.png').convert("L")
        plt.imshow(image,interpolation = 'bicubic')
        plt.xticks([])
        plt.yticks([])
        plt.show()
        i+=1
