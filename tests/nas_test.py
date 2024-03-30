import os
import subprocess

# 替换此路径为您的文件夹路径
folder_path = "G:\\book\\Englishbook\\epub"

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 过滤出 EPUB 文件
epub_files = [file for file in files if file.endswith(".epub")]

# 创建一个列表来存储 EPUB 地址
epub_addresses = []

# 初始化列表
untranslated = []  # 未翻译的列表
translated = []  # 已翻译的列表
other_epubs = []  # 其他 EPUB 文件列表

# 用于临时存储已检测到的双语版文件名
bilingual_detected = set()

for file in epub_files:
    base_name = file[:-5]  # 移除扩展名获取基础文件名
    full_path = os.path.join(folder_path, file)  # 将文件名转换为完整路径
    if "_bilingual" in file:
        # 对于双语版，检查是否存在其非双语版本
        if base_name.replace("_bilingual", "") + ".epub" in epub_files:
            translated.append(base_name.replace("_bilingual", "") + ".epub")
        else:
            # 如果没有对应的非双语版本，视为其他 EPUB 文件
            other_epubs.append(file)
    else:
        # 对于非双语版本，检查是否存在其双语版本
        if base_name + "_bilingual.epub" in epub_files:
            # 如果存在，已经在上面的逻辑中处理，这里不做操作
            continue
        else:
            # 如果不存在双语版本，视为未翻译
            untranslated.append(file)

# 确保所有已翻译的文件都不在未翻译列表中
untranslated = [file for file in untranslated if file not in translated]

# 构建除去已翻译和未翻译的 EPUB 文件列表
other_epubs = [file for file in epub_files if file not in untranslated and file not in translated]

for epub in translated:
    print("translated",epub)

for epub in untranslated:
    print("untrans",epub)

for epub in other_epubs:
    print("others",epub)

untranslated_paths = [folder_path + "\\" + file for file in untranslated]

for epub in untranslated_paths:

    # 创建命令
    command = ["python", 
            "E:\Code\\Python_code\\bilingual_book_maker-main\\make_book.py", 
            "--book_name", 
            epub,
            "--model","google"]

    # 执行命令
    subprocess.run(command)
