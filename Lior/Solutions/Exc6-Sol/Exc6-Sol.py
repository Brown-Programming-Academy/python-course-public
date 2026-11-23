ROOT_DIRECTORY = "root"
CREATE_FILE = 1
CREATE_DIR = 2
OPEN_OBJECT = 3
DELETE_OBJECT = 4
PRINT_TREE = 5
FIND_OBJECT = 6
SHOW_STATS = 7
RETURN_CODE = 0

def get_weight(entity):
    if isinstance(entity, str):
        return len(entity)
    else:
        weight = 0

        for content in entity.values():
            weight += get_weight(content)

        return weight

def print_content(directory):
    print(30 * '-')
    for name, content in directory.items():
        weight = get_weight(content)
        print(f"{name} - weight: {weight}", end="")

        if (isinstance(content, dict)):
            print(f"; Items: {len(content)}", end="")

        print()

    print(30 * '-')

def choose_action():
    op_code = None

    while True:
        op_code = int(input("""
    Please choose action:
    1) Create new file
    2) Create new directory
    3) Open entity
    4) Delete entity
    5) Print tree
    6) Find entity
    7) Show stats
    0) Back to parent  (or exit)
    """))
        if (not RETURN_CODE <= op_code <= SHOW_STATS):
            print("Wrong input, please try again")
        else:
            return op_code

def create_new_file(directory):
    while True:
        name = input("Insert file name: ")

        if name.strip() == "":
            print("Name may not be empty")
        elif name in directory:
            print("Name already exist in this directory")
        else:
            content = input("Insert file content:\n")
            directory[name] = content
            return

def create_new_dir(directory):
    while True:
        name = input("Insert directory name: ")

        if name.strip() == "":
            print("Name may not be empty")
        elif name in directory:
            print("Name already exist in this directory")
        else:
            directory[name] = {}
            return
        
def open_obj(path, directory):
    name = input("Choose object to open: ")

    if name in directory:
        if isinstance(directory[name], str):
            print(directory[name])
        else:
            enter_directory(f"{path}/{name}", directory[name])

# ---------- Extensions ----------

def print_tree(directory, indent=0):
    for name, content in directory.items():
        if isinstance(content, dict):
            print(f"{'    ' * indent}{name}/")
            print_tree(content, indent + 1)
        else:
            print(f"{'    ' * indent}{name}")

def find(directory, name, path=""):
    for item_name, content in directory.items():
        item_path = f"{path}/{item_name}"

        if item_name == name:
            return item_path

        if isinstance(content, dict):
            result = find(content, name, item_path)

            if result is not None:
                return result

    return None

def count_files(directory):
    count = 0

    for content in directory.values():
        if isinstance(content, str):
            count += 1
        else:
            count += count_files(content)

    return count

def max_depth(directory):
    deepest = 0

    for content in directory.values():
        if isinstance(content, dict):
            deepest = max(deepest, max_depth(content))

    return deepest + 1

def delete_obj(directory):
    name = input("Choose object to delete: ")

    if name in directory:
        del directory[name]
        print(f"'{name}' deleted")
    else:
        print(f"'{name}' does not exist")

def find_obj(path, directory):
    name = input("Choose object to find: ")
    result = find(directory, name, path)

    if result is None:
        print(f"'{name}' not found")
    else:
        print(f"Found: {result}")

def show_stats(directory):
    print(f"Files: {count_files(directory)}")
    print(f"Max depth: {max_depth(directory)}")

# ---------- Main loop ----------

def enter_directory(path, directory):
    while True:
        print(f"\n{30 * '='}\n")
        print(f"You are here: {path}")
        print_content(directory)
        op_code = choose_action()

        if op_code == CREATE_FILE: create_new_file(directory)
        elif op_code == CREATE_DIR: create_new_dir(directory)
        elif op_code == OPEN_OBJECT: open_obj(path, directory)
        elif op_code == DELETE_OBJECT: delete_obj(directory)
        elif op_code == PRINT_TREE: print_tree(directory)
        elif op_code == FIND_OBJECT: find_obj(path, directory)
        elif op_code == SHOW_STATS: show_stats(directory)
        elif op_code == RETURN_CODE: return

# main
enter_directory(ROOT_DIRECTORY, {})