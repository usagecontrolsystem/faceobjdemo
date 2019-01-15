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

# coding: utf-8

# In[9]:


import socket
import sys
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


# In[10]:


def restore_attribute_manager():
	try:
		attribute_manager_path = "../attribute_manager/identities_detected.txt"
		with open(attribute_manager_path, "w") as f:
			f.write("0")
		f.close()
		print("Attribute manager file resetted\n")
	except:
		print("Error in reading the attribute manager file\n")


# In[11]:


def run_server(port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = get_ip()
 
    # Bind the socket to the port
    #server_address = ('146.48.99.81', 8890)
    print(ip)
    server_address = (ip, port)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)


    attribute_manager_path = "../attribute_manager/identities_detected.txt"

    while True:
        print('\nwaiting to receive message')
        data_rcv, address = sock.recvfrom(4096)

        print('received %s bytes from %s' % (len(data_rcv), address))
        print(data_rcv.lower().strip())	
        with open(attribute_manager_path) as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            print(lines)
            if data_rcv.lower().strip() in lines:
                data = "1"
            else:
                data = "0"
       print("data sent " + data)
       if data:
            sent = sock.sendto(data.encode(), address)
            print('sent %s bytes back to %s' % (sent, address))


# In[12]:


import sys
port = sys.argv[1]
restore_attribute_manager()
run_server(int(str(port)))

