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

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 1967)
message = 'Giacomo Giorgi ismkddasfdasfsafsa'

try:

    # Send data
    print(sys.stderr, 'sending "%s"' % message)
    sent = sock.sendto(message.encode(), server_address)

    # Receive response
    print(sys.stderr, 'waiting to receive')
    data, server = sock.recvfrom(4096)
    print(sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
