# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
import sys
from socket import *

# Get the server hostname and port as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
timeout = 1
 
# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times

while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description
    current_time = time.asctime()  # String in format: 'Sun Jun 20 23:21:05 1993'
    d = "Ping " + str(ptime) + " " + current_time
    data = d.encode()

    try:
        # Record the "sent time"
        sent_time = time.time()

        # Send the UDP packet with the ping message
        print("Sending message: ", d)
        clientSocket.sendto(data, (host, port))

        # Receive the server response
        recv_message, server_adress = clientSocket.recvfrom(2048)

        # Record the "received time"
        time.sleep(0.000001)  # Delay to avoid rtt = 0.0
        recv_time = time.time()

        # Display the server response as an output
        print("Response message: ", recv_message.decode())

        # Round trip time is the difference between sent and received time
        rtt = recv_time - sent_time
        print("Round Trip Time: ", str(rtt))
        print("\n")

    except:
        # Server does not response
	    # Assume the packet is lost
        print("Request timed out.")
        print("\n")
        continue

# Close the client socket
clientSocket.close()
 
