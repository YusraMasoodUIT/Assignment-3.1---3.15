print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.11")
print ("Enter some numbers and I'll tell you if the list contains all even numbers or not")

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
def allEven(list): # start of Function
    y = 0
    length = len(list) # stores the length of the list
    for x in list: #calculates mod of every element in list by dividing it by 2
       modul = x % 2
       if modul == 0 : # if number is even the mod will be zero
           y = y + 1
    if y == length : # if the list is even then the number of mods would be equal to the number of elements in the list
        return True
    else:
        return False
    

input()
