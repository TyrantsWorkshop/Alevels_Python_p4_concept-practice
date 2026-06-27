##create a text file named "StudentRecord.txt"
## input student id, class and marks until id 0000 is entered. each record is written to the file.
## read the file and calculate the average marks of all students.
## count and output how many students have marks greater than 80.

FileObj = open("StudentRecord.txt", "w")
StudentId = input("enter id:")
while StudentId != "0000":
    Class = input("enter class")
    marks = input("enter marks")
    FileObj.write(StudentId + ""+Class +""+ marks)
    FileObj.write("\n")
    StudentId = input("enter id:")
FileObj.close()

#SearchId = input("enter a student id to be searched")
#FileObj = open("StudentRecord.txt", "r")
#Found = False
#FileStr = FileObj.readline()
#while len(FileStr) > 0:
    #if FileStr[0:4] == SearchId:
        #print(FileStr)
        #Found = True
    #Filestr = FileObj.readline()
#if not Found:
    #print("record not found")
#FileObj.close()


FileObj = open("StudentRecord.txt", "r")
counter = 0
StudentCount = 0
total = 0
FileStr = FileObj.readline()
while len(FileStr)> 0:
    marks = int(FileStr[6:])
    if marks > 80:
        counter = counter + 1
    total = total + marks
    StudentCount = StudentCount + 1
    FileStr = FileObj.readline()
FileObj.close()
print("average=", total/StudentCount)
print(counter)




