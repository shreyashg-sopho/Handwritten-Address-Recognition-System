def fun2():
    import cv2
    import numpy as np
    import os
    import sys
    import ntpath
    
    """ To sort the contours in 4 ways
    		left-to-right
    		right-to-left
    		top-to-bottom
    		bottom-to-top
    """
    def sort_contours(cnts, method="left-to-right"):
        # initialize the reverse flag and sort index
        reverse = False
        i = 0
        # handle if we need to sort in reverse
        if method == "right-to-left" or method == "bottom-to-top":
            reverse = True
        # handle if we are sorting against the y-coordinate rather than
        # the x-coordinate of the bounding box
        if method == "top-to-bottom" or method == "bottom-to-top":
            i = 1
        # construct the list of bounding boxes and sort them from top to bottom
        boundingBoxes = [cv2.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][i], reverse=reverse))
        # return the list of sorted contours and bounding boxes
        return (cnts, boundingBoxes)
    
    
    def segment_character(image, directory):
        image=cv2.imread(directory+image)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        row, col= image.shape
        ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        '''
        #dilation
        kernel = np.ones((5,5), np.uint8)
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)
        
        #adding GaussianBlur (this is used for removal of noise)
        gsblur=cv2.GaussianBlur(img_dilation,(5,5),0)
        '''
        ctrs, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        (ctrs, boundingBoxes) = sort_contours(ctrs, method="left-to-right")
    
        characters = {}
        count = 0
        # For each contour, find the bounding rectangle and draw it
        for i, cnt in enumerate(ctrs):
            x, y, w, h = cv2.boundingRect(cnt)
            # Ignore small contours - Considered to be unwanted elements
            if ((w*h) < 100):
                continue
            # Find the segmented character and store
            roi = thresh2[y:y+h, x:x+w]
            # Analyse the contour bounding box x,y,h,w values to get better understanding
            characters[count] = roi
            count = count + 1
    
        return characters
    
    
    import shutil
    path='./segmented_img/'
    arr=os.listdir(path)
    for fold in arr:
        shutil.rmtree('segmented_img/'+fold)
        
    path='./words/'
    arr=os.listdir(path)
    #print(arr)
    
    for i in range(0,len(arr)):
        path = "segmented_img/folder"+str(i)
        os.mkdir(path)
    
        
    j=0   
    for img in arr:
        characters= segment_character(img, './words/')
        path = "segmented_img/folder"+str(j)+"/"
        j+=1
        i=10
        for key in characters:
            imageName = str(i) + '.png'
            cv2.imwrite(path+imageName, characters[key])
            i+=1