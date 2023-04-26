import socket

HOST = '192.168.1.14'
PORT = 9587

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket object to the specified IP address and port
s.bind((HOST, PORT))

# listen for incoming connections
s.listen()

# print a message indicating that the socket is listening on the specified port
print(f"listening on port {PORT}...")

# loop forever, accepting incoming connections and receiving files
while True:
    # accept a connection from a client
    conn, addr = s.accept()

    # print a message indicating that a connection has been received
    print(f"[+] received a connection from -> {addr}")

    # receive information about the file to be received
    file_info = conn.recv(1048576).decode().replace("\r\n", "|").replace("\n", "|").strip().split("|")
    print(file_info)
    print(file_info[0], int(file_info[1]))

    # extract the file name and size from the received information
    file_name, file_size = file_info[0], int(file_info[1])

    # print a message indicating the received file name and size
    print(f"Received file {file_name} ({file_size} bytes)")

    # open a file with the received name for writing in binary mode
    with open(file_name, "wb") as f:
        remaining_size = file_size
        # loop until the entire file has been received
        while remaining_size > 0:
            # receive a chunk of data from the client, up to a maximum of 1MB at a time
            data_size = min(1048576, remaining_size)
            data = conn.recv(data_size)
            print(data)
            # write the received data to the file
            f.write(data)
            # decrement the remaining file size by the amount of data received
            remaining_size -= len(data)
            # print the remaining file size after each chunk of data is received
            print(remaining_size)

    # print a message indicating that the file has been saved successfully
    print("File saved successfully")
