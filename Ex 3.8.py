print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.8")
print("Tell me the radius of the circle  and I'll calculate its perimeter")
import math
rad = eval(input("Enter the radius of the circle "))
def perimeter(rad):
    y = math.pi
    x = 2 * y * rad
    print("The perimeter of circle is " + str(x))
   
perimeter(rad)

input()
