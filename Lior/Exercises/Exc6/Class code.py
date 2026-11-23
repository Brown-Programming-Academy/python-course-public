ROOT_DIR = "root"
CREATE_FILE = 1
CREATE_DIR = 2
OPEN_OBJECT = 3
BACK = 0

def get_weight(obj):
    if isinstance(obj, str):
        return len(obj)
    else:
        weight = 0

        for content in obj.values():
            weight += get_weight(content)
        
        return weight

def show_content(directory : dict):
    for name, content in directory.items():
        weight = get_weight(content)
        print(f"{name} - Weight: {weight}", end="")

        if isinstance(content, dict):
            print(f"; Items: {len(content)}", end="")

        print()

def choose_op():
    while True:
        op_code = int(input(f"""
Pleae choose action:
{CREATE_FILE}: Create new file
{CREATE_DIR}: Create new directory
{OPEN_OBJECT}: Open file/directory
{BACK}: Back to previous directory (or exit):
"""))

        if BACK <= op_code <= OPEN_OBJECT:
            return op_code

        print("Wrong input")

def create_new_file(directory):
    while True:
        name = input("Please insert file name: ")

        if name.strip == "":
            print("Name cant be empty")
        elif name in directory:
            print(f"{name} already exist in directory")
        else:
            content = input("Insert content: ")
            directory[name] = content
            return

def create_new_dir(directory):
    while True:
        name = input("Please insert directory name: ")

        if name.strip == "":
            print("Name cant be empty")
        elif name in directory:
            print(f"{name} already exist in directory")
        else:
            directory[name] = {}
            return
            
def open_obj(path, directory):
    name = input("Insert object name: ")

    if name not in directory:
        print(f"404")
    else:   
        if isinstance(directory[name], str):
            print(directory[name])
        else:
            enter_directory(f"{path}/{name}" ,directory[name])

def enter_directory(path, directory):
    while True:
        print(f"{30 * "#"}\nYou are here: {path}\n{30 * "#"}")
        
        show_content(directory)

        op_code = choose_op()

        if op_code == CREATE_FILE: create_new_file(directory)
        elif op_code == CREATE_DIR: create_new_dir(directory)
        elif op_code == OPEN_OBJECT: open_obj(path, directory)
        elif op_code == BACK: return

#### Main loop #####
enter_directory(ROOT_DIR, {})