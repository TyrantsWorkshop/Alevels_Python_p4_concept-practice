## implement bubble sort and selection sort using functions.
## input 5 marks and sort them in ascending order using bubble sort.
## sort a list of names alphabetically using bubble sort.
## sort a list of prices in ascending and descending order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort(nums.copy())
print("bubble sort:", sorted_nums)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr

data = [29, 10, 14, 37, 13]
sorted_data = selection_sort(data.copy())
print("selection sort:", sorted_data)

marks = []
for i in range(5):
    marks.append(int(input("enter mark: ")))

for i in range(len(marks) - 1):
    for j in range(len(marks) - i - 1):
        if marks[j] > marks[j + 1]:
            temp = marks[j]
            marks[j] = marks[j + 1]
            marks[j + 1] = temp
print("sorted marks:", marks)

names = ["Charlie", "Alice", "Bob", "Diana"]
for i in range(len(names) - 1):
    for j in range(len(names) - i - 1):
        if names[j] > names[j + 1]:
            temp = names[j]
            names[j] = names[j + 1]
            names[j + 1] = temp
print("sorted names:", names)

prices = [500, 1200, 800, 300, 950]
prices.sort()
print("ascending:", prices)
prices.sort(reverse=True)
print("descending:", prices)
