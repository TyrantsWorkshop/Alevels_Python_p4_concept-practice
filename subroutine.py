## write a function to calculate the area of a triangle using base and height.
## call the function from the main program and output the result.

def FindArea(B,H):
    area = 0.5 *B*H
    return(area)
base = float(input("enter base of the triangle"))
height = float (input("enter height of the triangle"))
print("area of the triangle:",FindArea(base,height))
