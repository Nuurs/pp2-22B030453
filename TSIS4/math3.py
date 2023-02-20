from  math import tanh

def area_of_regular_polygon(a,b):
    area=a*(b**2)/(4*tanh(180/a))
    print (area)

a = int(input())
b = int(input())
area_of_regular_polygon(a,b)