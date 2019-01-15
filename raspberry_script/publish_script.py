#!/usr/bin/python3
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
import argparse
from socket import *
import subprocess
import time

PLAY = "PERMIT"
PAUSE = "DENY"
CLOSE = "TERMINATE"


client_socket = socket(AF_INET, SOCK_DGRAM)
addr = ("127.0.0.1", 12345)
client_socket.sendto("start".encode(), addr)

status = ""
command = ""
while True: 
    
    data, server = client_socket.recvfrom(1024)
    command = str(data)
    
    if PLAY in command :
        print("PLAY")
        subprocess.call(["uv4l", "--driver", "raspicam","--auto-video_nr", "--encoding", "h264", "--width", "1920", "--height", "1080"])
    if "TERMINATE" in command: 
        #put your username here
        subprocess.call(["sudo", "pkill", "uv4l"])
        status = "STOP"
        time.sleep(20)
        client_socket.sendto("start".encode(), addr)
        
    
