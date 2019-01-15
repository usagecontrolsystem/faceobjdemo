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
import RPi.GPIO as GPIO
import time
import socket 
import sys
import argparse

#server socket

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(7, GPIO.IN)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 7890))
while True : 
	data,address = sock.recvfrom(128)
	print(data)
	value = GPIO.input(4)
	print("SENDING " + str(value))
	sock.sendto(str(value) +  '\n', address)	    	
