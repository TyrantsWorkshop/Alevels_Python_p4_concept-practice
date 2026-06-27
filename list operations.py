## practice list operations using the following tasks:
## append and insert items, sort and reverse a list, pop an item, count occurrences and find index,
## extend a list, copy a list, filter scores above 60, remove an item and build a list of squares.

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "blueberry")
print(fruits)

numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print("sorted:", numbers)

numbers.reverse()
print("reversed:", numbers)

values = [10, 20, 30, 40, 50]
removed = values.pop(2)
print("removed:", removed)
print("list:", values)

items = ["pen", "book", "pen", "bag", "pen"]
count_pen = items.count("pen")
print("pen count:", count_pen)

index_book = items.index("book")
print("book at index:", index_book)

mixed = [1, 2, 3]
mixed.extend([4, 5, 6])
print(mixed)

copy_list = values.copy()
copy_list[0] = 99
print("original:", values)
print("copy:", copy_list)

scores = [45, 78, 92, 56, 88, 34]
above_60 = []
for s in scores:
    if s >= 60:
        above_60.append(s)
print("passed:", above_60)

names = ["Tom", "Amy", "Sam", "Leo"]
names.remove("Amy")
print(names)

empty = []
for i in range(5):
    empty.append(i * i)
print(empty)
