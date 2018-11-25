print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.5")
print("This program will tell you the words that have four letters in it")
list = [] #create an empty list
num = eval(input("how many words do you want to enter "))#ask the user for the number of inputs
a = 1
while a != num + 1: # loop to enter the words according to user's wish
           word1 = input("Enter a word ")
           list.append(word1)#assign words to list
           a = a+1
           if a == num +1:# stopping while loop
               break
print("The four letter words are :-")
for word in list: #start of for loop to seperate each word from list
    flett = 0
    for lett in word:#start of for loop to seperate eachletter from the seperated word
        flett = flett + 1
    if flett == 4:
       print(word)#print the word if it contains exactly four letters

input()
