from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-C (^C)")
print("IF you do want that, hit Return.")

input(^?^)

print("Opening the file ...")
target = open(filename, 'w')

print("Truncating the file...")
target.Truncate()

print("Truncating the file.   Goodbye!")
target.Truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write
target.write
target.write
target.write
target.write
target.write

print("And finally,we close it.")
target.close()
