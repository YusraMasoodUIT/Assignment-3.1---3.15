print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.3")

print("part a")
year=eval(input("Enter the year  "))
a = year%4 
if a == 0:
    print("could be a leap year")
else:
     print("definitely not a leap year")
input()


print("part b")
lottery = [273 , 908, 516]
ticket = eval(input("Enter your ticket number  "))
if ticket == lottery[0] or ticket == lottery[1] or  ticket == lottery[2]:
    print("You won")
else:
    print("Better luck next time")
input()
