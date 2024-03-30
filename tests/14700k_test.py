import os

# 替换此路径为您的文件夹路径
folder_path = "F:\\book\\Englishbook\\epub"

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 过滤出 EPUB 文件
epub_files = [file for file in files if file.endswith(".epub")]

# 创建一个列表来存储 EPUB 地址
epub_addresses = []

# 临时存储已检测到的双语版文件名，以便排除
bilingual_detected = set()

# 将 EPUB 地址添加到列表中
for file in epub_files:
    # 检查是否为双语版或已经检测到对应的双语版
    base_name = file[:-5]  # 移除".epub"获取基础文件名
    if base_name + "_bilingual.epub" in epub_files or base_name in bilingual_detected:
        # 如果当前文件是双语版或已经找到对应的双语版，则跳过
        continue
    # 检查对应的双语版文件是否存在
    if base_name + ".epub" in epub_files and base_name + "_bilingual.epub" in epub_files:
        bilingual_detected.add(base_name)  # 添加到已检测集合，防止重复添加
        continue  # 存在对应的双语版本时，跳过添加
    epub_address = os.path.join(folder_path, file)
    epub_addresses.append(epub_address)

# 打印结果或进行后续处理
for address in epub_addresses:
    print(address)