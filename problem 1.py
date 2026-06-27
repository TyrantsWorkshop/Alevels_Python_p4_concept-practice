## input numbers until 0 is entered. for all numbers entered calculate:
## average of positive numbers, average of negative numbers and percentage of numbers ending in zero.

totalneg=0
totalpos=0
poscount=0
negcount=0
endzero=0
totalnum=0

num = int(input("enter number"))
while num != 0 :
    if num > 0:
        totalpos=totalpos + num
        poscount=poscount  + 1
    if num < 0:
        totalneg=totalneg + num
        negcount=negcount  + 1
    if num%10 == 0:
        endzero = endzero + 1
    totalnum = totalnum + 1
    num = int(input("enter number"))

posAverage=totalpos/poscount
negAverage=totalneg/negcount
percent=endzero/totalnum *100

print ("positive number average",posAverage)
print ("negative number average",negAverage)
print ("percent of number ending in 10",percent)   
