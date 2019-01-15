'''
******************************************************************************
 * Copyright 2018 IIT-CNR
 * 
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License.  You may obtain a copy
 * of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
 * License for the specific language governing permissions and limitations under
 * the License.
 ******************************************************************************
'''

import numpy as np
import cv2
import time 
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

count_img = 0

if (len(sys.argv) >= 2):
	video_path = sys.argv[1]
else:
	video_path = 0

print(video_path)

folder_name = raw_input("Please enter your name: ")
directory = os.path.join(os.path.join(dir_path,"train_img"), folder_name)
print "Image folder: " + directory

cap = cv2.VideoCapture(video_path)

if(cap.isOpened() == False):
	print("Error opening the video\n")
	sys.exit(0)

if not os.path.exists(directory):
    os.makedirs(directory)

while(cap.isOpened()):
    count ++
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    filename = os.path.join(directory,str(time.time()) + ".jpeg")

    cv2.imwrite(filename, frame)     # save frame as JPEG file
    if cv2.waitKey(1) & 0xFF == ord('q'):
	break
    if count == 3000:
	break
cap.release()
cv2.destroyAllWindows()
