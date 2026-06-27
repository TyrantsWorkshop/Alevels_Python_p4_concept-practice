## write a program to store product information for 5 products in a 2D list. each row contains product code, price and stock quantity.
## display product id and stock. input a product code and quantity, calculate bill amount and update stock.
## output product codes where price is greater than 500 and stock is less than 50.
## copy product code, price and stock into three separate lists.
## calculate total price of all products.
## find and output the product with maximum stock.
## input a stock threshold and output all products below that threshold.
## for a 3x3 matrix, calculate and output the sum of each row and each column.
## input marks for 4 students with 3 subjects each, calculate and output each student's average.

prodInfo = [[0 for C in range(3)]for r in range (5)]
for r in range (5):
    prodInfo[r][0] = input("enter code")
    prodInfo[r][1] = int(input ("enter price"))
    prodInfo[r][2] = int(input ("enter stock quantity"))

print ("prodId    stock")
for r in range(5):
    print(prodInfo[r][0],"    ",prodInfo[r][2])

product = input("enter the product to buy")
quantity = int(input("enter the quantity to buy"))
for r in range (5):
    if product == prodInfo[r][0] :
        billAmount = prodInfo[r][1] * quantity
        print ("bill amount=", billAmount)
        prodInfo[r][2] = prodInfo[r][2] - quantity
        break

for r in range (5):
    if prodInfo[r][1] > 500 and prodInfo[r][2] < 50:
        print(prodInfo[r][0])

ProCode = []
price = []
sQuantity = []

for r in range(5):
    ProCode.append(prodInfo[r][0])
    price.append(prodInfo[r][1])
    sQuantity.append(prodInfo[r][2])

total_price = 0
for r in range(5):
    total_price = total_price + prodInfo[r][1]
print("total price of all products:", total_price)

max_stock = prodInfo[0][2]
max_index = 0
for r in range(1, 5):
    if prodInfo[r][2] > max_stock:
        max_stock = prodInfo[r][2]
        max_index = r
print("product with max stock:", prodInfo[max_index][0])

threshold = int(input("enter stock threshold: "))
print("products below threshold:")
for r in range(5):
    if prodInfo[r][2] < threshold:
        print(prodInfo[r][0], prodInfo[r][2])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sum = []
for r in range(3):
    total = 0
    for c in range(3):
        total = total + matrix[r][c]
    row_sum.append(total)
print("row sums:", row_sum)

col_sum = []
for c in range(3):
    total = 0
    for r in range(3):
        total = total + matrix[r][c]
    col_sum.append(total)
print("column sums:", col_sum)

student_marks = [[0 for c in range(3)] for r in range(4)]
for r in range(4):
    for c in range(3):
        student_marks[r][c] = int(input("enter mark: "))

for r in range(4):
    average = 0
    for c in range(3):
        average = average + student_marks[r][c]
    average = average / 3
    print("student", r + 1, "average:", average)
