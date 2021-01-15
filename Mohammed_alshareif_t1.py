#########required lib to get the code run
import urllib.request
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
#import cv2
from PIL import Image
import imagehash
import re
import dhash
from PIL import Image
import json
import urllib.parse
######read images and compare the files 
####image 1: https://images.ctfassets.net/3prze68gbwl1/asset-17suaysk1qa1jhl/d276861783e0ab0ffab32afcdc84d597/python-socket-programming.jpg?h=445&w=1024
#####image 2 https://pluralsight.imgix.net/paths/python-7be70baaac.png
def downloadImages(image1,image2,auth):
	if not image1:
		print("Image one could not be empty ")
		return
	if not image2:
		print("Image Two could not be empty ")
		return
	img1=image1+"&auth="+auth
	img2=image2+"&auth="+auth
	resource = urllib.request.urlopen(image1)
	output = open("file1.jpg","wb")
	output.write(resource.read())
	output.close()
	print("Image one should be downloaded from path....."+img1)
	resource = urllib.request.urlopen(image2)
	output = open("file2.jpg","wb")
	output.write(resource.read())
	output.close()
	print("Image one should be downloaded from path....."+img2)
	print("Please wait while comparing files.....")
	compare_images("file1.jpg", "file2.jpg", "Task One")


def compare_images(imageA, imageB, title):
	image1=Image.open(imageA)
	image2=Image.open(imageB)
	imageHashInt=dhash.dhash_int(image1,8)
	imageHashInt2=dhash.dhash_int(image2,8)
	res=dhash.get_num_bits_different(imageHashInt,imageHashInt2)	
	finalRes=str(100-((res/128)*100))+'%'
	x={"Similarity is ":finalRes}
	y = json.dumps(x)
	print(y)
	

def isValidURL(str):
 
    # Regex to check valid URL 
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty 
    # return false
    if (str == None):
        exit("Error in URL format")
 
    # Return if the string 
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
         exit("Error in URL format")


print("Task Assessment Version 0.1")
print("Mohammed Al Shareif - Task, compare two images ")
auth=input("Enter you Auth: ")
print("Your Auth Key is:"+auth)
image1=input("Enter path for image 1: ")
imageFormat=isValidURL(image1)
image2=input("Enter path for image 2: ")
imageFormat=isValidURL(image2)
userAction=input("Enter 0 to kill the process or any other key to processed: ")
if userAction==0:
	exit("Thank u")
else:
	print("processing")
	downloadImages(image1,image2,auth)


