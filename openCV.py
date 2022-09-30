from typing import Reversible
import numpy as np
import cv2
import os

filename = 'video5.avi'
frames_per_seconds = 24.0
my_res = '720p'

# ffmpg


def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


std_dimentions = {
    "480p": (640, 480),
    "720p": (1280, 720),
}


def get_dims(cap, res='720'):
    width, height = std_dimentions['720p']
    if res in std_dimentions:
        width, height = std_dimentions[res]
    change_res(cap, width, height)
    return width, height


VIDEO_TYPE ={
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}
def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)
dims = get_dims(cap, res=my_res)
video_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dims )



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    gaus = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 5)
    retval, otsu_threshold = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)
    gaus_otsu = cv2.adaptiveThreshold(
    otsu_threshold, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 5)
    out.write(otsu_threshold)
    frame = rescale_frame(frame, percent=100)
    # Our operations on the frame come here
    
    # Display the resulting frame
    #cv2.imshow('frame', frame)
    cv2.imshow('frame', gaus_otsu)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


#When everithing done, release the picture
cap.release()
out.release()
cv2.destroyAllWindows()
