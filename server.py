import socket
import base64

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
        file_info = conn.recv(4096).decode().replace("\r\n", "|").replace("\n", "|").strip().split("|")
        if not file_info:
            break
        if len(file_info) < 2:
            continue  # 如果 file_info 列表中元素不足两个，说明格式不正确，跳过本次循环
        file_name, file_size = file_info[0], int(file_info[1])
        print(f"Received file {file_name} ({file_size} bytes)")

        with open(file_name, "wb") as f:
            remaining_size = file_size
            while remaining_size > 0:
                data_size = min(1024, remaining_size)
                data = conn.recv(data_size)
                f.write(data)
                remaining_size -= len(data)

        print("File saved successfully")

    conn.close()
    print("Connection closed")
