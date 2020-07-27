#Jainam Sanghvi
#18BCE208
#Semester 4
#Division-D

#QUESTION 1

#Extract the text from the images and store the story in text file. Separate text file for each story. [Marks: 15]

# Python program to extract text from all the images in a folder 
# storing the text in corresponding files in a different folder 

#IMPORTING libraries
from PIL import Image   #This library is used for processing the image or creating image scratch.
import pytesseract as pt  #It is used to recognise the OCR tool for python
import cv2
import os
import numpy as np

#This is the path where the library tesseract is saved. It is open source text recognition OCR Engine. Used for extracting the printed text from images.
pt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

#This function converts the colour image to gray image and forming the array, and then extract text and then result is returned. 
def get_text(img_path,count):
    
    img = cv2.imread(img_path)                  #This is reading the image.
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Converting the colour image to gray image with the help of opencv.
    kernel = np.ones((1,1),np.uint8)            #Initializing the array and then used 12 times a dilation with a 1x1 structuring element (SE).
    img = cv2.dilate(img,kernel,iterations=1)   #Apply dilation to remove some noise.  
    img = cv2.erode(img,kernel,iterations=1)    #Apply erosion to remove some noise.
    cv2.imwrite("D:/Semester 4/PSC_SE/18BCE208_Gray_Images/" + "g_ " + str(count) + ".png",img) #Write the image after the conversion using opencv.
    result = pt.image_to_string(Image.open("D:/Semester 4/18BCE208.pdfPSC_SE/18BCE208_Gray_Images" + "/g_ " + str(count) + ".png")) #Extrcting and storing the result to the variable.
    return result   #Return the text of the single-single image.


path, dirs, files = next(os.walk("D:/Semester 4/PSC_SE/18BCE208_Text_files_q1")) #This tells us that the path given contains the total files and it stores each for all the subdirectories also.
file_count = len(files) #Stores the value of total files in the folder(integer value).

j = 1 
k = 0
for root,direc,files in os.walk('D:/Semester 4/PSC_SE/18BCE208_Images'):    #This tells us that the path given contains the total files and it stores each for all the subdirectories also.
    print(root)     #Just prints the root path of the path given.
    cou = len(files)    #Clculate the length of the total files in the sub directory.
    i=0         #This val=riable is used to check the file which we require and other to eliminate which doesn't have the content on the page.
    for file in files:  #one by one the files of photo which has images folder name will be iterated.
        i += 1
        path = os.path.join(root,file)      #Path of that file is joined with the root node and then it is stored in the variable path.
        if i == 1 or i==2 or i==3 or i == cou-1 or i == cou:    #This are the number which we don't want in the text files.
            continue
        ans = get_text(path,j)      #Here, the returned text that is extracted from the images is stored here.
        print(file)         #Just print the file name that we have extracted.
        j += 1              #Incrementing the value.
                
        with open("D:/Semester 4/PSC_SE/18BCE208_Text_files_q1/file_" + str(k) + ".txt","a", encoding="utf-8") as f:    #We open and append all the files seperate;y as per pdf one file is used to store the contect of whole nmovel.
            f.write(ans)    #Just write the content in the file.
            f.write("\n")   #After each time the new line is used.
            f.close()       #Close the file.
    k += 1                  #New file to be created as file_1,2,...

