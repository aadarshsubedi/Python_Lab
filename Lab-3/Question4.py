#Create a function that returns both the area and circumference of a circle given its radius. 
PI=3.147
def Circle(r):
    area=PI*r**2
    circumference=2*PI*r
    return area,circumference

list=Circle(5)
print(f"The area and circumference is {list}")