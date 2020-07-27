#Jainam Sanghvi
#18BCE208
#Semester 4
#Division-D

#QUESTION:2

#Each text file store the information like Name of story, Author Name, Publisher details and entire story. [Marks: 15]

# Python program to extract text from all the images in a folder 
# storing the text in corresponding files in a different folder 

#IMPORTING libraries
from PIL import Image #This library is used for processing the image or creating image scratch.
import pytesseract as pt #It is used to recognise the OCR tool for python.
import cv2
import os
import numpy as np

#This is the path where the library tesseract is saved. It is open source text recognition OCR Engine. Used for extracting the printed text from images.
pt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

#This function converts the colour image to gray image and forming the array, and then extract text and then result is returned. 
def get_text(img_path,count):

    img = cv2.imread(img_path)                      #This is reading the image.
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)      #Converting the colour image to gray image with the help of opencv.
    kernel = np.ones((1,1),np.uint8)                #Initializing the array and then used 12 times a dilation with a 1x1 structuring element (SE).
    img = cv2.dilate(img,kernel,iterations=1)       #Apply dilation to remove some noise.
    img = cv2.erode(img,kernel,iterations=1)        #Apply erosion to remove some noise.
    cv2.imwrite("D:Semester 4//PSC_SE/18BCE208_Gray_Images/" + "g_ " + str(count) + ".png",img) #Write the image after the conversion using opencv.
    result = pt.image_to_string(Image.open("D:/PSC_SE/18BCE208_Gray_Images" + "/g_ " + str(count) + ".png")) #Extrcting and storing the result to the variable.
    return result   #Return the text of the single-single image.


path, dirs, files = next(os.walk("D:/Semester 4/Semester 4/PSC_SE/18BCE208_Text_files_q1"))
file_counts = len(files)

name=[]     #a list is created for storing all the names of stories.
for root,direc,files in os.walk('D:/Semester 4/PSC_SE/18BCE208_Name Of Story'):     #This loop is used to iterate all the story title stored in the path given in os.walk()
    i=0     #This variable is used to pass to the function get_text() and in that order it will get saved in the folder.
    for file in files:      #one by one the files of photo which has title will be iterated.
        i += 1
        path = os.path.join(root,file)      #Path of that file is joined with the root node and then it is stored in the variable path.
        na = get_text(path,i)               #Function is called to get the text form of the title of the story.
        name.append(na)                     #The name of the story is appended in the name list.(all the names of story are stored here) 
        print(na)                           #Just printing the name of story on the console. 
print(name)                     #Print the list containing the name sof story.

author=[]   #a list is created for storing all the names of author.
for root,direc,files in os.walk('D:/Semester 4/PSC_SE/18BCE208_Name Of Author'):    #This loop is used to iterate all the author name stored in the path given in os.walk()
    i=0     #This variable is used to pass to the function get_text() and in that order it will get saved in the folder.
    for file in files:      #one by one the files of photo which has author name will be iterated.
        i += 1
        path = os.path.join(root,file)      #Path of that file is joined with the root node and then it is stored in the variable path.
        na = get_text(path,i)               #Function is called to get the text form of the name of the author.
        author.append(na)                   #The name of the story is appended in the name list.(all the names of author of story are stored here)
        print(na)                           #Just printing the name of author of the story on the console.
print(author)               #Print the list containing the name of all the authors of stories.

publisher=[]   #a list is created for storing all the names of publisher.
for root,direc,files in os.walk('D:/Semester 4/PSC_SE/18BCE208_Name Of Publisher'):    #This loop is used to iterate all the publisher's name stored in the path given in os.walk()
    i=0     #This variable is used to pass to the function get_text() and in that order it will get saved in the folder.
    for file in files:      #one by one the files of photo which has title will be iterated.
        i += 1
        path = os.path.join(root,file)      #Path of that file is joined with the root node and then it is stored in the variable path.
        na = get_text(path,i)               #Function is called to get the text form of the publisher of the story.
        publisher.append(na)                   #The name of the story is appended in the name list.(all the names of publisher of the story are stored here)
        print(na)                           #Just printing the name of publisher of the story on the console.
print(publisher)               #Print the list containing the name of publisher of stories.

k = 0       #New file to be created as file_1,2,...
for i in range(1,file_counts+1):    #It will run for total text files. 
    k += 1
    with open("D:/Semester 4/PSC_SE/18BCE208_Text_files_q2/file_" + str(k) + ".txt","w", encoding="utf-8") as f1:  #We open and append all the files seperate;y as per pdf one file is used to store the contect of whole nmovel.
        f1.write("NAME OF THE STORY IS:")  #This is to append in the file.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write(name[i-1])  #This is to append in the file.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write("NAME OF THE AUTHOR OF THE STORY IS:")  #This is to append in the file.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write(author[i-1])  #This is to append in the file.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write("NAME OF THE PUBLISHER OF THE STORY IS:")  #This is to append in the file.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write(publisher[i-1])  #This is to append in the file.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        f1.write("\n")      #This is used to change the line , i.e. new line.
        with open("D:/Semester 4/PSC_SE/18BCE208_Text_files_q1/file_" + str(k) + ".txt","r", encoding="utf-8") as file:  #We will open the old file done in que:2.
            line = file.readlines()     #Then in new file after all content above steps done then append all the content of the old file done in below steps. 
        for l in line:  
            f1.write(l)
        f1.close()   # Then close the files.

