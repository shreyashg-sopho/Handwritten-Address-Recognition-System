def fun0(image,directory):   
    import os
    import sys
    import cv2
    import numpy as np
    import ntpath
    
    def segment_sentence(image, directory):
        image=cv2.imread(directory+image)
        # grayscale the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # get threshold for pixel values
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh2 = cv2.threshold(gray, 127  , 255, cv2.THRESH_BINARY)
    
        # dilate the image
        kernel = np.ones((5, 100), np.uint8)
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    
        # find contours
        ctrs, hier = cv2.findContours(
            img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #print(len(ctrs))
        # sort contours
        sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])
        sorted_ctrs = sorted_ctrs[0:]
    
        sentences = []
        j=1
        for i, ctr in enumerate(sorted_ctrs):
    
            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)
    
            # Ignore small contours - Considered to be unwanted elements
            if ((w*h) < 5000):
               continue
    
            # Getting ROI
            roi = thresh2[y:y+h, x:x+w]
    
            # save each segmented image
            sentences.append(roi)
    
            cv2.imwrite('./Lines/'+"new"+str(j)+".png", roi)
            j+=1
            #print(sentences)
        return sentences
    segment_sentence(image, directory)
    
    
