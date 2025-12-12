import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)

    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    output = []
    
    entries = os.listdir(full_path)
    for name in entries:
        entry_path = os.path.join(full_path, name)
        entry_size = os.path.getsize(entry_path)
        entry_is_dir = os.path.isdir(entry_path)
        line = f'- {name}: file_size={entry_size} bytes, is_dir={entry_is_dir}'
        output.append(line)
    return '\n'.join(output)

