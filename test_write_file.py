from functions.write_file import write_file

print("Result for current directory:")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print()

print("Result for 'pkg' directory:")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print()

print("Result for '/tmp/temp.txt' file write:")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print()