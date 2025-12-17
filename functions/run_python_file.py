import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    commands = ['python', file_path]
    commands.extend(args)
    
    completed_process = subprocess.run(commands, cwd=working_directory,  capture_output=True, timeout=30, text=True)

    output_strings = []
    
    if completed_process.stdout:
        output_strings.append(f'STDOUT:{completed_process.stdout}')
    if completed_process.stderr:
        output_strings.append(f'STDERR:{completed_process.stderr}')
    if completed_process.returncode != 0:
        output_strings.append(f'Process exited with code {completed_process.returncode}')
    if output_strings == []:
        return "No output produced"
    
    output = "\n".join(output_strings)

    return output
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description= "Runs a python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to run a python file from, relative to the working directory.",
            ),
        },
    ),
)