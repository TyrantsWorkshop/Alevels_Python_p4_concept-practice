## create a base class shape and derived classes rectangle and circle.
## override findArea in each derived class. input dimensions and output the area of each shape.

class shape:
	def __init__(self):
		self.__areaValue = 0
	def findArea(self):
		print("area value=",self.__areaValue)

class Rectangle(shape):
	def __init__(self,L,B):
		shape.__init__(self)
		self.__lenght = L
		self.__breadth = B
	def findArea(self):
		self.__areaValue = self.__lenght * self.__breadth
		print("area value=",self.__areaValue)

class circle(shape):
	def __init__(self,R):
		shape.__init__(self)
		self.__radius=R
	def findArea(self):
		self.__areaValue = 3.14 * self.__radius * self.__radius
		print("area value=",self.__areaValue)


R = float(input("enter radius"))
objCircle = circle(R)
objCircle.findArea()

L = float(input("enter lenght"))
B = float(input("enter breadth"))
objRectangle = rectangle(L,B)
objRectangle.findArea()
