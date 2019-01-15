# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np

def get_image(camera):
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im

def get_text(): 
    # construct the argument parse and parse the arguments

    # load the example image and convert it to grayscale
    # Camera 0 is the integrated web cam on my netbook
    camera_port = 0
    
    #Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30
    
    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    camera = cv2.VideoCapture(camera_port)
    
    # Captures a single image from the camera and returns it in PIL format
    
    
    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in range(ramp_frames):
        temp = get_image(camera)
    print("Taking image...")
    # Take the actual image we want to keep
    camera_capture = get_image(camera)
    
    # You'll want to release the camera, otherwise you won't be able to create a new
    # capture object until your script exits
    del(camera)

    # image = cv2.imread(image_address)
    gray = cv2.cvtColor(camera_capture, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    
    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    # print(text)
    text =  text.split("\n")
    name,rollno = '', ''
    out = {}
    for i in text:
        if "AM." in i:
            i = i.split(" ")
            print(i)
            name = i[0:-1]
            name = " ".join(name)
            rollno = i[-1]
    orderid = "xyz"
    agent = "Delhivery"
    out = {'name': name,'rollno': rollno,"orderid":orderid,"agent":agent}
    return out

def get_imText(path):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    # print(text)
    text =  text.split("\n")
    # print(text)
    k = text[0].split(" ")
    orderid = k[-1]
    name = text[2].split(" ")[2:]
    name = " ".join(name)
    # rollno = text[1]
    for i in text:
        if "AM." in i:
            i = i.split(" ")
            rollno = i[-1]
    agent = text[-1].split(" ")[-1]
    print("orderid :",orderid)
    print("name :",name)
    print("Rollno :",rollno)
    print("Agent :",agent)
    out = {'name': name,'rollno': rollno,"orderid":orderid,"agent":agent}
    return (out)
        # return (inputstring)
#get_imText("C:\\Users\\Vamshi\\hack\\acour\\track\\demo.png")
#get_text()