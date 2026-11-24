ROOT_FOLDER = "root"
CREATE_FILE = 1
CREATE_DIR = 2
OPEN = 3
BACK = 0

def get_weight(content): pass
    

def show_content(folder : dict):
    for name, content in folder.items():
        weight = get_weight(content)
        print(f"{name} - {weight}", end="")

        if isinstance(content, dict):
            print(f"; Items: {len(content)}", end="")

        print()

def get_opcode(): pass
def create_new_file(folder): pass
def create_new_dir(folder): pass
def open_obj(path, folder): pass

def enter_directory(path, folder):
    while True:
        print(f"\n{10 * "🐶"}\nYou are here: {path}\n{10 * "🐶"}\n")
        show_content(folder)
        op_code = get_opcode()

        if op_code == CREATE_FILE: create_new_file(folder)
        elif op_code == CREATE_DIR: create_new_dir(folder)
        elif op_code == OPEN: open_obj(path, folder)
        elif op_code == BACK: return

# Main
enter_directory(ROOT_FOLDER, {})