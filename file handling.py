## create a text file named sample.txt, write lines to it, read and display the full content.
## read the file line by line and output each line without extra whitespace.
## write numbers 10, 20, 30, 40 and 50 to numbers.txt and calculate the sum when reading the file.
## write a list of student names to students.txt and read them back into a list.

file = open("sample.txt", "w")
file.write("Hello World\n")
file.write("Python Practice\n")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

file = open("sample.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

file = open("numbers.txt", "w")
for i in range(1, 6):
    file.write(str(i * 10) + "\n")
file.close()

file = open("numbers.txt", "r")
total = 0
for line in file:
    total = total + int(line.strip())
print("sum:", total)
file.close()

file = open("students.txt", "w")
students = ["Ali", "Sara", "John"]
for name in students:
    file.write(name + "\n")
file.close()

file = open("students.txt", "r")
names = []
for line in file:
    names.append(line.strip())
print("names:", names)
file.close()
