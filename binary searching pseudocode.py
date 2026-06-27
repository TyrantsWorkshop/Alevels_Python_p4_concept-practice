# let list is an array of N elements.input a particular item.search the item using binary search technique.
# implement binary search using iteration and recursion.
# find the first occurrence of a duplicate value in a sorted list.
# input an item from the user and search for it in a sorted list.
# search for a name in a sorted list of names.

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1

my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
item_to_find = 23
result_index = binary_search(my_list, item_to_find)

if result_index != -1:
    print(f"Item {item_to_find} found at index {result_index}.")
else:
    print(f"Item {item_to_find} not found in the list.")

def binary_search_recursive(arr, item, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == item:
        return mid
    if arr[mid] > item:
        return binary_search_recursive(arr, item, low, mid - 1)
    return binary_search_recursive(arr, item, mid + 1, high)

scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
search_score = 70
result = binary_search_recursive(scores, search_score, 0, len(scores) - 1)
if result != -1:
    print("Score found at index:", result)
else:
    print("Score not found")

prices = [100, 250, 400, 400, 400, 500, 750]
target_price = 400
low = 0
high = len(prices) - 1
first_index = -1
while low <= high:
    mid = (low + high) // 2
    if prices[mid] == target_price:
        first_index = mid
        high = mid - 1
    elif prices[mid] > target_price:
        high = mid - 1
    else:
        low = mid + 1
print("First occurrence at index:", first_index)

sorted_ids = [11, 22, 33, 44, 55, 66, 77, 88, 99]
user_item = int(input("Enter item to search: "))
index_found = binary_search(sorted_ids, user_item)
if index_found != -1:
    print("Found at index:", index_found)
else:
    print("Item not in list")

letters = ["a", "c", "e", "g", "i", "k", "m", "o"]
missing = binary_search(letters, "z")
if missing == -1:
    print("Letter z not found")

names_sorted = ["Anna", "Ben", "Carl", "Dana", "Evan", "Faye"]
search_name = input("Enter name: ")
name_low = 0
name_high = len(names_sorted) - 1
name_found = False
while name_low <= name_high and name_found == False:
    name_mid = (name_low + name_high) // 2
    if names_sorted[name_mid] == search_name:
        name_found = True
        print("Name found at index:", name_mid)
    elif names_sorted[name_mid] > search_name:
        name_high = name_mid - 1
    else:
        name_low = name_mid + 1
if name_found == False:
    print("Name not found")
