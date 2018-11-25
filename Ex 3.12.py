print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.12")
print("Enter some numbers in the list and I'll tell you the negative numbers in that list")
num = eval(input("how many numbers do you want to enter in a list ")) #ask the user about how many numbers he want to enter
count = 0
list = []#initialize an empty list
while count != num: #loop which continues till user enter all the numbers
    lsint = eval(input("Enter the number "))
    list.append(lsint)
    count = count + 1

    if count == num:
        break
print("The list of integers is :-")
print(list) # display the list on the screen
print("The negative numbers in the list are ")
def negative(list):
    for number in list:
        if number < 0 :
            print(number)
negative(list)

input()

