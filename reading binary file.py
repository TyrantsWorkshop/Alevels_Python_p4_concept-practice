## read employee record data from a binary file named employeeinfo.DAT using pickle and display the employee id and name.

import pickle
class employee:
    def __init__(self,Id,name):
        self.Sid = ""
        self.Sname = ""
emp = employee()
emp = pickle.load(file1)
print(emp.Sid)
print(emp.Sname)


