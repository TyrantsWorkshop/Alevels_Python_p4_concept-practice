## create a dictionary to store student details. access values, add a new key and loop through all key-value pairs.
## calculate the average mark from a dictionary of subject marks.
## input a product code and search for its stock in an inventory dictionary.
## add and delete items from a dictionary.
## create a phone book by inputting names and numbers, then search for a name.
## count how many times each word appears in a list using a dictionary.

student = {"name": "Ali", "age": 16, "grade": "A"}
print(student["name"])
print(student.get("age"))

student["school"] = "Central High"
print(student)

for key in student:
    print(key, ":", student[key])

marks = {"math": 85, "science": 92, "english": 78}
total = 0
count = 0
for subject in marks:
    total = total + marks[subject]
    count = count + 1
average = total / count
print("average:", average)

inventory = {"P101": 50, "P102": 30, "P103": 75}
search_code = input("enter product code: ")
if search_code in inventory:
    print("stock:", inventory[search_code])
else:
    print("product not found")

inventory["P104"] = 20
del inventory["P102"]
print(inventory)

phone_book = {}
for i in range(3):
    name = input("enter name: ")
    number = input("enter number: ")
    phone_book[name] = number

lookup = input("search name: ")
if lookup in phone_book:
    print("number:", phone_book[lookup])
else:
    print("not found")

word_count = {}
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
print(word_count)
