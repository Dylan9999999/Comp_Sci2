'''
FLOWER POT
Name: Dylan Ever
Description: This code takes a csv file and provides the user with functions to analyze the data.
Date: 12/13/2023
Bugs: n/a
Challenges: Creating graph,
Credits: Sawyer helped with try except feature, Cooper helped with functions
'''

import matplotlib.pyplot as plt 

def main():
   #this is the main function which asks the user which fucntion they want to run
    
    """ doc """
    from pathlib import Path
    current_dir = Path(__file__).parent
    print(current_dir)
    file_path = current_dir / "gcds_data3.csv"

    file_input = open(file_path, 'r+')    
    
    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True
    while go is True:
    #checks which answer the user inputted and runs the function the user choose
        print("Menu: Enter Choice or 'Q' to (Q)uit:")
        print("1) Print All Students in a specific Grade")
        print("2) Print a Specific Students Information")
        print("3) Graph Boys Vs. Girls")
        print("4) Print all males")
        print("5) Print all females")
        print("6) Print students in a specific town")
        print("7) How many kids in each family go to GCDS")
        print("8) Add student and information to file")
        print("9) Sort a city by last name")
        print("10) Create a file with kids from specific town")


        answer = input()
        if answer == "1":
            grade = input ("Enter a Grade: ")            
            check_grade(file_input, grade)
        elif answer == "2":
            student_lookup(file_input)
        elif answer == "3":
            boys_girls(file_input)
        elif answer == "4":
            check_males(file_input)
        elif answer == "5":
            check_females(file_input)
        elif answer == "6":
            location = input ("Enter a location: ").lower()
            check_location(file_input, location)
        elif answer == "7":
            family = input ("Enter a last name: ").lower()
            check_family(file_input, family)
        elif answer == "8":
            add_student(file_input)
        elif answer == "9":
            organize(file_input)
        elif answer == "10":
            csv(file_input)
        elif answer == "Q":
            go = False
            print("bye")
            return
        else:
            print("Invalid")
        cut = True
        cont = input("Would you like to keep going? y/n")
        
        if cont == "n":
            print ("Goodbye")     
            break
        else:
            continue       


def check_grade(file_in, grade):
    #Checks if a student is in the grade imputted and returns all students in that grade
    #file_in - reads in the excel document of information, grade - the grade level inputted by user
    #return void
    """ doc """

    file_in.seek(1)                                     #move pointer to line 1

    for record in file_in:
        kid = record.split(",")
        if kid[2] == "Grade " + grade :
            print(kid[1] + " " + kid[0])



def student_lookup(file_in):
    #Looks up all information about a specific student
    #file_in - reads in the excel document of information
    #return void
    """ doc """

    file_in.seek(1)                                     #move pointer to line 1

    first_name = input("Enter First Name:")
    last_name = input("Enter Last Name:")
    
    for record in file_in:
        kid = record.split(",")
        if kid[1].lower() == first_name.lower() and kid[0].lower() == last_name.lower():
            print("\n" + kid[1] + "\n" + kid[0] + "\n" + kid[2] + "\n" + kid[3] + "\n" + kid[4] + "\n" + kid[5] + "\n" + kid[6])
        else:
            print("Not found")
            break
def boys_girls(file_in):
    #Creates a graph plotting both the population of boys and girls
    #file_in - reads in the excel document of information
    #return void
    """doc"""
    boys = 0
    girls = 0
    file_in.seek(1)
    for record in file_in:
        kid = record.split(",")
        if kid[3] == "Male":
            boys += 1
        if kid[3] == "Female":
            girls += 1

  
    # x-coordinates of left sides of bars  
    left = [0, 1000] 
  
    # heights of bars 
    height = [boys, girls]

    # labels for bars 
    tick_label = ['Boys', 'Girls'] 
    # naming the x-axis 
    plt.xlabel('x - axis') 
    # naming the y-axis 
    plt.ylabel('y - axis') 
    # plot title 
    plt.title('Boys vs. Girls') 

    plt.bar(tick_label, height)
  
    # function to show the plot 
    plt.show() 

def check_males(file_in):
    #Prints first and last name of all males
    #file_in - reads in the excel document of information
    #return void

    file_in.seek(1)

    for record in file_in:
        kid = record.split(",")
        if kid[3] == "Male":
            print(kid[1] + " " + kid[0])
def check_females(file_in):
    #Prints first and last name of all females
    #file_in - reads in the excel document of information
    #return void

    file_in.seek(1)

    for record in file_in:
        kid = record.split(",")
        if kid[3] == "Female":
            print(kid[1] + " " + kid[0])

def check_location(file_in, location):
    file_in.seek(1)
    for record in file_in:
        kid = record.split(",")
        if kid[5].lower() == location:
            print ((kid[1] + " " + kid[0] + " - " + kid[5]))
def check_family(file_in, family):
    #Prints all people in a specific family
    #file_in - reads in the excel document of information, family - last name inputted by user
    #return void

    file_in.seek(1)
    home = ""
    for record in file_in:
        kid = record.split(",")
        if kid[0].lower() == family:
            home = kid[4]
    file_in.seek(1)
    for record in file_in:
        kid = record.split(",")
        if kid[4] == home:
            print(kid[1] + " " + kid[0])
        else:
            print("Not Found")
            break
def add_student(file_in):
    #Adds a new data set into the file
    #file_in - reads in the excel document of information
    #return void
    file_in.seek(1)                                     #move pointer to line 1

    for record in file_in:
        kid = record.split(",")

    add_first = input ("Enter an updated students' first name to add: ")
    add_last = input ("Enter the updated students' last name to add: ")
    add_grade = input ("Enter the updated students' grade to add: ")
    add_gender = input ("Enter the updated students' gender to add: ")
    add_address = input ("Enter the updated students' adress to add: ")
    add_city = input ("Enter the updated students' city to add: ")
    add_state = input ("Enter the updated students' state to add: ")
    f = open("C:/Users/dever26/Desktop/gcds_data3.csv", "a")
    f.write(add_last+","+add_first+","+"Grade "+add_grade+","+add_gender+ ","+add_address+","+add_city+","+add_state + "\n")
    f.close()

    f = open("C:/Users/dever26/Desktop/gcds_data3.csv", "r")
    print("The record has been added")
    f.close()
def organize(file_in):
    file_in.seek(1)
    city = input("Enter an city: ")
    last_names = []

    for record in file_in:
        kid = record.split(",")
        if kid[5].lower() == city.lower():
            list.append(last_names, kid[0])

    last_names.sort()
    print (last_names)
def csv(file_in):
    #Creates a csv titled town.csv which prints all members of a specific town
    #file_in - reads in the excel document of information
    #return void

    file_in.seek(1)
    f = open("town.csv", "a+")

    town = input("Enter a town: ")
    for record in file_in:
        kid = record.split(",")
        if town == kid[5].lower():
            f.write(kid[1] + " " + kid[0] + "\n")
    f.close()
    
if __name__ == '__main__': 
    main()
