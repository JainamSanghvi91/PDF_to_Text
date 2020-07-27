#Jainam Sanghvi
#18BCE208
#Semester 4
#Division-D

#PDF TO IMAGE CONVERSION

#BASIC REQUIREMENTS TO START THE ASSIGNMENTS:

#Select/Scan/Download atleast 5 kids story books. Use OpenCV or NLTK kind of library to read text
#from it. You can download free story book pdf file from https://monkeypen.com/pages/free-
#childrens-books and take/convert images from it.

#IMPORT LIBRARIES
import pdf2image
from PIL import Image  #This library is used for processing the image or creating image scratch.
import time
import os

#Basically in this code we are taking each pdf file which contains story and then converting
#that pdf file to different Images.

#DECLARE CONSTANTS
DPI = 200               #DPI-dots per inch, it is used to see the relative resolution of OUTPUT pdf, but should be not above 300.

OUTPUT_FOLDER = None    #Folder where the output file is to be generated bu none because we need to save in different folders. Because we need to further use the particular folder .
                        #The converted images will be written there to save system memory.

FIRST_PAGE = None       #First page that will be converted. It will only convert first page and for eg. we have 15 pages in pdf then for rest we need to use loop.

LAST_PAGE = None        #Last page that will be converted. It will only convert last page and for eg. we have 15 pages in pdf then for rest we need to use loop.

FORMAT = 'jpg'          #File format or the output images. Supported values are ppm, jpeg, png and tiff.

THREAD_COUNT = 1        #Number of threads to use when converting the PDF. Limited to the actual number of pages.

USERPWD = None          #Password for the PDF if it is password-protected.

USE_CROPBOX = False     #Uses the PDF cropbox instead of the default mediabox.
                        #This is a rather dark feature that should be set to true when the module does not seem to work with your data.

STRICT = False          #Raises PDFSyntaxError when the PDF is partially malformed. Most PDF are partially malformed and that parameter should be kept to False.

#In this Function we are converting the pdf file to images and also calcultaing the total time taken by the single pdf to convert all the images. 
def pdftoimg(PDF_PATH):    
    start_time = time.time() #The current time when the pdf starts to convert to images
    convert_pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT) #This is converting the pdf to image and all the terms are explained above.
    print ("Time taken : " + str(time.time() - start_time))#Total time will be displayed end_time - start_time.
    return convert_pil_images #Returns the PIL_image.

#This saves all the image to the specific folder and in the specific format.     
def save_images(convert_pil_images,i):
    #This method helps in converting the images in PIL Image file format to the required image format
    index = 'A' #Initializing the variable to save the image with thar variable name.
    for image in convert_pil_images:    
        image.save("D:/Semester 4/PSC_SE/18BCE208_Images/Colour_Image_" + str(i) + "/Image_" + index + ".jpg") #This saves the image to the desired folder and variable is passed by the main function ans A so Colour_Image_A is the folder name.
        index = chr(ord(index) + 1) #Incremented for the image to save as Image_A,Image_B,... so on.

#if __name__ == "__main__":
for root,direcs,files in os.walk('D:/Semester 4/PSC_SE/18BCE208_Novels'): #This os.walk() function requires the path of root directory and then automatically runs the child files.
    i='A'   #Initializing the variable and this is used for saving in the folder name as A,B,...
    for file in files:  #Here we have the total files which we want to convert to images and they are iterated one by one.
        print(file) #This will print the file name which we are iterating and then the path for the each folder is passed in the path variable and then passed to pdftoimg. 
        path = os.path.join(root,file)  #This gives the path for the each folder one by one and we use to join  
        if i==3:    #Here we have eliminated this page because it contains the code that cannot be converted to colour.
            continue
        convert_pil_images = pdftoimg(path) #Here in the pdftoimg we pass the path to the function and then in return we get all the pil_images. 
        save_images(convert_pil_images,i)   #We got the images and also the value of i as A,B,... then pass to save_images to save the images to the folder.
        i = chr(ord(i) + 1)     #As the folfer name is of Colour_Image_A,Colour_Image_B... so we need to increment in the character format.
