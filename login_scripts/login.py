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
from threading import Thread
import subprocess
import sys

def wait_for_terminate(socket, username) :
    while True: 
        data, server = socket.recvfrom(1024)
        command = str(data)
        if "TERMINATE" in command: 
            subprocess.run(["pkill", "-u", username])

def get_args(): 
    parser = argparse.ArgumentParser(description="run the script using the passed username")
    parser.add_argument("--user", type=str, default=None, help="user to be controlled")
    args = parser.parse_args()
    return args

PLAY = "PERMIT"
PAUSE = "DENY"
CLOSE = "TERMINATE"

args = get_args()
username = args.user

print(username)

client_socket = socket(AF_INET, SOCK_DGRAM)
addr = ("127.0.0.1", 12345)
client_socket.sendto("start".encode(), addr)

command = ""
data, server = client_socket.recvfrom(1024)
command = str(data)    
if PLAY in command :
    print("PLAY")
    thread = Thread(target = wait_for_terminate, args=(client_socket, username))
    thread.start()
if "TERMINATE" in command: 
    #put your username here
    subprocess.run(["pkill", "-u", username])
print("THE END")
