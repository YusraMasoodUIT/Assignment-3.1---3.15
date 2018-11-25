print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.15")
print("use of swapping function")
num = eval(input("How many names do you want to enter "))
team=[]
x = 0
while x != num:
    name = input("Enter the name ")
    team.append(name)
    x = x+1
    if x == num :
        break

print(team)

team[0], team[num-1]= team[num-1], team[0]
print("List after applying swapping function:- ")
print(team)
