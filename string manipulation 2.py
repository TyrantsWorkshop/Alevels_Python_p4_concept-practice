## write a program to input a string . validate the string and output a validation message .validate the string using criterias:
##  1-lenght should not exceed 12 character
##  2-it should contain at single @ symbol
##  3-it should contain at least one uppercase letter and 1 digit
##  4-no other symbol should be present except @

string = input("enter string")
validate = False

if len(string) <= 12:
    validate = True

sym = 0
uppcase = 0
lcase = 0
digit = 0
other = 0

for i in range(len(string)):
    ch = string[i]
    if ch.isupper()== True:
        uppcase = uppcase + 1
    elif ch.isdigit()==True:
        digit = digit + 1
    elif ch == '@':
        sym = sym + 1
    elif ch.islower()==True:
        lcase = lcase + 1
    else:
        other = other + 1

if validate == True and sym >= 1 and uppcase >=1 and digit >= 1 and other == 0:
    print("string is valid")
else:
    print("string is invalid")
