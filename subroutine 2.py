##write program to create a functtion which will extract a substring from a given string. the function will have threee parameters
##  1-a string
##  2-starting index
##  3-number of characters to be extracetd from the starting  index
##the function will return the extracted substring to the main program. you need to use only iteration to extract the characters.

def extract (string,startpos,NC):
    newStr = ""
    for i in range(startpos-1,startpos-1+NC):
        newStr = newStr + string[i]

    return(newStr)

str1 = input("enter a string")
start = int(input("enter starting index"))
NC = int(input("enter number of characters"))
substr = extract(str1,start,NC)
print("the new substring is :",substr)
            
