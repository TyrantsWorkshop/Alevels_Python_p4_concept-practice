##    assume that there are three different lists used to store 5 products information.the lists are given below:
##    ProdCode=["P1010","P1020","P1030","P1040","P1050"]
##    price=[8000,2500,1800,5000,7000]
##    DiscountPercent=[5,2,8,5,10]
##    write a program to input a product code and quantity.calculate and output the discount amount and the bill amount.
## calculate and output price with 12% tax for each product.
## find and output the cheapest product.
## calculate total revenue using given sold quantities and discounts.
## input multiple product orders and calculate the grand total bill.
## display a table of product code, price and discount percent.


ProdCode=["P1010","P1020","P1030","P1040","P1050"]
price=[8000,2500,1800,5000,7000]
DiscountPercent=[5,2,8,5,10]

quantity = int(input("enter quantity"))
searchProduct = input("enter product code")
found = False
index = 0
for index in range(5):
    if ProdCode[index] == searchProduct:
        found = True
        total = price[index] * quantity
        discount = total*DiscountPercent[index]/100
        billAmount = total - discount
        break
    index = index + 1

if found:
    print("discount:",discount)
    print("bill:",billAmount)
else:
    print("product not found")

tax_rate = 12
for i in range(5):
    base = price[i]
    tax = base * tax_rate / 100
    final_price = base + tax
    print(ProdCode[i], "price with tax:", final_price)

cheapest_index = 0
for i in range(1, 5):
    if price[i] < price[cheapest_index]:
        cheapest_index = i
print("cheapest product:", ProdCode[cheapest_index])
print("price:", price[cheapest_index])

total_revenue = 0
sold_qty = [2, 5, 3, 1, 4]
for i in range(5):
    item_total = price[i] * sold_qty[i]
    item_discount = item_total * DiscountPercent[i] / 100
    total_revenue = total_revenue + (item_total - item_discount)
print("total revenue:", total_revenue)

order_count = int(input("how many products to buy: "))
grand_total = 0
for o in range(order_count):
    code = input("enter product code: ")
    qty = int(input("enter quantity: "))
    for i in range(5):
        if ProdCode[i] == code:
            subtotal = price[i] * qty
            disc = subtotal * DiscountPercent[i] / 100
            grand_total = grand_total + (subtotal - disc)
            break
print("grand total:", grand_total)

print("Product    Price    Discount%")
for i in range(5):
    print(ProdCode[i], "   ", price[i], "      ", DiscountPercent[i])
