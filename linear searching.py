##writee a program for the following
##   inout and create a list of ten names
##   input a particular name ,search the name in the list. if found ouput the position,otherwise output error message
## search for a number in a list and output its index if found.
## input 5 marks, search for a mark and output all positions where it appears.
## count how many times a student name appears in a list.
## find the maximum value in a list and output the value and its index.
## search for a roll number in a list and output its position if found.


namelist = []
for i in range(10):
    namelist.append(input("Enter name: "))

searchname = input("Enter a name to be searched: ")
found = False
index = 0

while index < 10 and found == False:
    if namelist[index] == searchname:
        found = True
        print("The name found in the position:", index + 1)
    index = index + 1

if found == False:
    print("The name does not exist in the list.")

numbers = [45, 12, 78, 34, 90, 23, 56, 11, 67, 88]
search_num = int(input("Enter number to search: "))
found_num = False
pos = 0
while pos < len(numbers) and found_num == False:
    if numbers[pos] == search_num:
        found_num = True
        print("Number found at index:", pos)
    pos = pos + 1
if found_num == False:
    print("Number not found")

marks = []
for i in range(5):
    marks.append(int(input("Enter mark: ")))
target = int(input("Enter mark to find all positions: "))
positions = []
for i in range(len(marks)):
    if marks[i] == target:
        positions.append(i + 1)
if len(positions) > 0:
    print("Found at positions:", positions)
else:
    print("Mark not found")

students = ["Ali", "Sara", "John", "Sara", "Mike"]
lookup = input("Enter student name: ")
count = 0
for name in students:
    if name == lookup:
        count = count + 1
print("Occurrences:", count)

data = [10, 25, 3, 47, 19, 8]
maximum = data[0]
max_index = 0
for i in range(1, len(data)):
    if data[i] > maximum:
        maximum = data[i]
        max_index = i
print("Maximum value:", maximum)
print("At index:", max_index)

roll_numbers = [101, 205, 310, 415, 520]
search_roll = int(input("Enter roll number: "))
found_roll = False
for i in range(len(roll_numbers)):
    if roll_numbers[i] == search_roll:
        found_roll = True
        print("Roll number found at position:", i + 1)
        break
if found_roll == False:
    print("Roll number not in list")
