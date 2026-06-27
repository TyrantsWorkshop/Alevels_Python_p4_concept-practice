# 1) create a textfile to input member name and their email address. both the information will be separated by # character.
# here member name and email address are variable lenght string for 5 members. the file name is contactdetails.txt
## 2)read the file amd copy all the email addresses of the members in a new file named newcontactdetails.txt. you must implement exception handling code in the program to
## handle runtime errors when occurs if any.


FileObj = open("contactdetails.txt", "w")

count = 0
for count in range(5):
    memberName = input("enter name")
    memberEmail = input("enter email")
    FileObj.write(memberName + "#"+memberEmail)
    FileObj.write("\n")
    count = count + 1
FileObj.close()


try:
    FileObj1 = open("contactdetails.txt", "r")
    FileObj2 = open("newcontactdetails.txt", "w")
    FileStr = FileObj1.readline()
    while len(FileStr)>0:
        for i in range (len(FileStr)-1):
            if FileStr[i] == '#':
                position = i    
                email = FileStr[Position+1 : ]
                FileObj2.write(email)
                FileObj2.write("\n")
        FileStr = FileObj1.readline()
        FileObj1.close()    
        FileObj2.close()
except:
    print("file not found")

            
        
        

