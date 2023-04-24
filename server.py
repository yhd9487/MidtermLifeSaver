import socket

HOST = '192.168.1.14'
PORT = 9587

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f"listening on port {PORT}...")

while True:
    conn, addr = s.accept()
    print(f"[+] received a connection from -> {addr}")

    while True:
        file_info = conn.recv(1048576).decode().replace("\r\n", "|").replace("\n", "|").strip().split("|")
        print(file_info)
        print(file_info[0], int(file_info[1]))
        file_name, file_size = file_info[0], int(file_info[1])
        print(f"Received file {file_name} ({file_size} bytes)")

        with open(file_name, "wb") as f:
            remaining_size = file_size
            while remaining_size > 0:
                data_size = min(1048576, remaining_size)
                data = conn.recv(data_size)
                print(data)
                f.write(data)
                remaining_size -= len(data)
                print(remaining_size)

        print("File saved successfully")
