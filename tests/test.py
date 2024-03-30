import subprocess
import os

# 替换此路径为您的文件夹路径
folder_path = "F:\\book\\Englishbook\\epub"

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 过滤出 EPUB 文件
epub_files = [os.path.join(folder_path, file) for file in files if file.endswith(".epub")]

# 创建一个列表来存储符合条件的 EPUB 地址（不包含'bilingual'）
epub_addresses = [file for file in epub_files if 'bilingual' not in file]


# 打印 EPUB 地址列表
print(epub_addresses)
# 替换 ${openai_key} 为您的 OpenAI 密钥

for epub in epub_addresses:

    # 创建命令
    command = ["python", 
            "F:\PythonCode\\bilingual_book_maker-main\\bilingual_book_maker-main\\make_book.py", 
            "--book_name", 
            epub,
            "--model","google"]

    # 执行命令
    # subprocess.run(command)

