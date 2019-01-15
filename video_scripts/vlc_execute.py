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
import vlc
import time
import argparse
from socket import *
import sys

def get_args(): 
    parser = argparse.ArgumentParser(description="run the given video filename using the socket passed")
    parser.add_argument("--file_path", type=str, default=None, help="path of the video to show")
    parser.add_argument("--socket", type=str, default=None, help="insert the port on which the serverport of the PEP is listening")
    args = parser.parse_args()
    return args

PLAY = "PERMIT"
PAUSE = "DENY"
CLOSE = "TERMINATE"

args = get_args()
path_file = args.file_path
client_socket = socket(AF_INET, SOCK_DGRAM)
addr = ("127.0.0.1", 12345)

client_socket.sendto("start", addr)

my_song = vlc.MediaPlayer(path_file)

my_song.pause()

command = ""
status = "UNKNOWN"

while True:
    #read from socket
    
    data, server = client_socket.recvfrom(1024)
    print data
    command = data
    
    if PLAY in command and status not in command:
        my_song.play()
        status = command
    if PAUSE in command and status not in command:
        my_song.pause()
        status = command
    if CLOSE in command and status not in command: 
        sys.exit()



