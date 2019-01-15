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

import cv2
import time
import os
import datetime

#cam = "http://146.48.99.159:8080/stream/video.mjpeg"
#cam = "http://146.48.99.48:8080/stream/video.mjpeg"
cam = "http://146.48.53.72:8080/stream/video.wmv"
directory = "stream_saved"
FILE_OUTPUT = 'output.avi'

save = 0
streaming_closed = 0


cap = cv2.VideoCapture(cam)

if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")

if not os.path.exists(directory):
    os.makedirs(directory)    



fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('stream_saved/' + str(time.time()) + '.avi',fourcc, 10, (1280,720))

frame_wrote = 0

while(True):

    #if the streaming is closed, try to reopen the streaming
    if streaming_closed == 1:
	cap = cv2.VideoCapture(cam)

    ret, current_frame = cap.read()
    
    #if ret is False the streaming is closed, set the streaming_closed to one and skip the cycle
    #if ret is True set the streaming_closed variable to 0 and continue the cycle because the streaming is opened
    if ret == False:
	print("Streaming video closed")
	streaming_closed = 1
        out.release()
	continue
    else:
	streaming_closed = 0


    now = datetime.datetime.now()
    #passed 5 minutes write 400 frames to a video
    if now.minute % 1 == 0:
	if frame_wrote < 400:
        	frame = cv2.flip(current_frame,1)
		#frame = current_frame       	
		# write the flipped frame
        	out.write(frame)
        	frame_wrote +=1
	else:
		frame_wrote = 0
		out.release()
		out = cv2.VideoWriter('stream_saved/' + str(time.time()) + '.avi',fourcc, 10, (1920,1080))
        if save == 0:
		print("Storing streaming")
		save = 1
    else:
	save = 0



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture
cap.release()
cv2.destroyAllWindows()
out.release()
