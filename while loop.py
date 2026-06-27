## input 6 ph values. calculate and output the average ph, percentage of values above 7 and the highest ph value.

total=0
highest=-1
above7=0
for count in range(6):
    ph= float(input("enter ph value"))
    total = total +ph
    if ph >highest:
        highest = ph
    if ph >7:
        above7 = above7+1
average = total/60
percentage = above7/60 *100
print ("average ph+", average)
print ("percentage+", percentage)
print ("highest+", highest)
        
    
