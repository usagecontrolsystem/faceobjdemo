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

cap = cv2.VideoCapture("http://146.48.99.48:8080/stream/video.mjpeg")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
print "hello"
out = cv2.VideoWriter('/home/antonio/output.avi',fourcc, 10, (1920,1080))
#while(cap.isOpened()):
for i in range(1, 500):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        # write the flipped frame
        out.write(frame)
        print str(i)
        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
