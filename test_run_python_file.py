from functions.run_python_file import run_python_file

print("Result for main.py:")
print(run_python_file("calculator", "main.py"))
print()

print("Result for calculator")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print()

print("Result for tests.py")
print(run_python_file("calculator", "tests.py"))
print()

print("Result for ../main.py")
print(run_python_file("calculator", "../main.py"))
print()

print("Result for nonexistent.py")
print(run_python_file("calculator", "nonexistent.py"))
print()

print("Result for lorem.txt")
print(run_python_file("calculator", "lorem.txt"))
print()