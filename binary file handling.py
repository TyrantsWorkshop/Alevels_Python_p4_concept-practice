##binary file handling
## write a program to input employee id and name, store the record in a binary file named employeeinfo.DAT using pickle,
## then read the file and display the stored employee id and name.

import pickle
class employee:
    def __init__(self,Id,name):
        self.Sid = Id
        self.Sname = name


Id = input("enter your id ")
name = input("enter your name")
emprecord = employee(Id,name)
file1 = open("employeeinfo.DAT","wb")
pickle.dump(emprecord,file1)
print("record heas been stored into the file successfully")
file1.close()


file1 = open("employeeinfo.DAT","rb")
emp = pickle.load(file1)
print(emp.Sid)
print(emp.Sname)





