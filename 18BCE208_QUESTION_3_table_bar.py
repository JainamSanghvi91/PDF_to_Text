#Jainam Sanghvi
#18BCE208
#Semester 4
#Division-D

#QUESTION 3
#Show table which is showing the story name, total number of pages in each story and display
#them in bar chart. [Marks: 10]

#Importing Necessary Libraries.
import pandas as pd 
from PIL import Image #This library is used for processing the image or creating image scratch.
import pytesseract as pt  #It is used to recognise the OCR tool for python
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import texttable as tt

#This is the path where the library tesseract is saved. It is open source text recognition OCR Engine. Used for extracting the printed text from images.
pt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

#This function converts the colour image to gray image and forming the array, and then extract text and then result is returned. 
def get_text(img_path,count):

    img = cv2.imread(img_path)                  #This is reading the image.
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Converting the colour image to gray image with the help of opencv.
    kernel = np.ones((1,1),np.uint8)            #Initializing the array and then used 12 times a dilation with a 1x1 structuring element (SE).
    img = cv2.dilate(img,kernel,iterations=1)   #Apply dilation to remove some noise.
    img = cv2.erode(img,kernel,iterations=1)    #Apply erosion to remove some noise.
    cv2.imwrite("D:/PSC_SE/18BCE208_Gray_Images/" + "g_ " + str(count) + ".png",img)     #Write the image after the conversion using opencv.
    result = pt.image_to_string(Image.open("D:/PSC_SE/18BCE208_Gray_Images" + "/g_ " + str(count) + ".png")) #Extrcting and storing the result to the variable.
    return result   #Return the text of the single-single image.

name=[]     #a list is created for storing all the names of stories.
for root,direc,files in os.walk('D:/PSC_SE/18BCE208_Name Of Story'): #This loop is used to iterate all the story title stored in the path given in os.walk()
    i=0     #This variable is used to pass to the function get_text() and in that order it will get saved in the folder.
    for file in files:  #one by one the files of photo which has title will be iterated.
        i += 1
        path = os.path.join(root,file)      #Path of that file is joined with the root node and then it is stored in the variable path.
        na = get_text(path,i)               #Function is called to get the text form of the titke of the story.
        name.append(na)                     #The name of the story is appended in the name list.(all the names of story are stored here) 
        print(na)                           #Just printing the name of story on the console. 
print(name)                     #Print the list containing the name sof story.

pages = []      #a list is created for storing all the total page numbers.
for path, dirs, files in os.walk("D:/PSC_SE/18BCE208_Images"):       #This loop is used to iterate all the images folder in the path given in os.walk()
    count=0     #This variable is used to increment the number as the total number of pages.
    for file in files:      #one by one the files of photo which has title will be iterated.
        path = os.path.join(root,file)    #Path of that file is joined with the root node and then it is stored in the variable path.
        count += 1                        #Increment the number as the image is found.
    pages.append(count)                   #The number of pages is appended in the pages list.(all the number of pages are stored here)     
pages.remove(0)                           #The number at the first value at index is 0 as value is 0 so we don't need that.
print(pages)                #Print the list containing the name sof story.

tab = tt.Texttable()        #This is a object named tab and is initialized.
titles = ['Name of Story','Total Number of Pages']  #This are the titles that are required in the table.
tab.header(titles)      #Printing the names of titles in the header means the column names.
data = [titles] + list(zip(name, pages))    #Now as list(zip(name,pages)) means we are creating new summary list and in that both values as number of pages and name of story is zipped together and concatenated to the title means merged in the same table.

for row in zip(name,pages):     #Now as ziped contains combine list values and one by one the loop will run and the values will be added.
    tab.add_row(row)            #This command helps to add row in the table.

s = tab.draw()                  #This completes the table.
print (s)                       #Just printing the table on the console.

##fig = go.Figure(data=[go.Table(
##    header=dict(values=['Name of Story', 'Total Pages']),
##    cells=dict(values=[name,pages]))])
##
##fig.update_layout(width=500, height=800)
##fig.show()

fig = plt.figure(figsize=(10,5)) #Create object to save the figure and also the size the graph. 
plt.bar(name,pages)             #This is used to plot the bar graph.
plt.xlabel('Name of Story')     #This is labelling the x-axis.
plt.ylabel('Number of pages')   #This is labelling the y-axis.
plt.title('SESSIONAL ASSIGNMENT')   #This is given title  
fig.savefig('Output_of_bar_graph.jpg') #This will save the graph.
plt.show()                      #This is displaying the graph.


