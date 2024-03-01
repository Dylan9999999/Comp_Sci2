'''
FLOWER POT
Name: Dylan Ever
Description: This preforms a series of manipulation functions using an inputted name
Date: 2/28/2024
Bugs: n/a
Challenges: Creating menu, return boolean if name contains a title/distinction
Credits: Cooper, Zach and Mr. Campbell helped with functions. Collaborated with Asher on def random
'''

vowel = ["a","e","i","o","u"]
import random
def main():
    #this is the main function which asks the user which fucntion they want to run

    while True:
        name = input("Enter your name or enter q to quit: ")
        if lowercase(name) == "q":
            break
        print ("1) check vowels")
        print ("2) check consenents")
        print("3) convert lowercase to uppercase")
        print("4) check for title")
        print ("5) check for palindrome")
        print("6) convert uppervase to lowercase")
        print("7) reverse the name")
        print ("8) print first name")
        print ("9) print middle name")
        print ("10) print last name")
        print ("11) Check if last name contains a hyphen")
        print ("12) Create initials from the name")
        print ("13) Randomize the letters in name")
        question = input("What would you like to do?")
        if question == "1":
            print (vname(name), "vowels")
        elif question == "2":
            print (cname(name), "consenents")
        elif question == "3":
            print (uppercase(name))
        elif question == "4":
            print (has_title(name))
        elif question == "5":
            print(pal(name), "palindromes")
        elif question == "6":
            print(lowercase(name))
        elif question == "7":
            print (reverse_name(name))
        elif question == "8":
            print (first_name(name))
        elif question == "9":
            print (middle_name(name))
        elif question == "10":
            print (last_name(name))
        elif question == "11":
            print (hyph(name))
        elif question == "12":
            print (initials(name))
        elif question == "13":
            print(randomize(name))
        else:
            print("Invalid Response, try again")
def vname(name):
    #checks the number of vowels
    #name - reads in the name inputted by the user
    #returns the number of vowels
    count = 0
    name = lowercase(name)
    for letter in name:
        if letter in vowel:
            count +=1
    return(count)

def cname(name):
    #checks the number of consenents 
    #name - reads in the name inputted by the user
    #returns count - the number of consenents
    count = 0
    for letter in name:
        if letter not in vowel:
            count +=1
    return(count)   

def has_title(name):
    #checks if name has a title
    #name -reads in the name inputted by the user
    #Returns true  -  name has a title, false - name doesn't have a title
 
    titles = ["Dr.", "Sir", "Esq", "Ph.d"] 
    for title in titles:
        if title in name:
            return True
    return False
def pal(name):
    #checks if name is a palindrom
    #name - reads in the name inputted by the user
    #returns true - name is palindrome, false - name is not palindrome 
    print(name)
    print(name[::-1])
    if lowercase(name) == lowercase(name[::-1]):
        return True
    else:
        return False
def lowercase(string):
    #converts uppercase to lowercase
    #string - passes variable
    #returns lowercase_string - the inputted string with all lowercase values
    lowercase_string = ""
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            lowercase_string += chr(ord(char) + 32)
        else:
            lowercase_string += char
    return lowercase_string

def uppercase(string):
    #converts lowercase to uppercase
    #string - passes variable
    #returns lowercase_string - the inputted string with all uppercase values
    uppercase_string = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string
def reverse_name(name):
    #reverses name
    #name - reads in the name inputted by the user
    #returns name with reversed letter position
    return name[::-1]
def first_name(name):
    #prints first name
    #name - reads in the name inputted by the user
    #returns first_name - only the first name in name
    first_name = ""
    for letter in name:
        if letter != " ":
            first_name += letter
        else:
            break
    return first_name
def middle_name(name):
    #prints middle name
    #name - reads in the name inputted by the user
    #returns middle_name - only the middle name(s) in name
    middle_names = ""
    first_space = name.index(" ")
    last_space = name.rindex(" ")
    if first_space != last_space:
        middle_names = name[first_space:last_space].strip()
    return middle_names
def last_name(name):
    #prints last name
    #name - reads in the name inputted by the user
    #returns last_name - only the first name in name
    last_name = ""
    for i in range(len(name)-1, -1, -1):
        if name[i] != " ":
            last_name = name[i] + last_name
        else:
            break
    return last_name
def hyph(name):
    #checks if last name has hyphen
    #name - reads in the name inputted by the user
    #returns true or false determining on if there is a hyphen
    lname = last_name(name)
    return "-" in lname
def initials(name):
    # converts name to initials
    #name - reads in the name inputted by the user
    #returns initials - first letter of each name
    initials = ""
    words = name.split()
    for word in words:
        initials += word[0]
    return initials
def randomize(name):
    #randomizes the letters in name
    #name - reads in the name inputted by the user
    #returns rname - the name with randomized scrambled letters
    list_name = []
    rname = ""
    for letter in name:
        list_name.append(letter)

    while len(list_name) > 0:
        rnum = random.randint(0,len(list_name)-1)
        rname += list_name.pop(rnum)
    return (rname)
main()
