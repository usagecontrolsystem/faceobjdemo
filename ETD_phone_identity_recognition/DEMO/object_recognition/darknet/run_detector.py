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

#python3 run_detector.py http://146.48.99.48:8080/stream/video.mjpeg

import subprocess 
import sys
import argparse


video_path = sys.argv[1]

DETECTOR_COMMAND = ["sudo", "./darknet", "detector", "demo", "cfg/coco.data", "cfg/yolov3.cfg", "yolov3.weights", video_path]



test = subprocess.Popen(DETECTOR_COMMAND, stdout=subprocess.PIPE)
output = test.communicate()[0]

