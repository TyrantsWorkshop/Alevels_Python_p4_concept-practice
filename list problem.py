##write a program to input and store 10 numbers using a list.perform the following -
##copy ther numbers which are even to a new list named evenlist.
##output average of numbers stored in the new list

evenlist = [ ]
num = [ ]
for i in range(10):
    num.append(int(input("enter number")))
    if num[i]%2==0:
        evenlist.append(num[i])
print(evenlist)
total = 0
for i in range(len(evenlist)):
    total=total +evenlist[i]
average = total/len(evenlist)
print("average=",average)
    

