import os,re,importlib.util,pyperclip


def list_files(directory):
    # 获取目录下所有文件和子目录名
    return os.listdir(directory)

def load_module(module_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.data

