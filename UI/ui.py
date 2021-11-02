mport pygame
import random
import glob
import os
import csv
import re
import pytesseract
import cv2

grey  = (200,200,200)
cyan = (0,255,255)
white = (255,255,255)
black = (0,0,0)
xcor = 550
ycor = 100
pygame.init()


display_width=1000
display_height=600

l_arrow = pygame.image.load("previous.png")
l_arrow = pygame.transform.scale( l_arrow  , (90, 35))

r_arrow = pygame.image.load("next.png")
r_arrow = pygame.transform.scale( r_arrow  , (90, 35))

extract = pygame.image.load("extract.png")
extract = pygame.transform.scale( extract  , (180, 35))

save = pygame.image.load("save.png")
save = pygame.transform.scale( save  , (180, 35))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, disp_x, disp_y,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect = (disp_x , disp_y)
    gamedisplay.blit(TextSurf, TextRect)
def image_display(image , x, y):
    gamedisplay.blit(image , (x,y))


img_dir = "./images_of_lines"
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
count = 0
text = ""
data_py = []

for f1 in files:
    img = cv2.imread(f1)
    data_py.append(img)
    img = pygame.image.load(f1)
    img = pygame.transform.scale( img  , (300, 300))
    data.append(img)
    
    
max_count = len(data)
print(max_count)
lines = []
gamedisplay = pygame.display.set_mode ((display_width, display_height))
gameexit=False

while not gameexit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                x, y = event.pos
                print(x,y)
                if  (x > 110 and x < 290) and (y > 420 and y < 450):
                        print("IN EXTRACT")
                        text = pytesseract.image_to_string(data_py[count])
                        
                        lines = text.split("\n")
                        cleared_lines = [0,0,0,0,0,0,0]

                        str0 = lines[0]
                        temp = str0.split(" ")
                        cleared_lines[0] = temp[1:]
                        print(lines[0])
                        del temp[:]

                        str1 = lines[1]
                        temp = str1.split(" ")
                        cleared_lines[1] = temp[1:]
                        del temp[:]

                        str2 = lines[2]
                        temp = str2.split(" ")
                        cleared_lines[2] = temp[1:]
                        del temp[:]


                        str3 = lines[3]
                        temp = str3.split(" ")
                        cleared_lines[3] = temp[1:]
                        del temp[:]

                        str4 = lines[4]
                        temp = str4.split(" ")
                        cleared_lines[4] = temp[1:]
                        del temp[:]

                        str5 = lines[5]
                        temp = str5.split(" ")
                        cleared_lines[5] = temp[1:]
                        del temp[:]

                        str6 = lines[6]
                        temp = str6.split(" ")
                        cleared_lines[6] = temp[1:]
                        del temp[:]

                        
                            
                        del cleared_lines [:]
                if  (x > 110 and x < 290) and (y > 460 and y < 495):
                        print("IN EXTRACT")
                        text = pytesseract.image_to_string(data_py[count])
                        
                        lines = text.split("\n")
                        cleared_lines = [0,0,0,0,0,0,0]

                        str0 = lines[0]
                        temp = str0.split(" ")
                        cleared_lines[0] = temp[1:]
                        print(lines[0])
                        del temp[:]

                        str1 = lines[1]
                        temp = str1.split(" ")
                        cleared_lines[1] = temp[1:]
                        del temp[:]

                        str2 = lines[2]
                        temp = str2.split(" ")
                        cleared_lines[2] = temp[1:]
                        del temp[:]


                        str3 = lines[3]
                        temp = str3.split(" ")
                        cleared_lines[3] = temp[1:]
                        del temp[:]

                        str4 = lines[4]
                        temp = str4.split(" ")
                        cleared_lines[4] = temp[1:]
                        del temp[:]

                        str5 = lines[5]
                        temp = str5.split(" ")
                        cleared_lines[5] = temp[1:]
                        del temp[:]

                        str6 = lines[6]
                        temp = str6.split(" ")
                        cleared_lines[6] = temp[1:]
                        del temp[:]

                        for i in range(len(cleared_lines)):
                            cleared_lines[i] = " ".join(cleared_lines[i])
                        with open("output.csv", 'a', newline='') as myfile:
                            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                            wr.writerow(cleared_lines)
                            
                        del cleared_lines [:]
                elif (x > 50 and x < 140) and (y > 370 and y < 405):
                    print("LEFT")
                    if count != 0 :
                        count -= 1
                    else:
                        count = max_count-1

                elif (x > 260 and x < 350) and (y > 370 and y < 405):
                    print("Right")
                    if count != max_count-1:
                        count +=1
                    else:
                        count = 0



    gamedisplay.fill(cyan)
    ycor = 100
    for string in lines:
         string_msg=""
         for chars in string:
             uft8 = ord(chars)
             if (uft8 == 58) or (uft8 == 32) or (uft8 >=97  and uft8<=122) or (uft8 >=65  and uft8<=90) or (uft8 >=48  and uft8<=57):
                 string_msg += chars
             
         message_display(string_msg.upper(), xcor, ycor, 20)
         del string_msg
         ycor = ycor + 30
    image_display(r_arrow, 260, 370)
    image_display(l_arrow, 50, 370)
    image_display(extract, 110, 420)
    image_display(save, 110, 460)
    image_display(data[count], 50,50)
    pygame.display.update()

pygame.quit()
