#!/usr/bin/env python
'''
@Description: Barcode scanner
@Author: Jack Huang
@Date: 2019-05-22 10:33:50
@LastEditTime: 2019-05-22 13:27:35
@LastEditors: Please set LastEditors
'''

import cv2
import datetime
from PIL import Image
from pyzbar.pyzbar import decode
import clipboard

from time import sleep
from note import Note


cap = cv2.VideoCapture(0)
# pre_init(44100, -16, 1, 1024)
# pygame.init()
start_time = datetime.datetime.now()
while True:
    # 1. Get the image of QR code 
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 2. Decode the image
    info = decode(gray)
    # 3. Get the result
    if len(info) != 0: 
        result = info[0].data.decode("utf-8")
        #print(result)
        
        # 4. Play the sound reminder
        Note(440).play(-1)
        sleep(0.0005)
        # 5. Copy the content to clipboard
        clipboard.copy(result)
        break
    now = datetime.datetime.now()
    if (now - start_time).seconds > 30:
        break
cap.release()
