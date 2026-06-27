## input a number between 0 and 100 inclusive. if the first input is valid output 1.
## otherwise keep asking until a valid number is entered and output the number of attempts taken.

attempt=1
num = input(int("enter number"))
if num>-1 and num<101:
    print(attempt)
else:
    num= input("enter number again")
    while num>-1 and num<101:
        attempt = attempt + 1
        num= input("enter number again")
    print(attempt)
    

    
     
    
