# 导入需要的模块
import os  # 操作文件和文件夹的模块
import hashlib  # 计算哈希值的模块

# 指定文件夹路径
folder = r'C:\Users\YHD\Documents\PycharmProjects\MidtermLifeSaver'

# 遍历指定文件夹中的所有文件
for dirpath, dirnames, filenames in os.walk(folder):
    # 遍历当前文件夹中的所有文件
    for filename in filenames:
        # 拼接文件的完整路径
        file_path = os.path.join(dirpath, filename)
        # ...

# 打开每个文件，并计算文件的哈希值
with open(file_path, 'rb') as f:
    file_hash = hashlib.sha1(f.read()).hexdigest()

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
