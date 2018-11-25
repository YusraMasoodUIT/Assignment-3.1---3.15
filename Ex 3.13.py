print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.13")
print("Use of help function ")
def average(num1 , num2):
    'function average takes 2 integers as input and calculates the average of them'
    sum = num1 + num2
    avg = sum/2
    print("The average is ")
    return avg


def noVowel(sen):
    'function noVowel takes a string as input and checks if that string contains vowel or not'
    for a in sen:
        if a == "a" or a == "e" or a == "i" or a == "o" or a == "u" or a == "A" or a == "E" or a == "I" or a == "O" or a == "U":
            global vowel
            vowel = vowel + 1
    if vowel > 0:
        return False
    else:
        return True

    
def allEven(list):
    'function allEven  takes a list of integers as input and returns all the even numbers in that list'
    y = 0
    length = len(list) 
    for x in list: 
       modul = x % 2
       if modul == 0 : 
           y = y + 1
    if y == length : 
        return True
    else:
        return False
def negative(list):
    'function negative takes a list of integers as input and returns all the negative numbers in that list'
    for number in list:
        if number < 0 :
            print(number)

input()

