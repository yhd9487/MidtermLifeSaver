import os
import hashlib

folder = '\\'
for dirpath, dirnames, filenames in os.walk(folder):
    # 遍历文件夹中的文件
    for filename in filenames:
        # 处理每个文件
        file_path = os.path.join(dirpath, filename)
        # ...
with open(file_path, 'rb') as f:
    file_hash = hashlib.sha1(f.read()).hexdigest()
hash_dict = {}
for dirpath, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha1(f.read()).hexdigest()
            if file_hash in hash_dict:
                print('重复文件：', file_path)
                print('与', hash_dict[file_hash], '重复')
            else:
                hash_dict[file_hash] = file_path

