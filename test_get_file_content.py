from functions.get_file_content import get_file_content

print("Result for lorem.txt")
print(get_file_content("calculator", "lorem.txt"))

print("Result for current file:")
print(get_file_content("calculator", "main.py"))
print()

print("Result for calulator file:")
print(get_file_content("calculator", "pkg/calculator.py"))
print()

print("Result for '/bin/cat' file:")
print(get_file_content("calculator", "/bin/cat"))
print()

print("Result for 'pkg/does_not_exist.py' file")
print(get_file_content("calculator", "pkg/does_not_exist.py"))