def read_file(file_name):
    try:
        with open('./files' + file_name, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('文件未找到')

def start():
    pass

if __name__ == '__main__':
    start()
