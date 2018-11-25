print("Yusra Masood , 18B-093-CS , Section A")
print("Ex 3.10")
print("Enter a string and I'll tell you if the list contains all consonants or not")
sen = input("Enter a string ")
vowel = 0
def noVowel(sen):
    for a in sen:
        if a == "a" or a == "e" or a == "i" or a == "o" or a == "u" or a == "A" or a == "E" or a == "I" or a == "O" or a == "U":
            global vowel
            vowel = vowel + 1
    if vowel > 0:
        return False
    else:
        return True
    
noVowel(sen)

input()
