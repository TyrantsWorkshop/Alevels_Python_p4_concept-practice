## write a program to input a string . validate the string and output a validation message .validate the string using criterias:
##  1-lenght should be more than 8
##  2-it should contain at least two upper case letters,2 digits and 1 lowercase letter
## input a word and output its reverse.
## count and output the number of vowels and consonants in a text.
## replace all spaces in a sentence with underscore characters.
## check whether an input word is a palindrome.
## validate an email address contains exactly one @ symbol not at the start or end.
## check whether a password is strong: at least 6 characters with one digit and one special symbol.


string = input('enter string')
v = False
if len(string)>8:
    v = True
uppercount = 0
lowercount = 0
digitcount = 0

for i in range(len(string)):
    ch = string[i]
    if ch.isupper()== True:
        uppercount = uppercount + 1
    elif ch.islower()==True:
        lowercount = lowercount + 1
    elif ch.isdigit()==True:
        digitcount = digitcount + 1

if v == True and uppercount >= 2 and digitcount >=2 and lowercount >= 1:
    print("string is valid")
else:
    print("string is invalid")

word = input("enter a word")
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word = reversed_word + word[i]
print("reversed:", reversed_word)

text = input("enter text")
vowelcount = 0
consonantcount = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowelcount = vowelcount + 1
    elif ch.isalpha():
        consonantcount = consonantcount + 1
print("vowels:", vowelcount)
print("consonants:", consonantcount)

sentence = input("enter sentence")
new_sentence = ""
for ch in sentence:
    if ch == " ":
        new_sentence = new_sentence + "_"
    else:
        new_sentence = new_sentence + ch
print(new_sentence)

check = input("enter word to check palindrome")
is_palindrome = True
left = 0
right = len(check) - 1
while left < right:
    if check[left] != check[right]:
        is_palindrome = False
        break
    left = left + 1
    right = right - 1
if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")

email = input("enter email")
at_count = 0
for ch in email:
    if ch == "@":
        at_count = at_count + 1
if at_count == 1 and email.find("@") > 0 and email.find("@") < len(email) - 1:
    print("valid email format")
else:
    print("invalid email format")

password = input("enter password")
has_digit = False
has_special = False
for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch in "!@#$%^&*":
        has_special = True
if len(password) >= 6 and has_digit and has_special:
    print("strong password")
else:
    print("weak password")
