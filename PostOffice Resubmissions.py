'''
FLOWER POT
Name: Dylan Ever
Description: This code calculates the price of what the user wants to mail based on size and distance traveled
Date: 9/20/22
Bugs: If the price is too high there is an error
Challenges: None
Credits: Sawyer helped with try except feature, Cooper helped with functions
'''



def zipcodezone(zip): 
    #this function takes in the zipcodes and returns the postage zone
    #zip is equal to the zipcode

    #the if, elif, else statments check if the zipcode is within the paramaters and returns the postal codes
    if 1<=zip<=6999:
        return 1
    elif 7000<=zip<=19999:
        return 2
    elif 20000<=zip<=35999:
        return 3
    elif 36000<=zip<=62999:
        return 4
    elif 63000<=zip<=84999:
        return 5
    elif 85000<=zip<=99999:
        return 6
    else:
        return "UNMAILABLE"
    
def dimensions(length, height, thickness):
    #this function takes in the length height and thickness and returns a number which is later used to clarify price
    #length - length of package
    # height - height of package
    # thickness - thickness of package
    #the if, elif and else statements check which of the parameters the heigh length and thickness fall into and returns a number coresponding to the parameter.
   
    if 3.5 <= length <= 4.5 and 3.5 <= height <= 6 and .007 <= thickness <= 0.015:
        return 1 
    elif 4.25 <= length <= 6 and 6 <= height <= 11.5 and .007 <= thickness <= 0.015:
        return 2
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 <= thickness <= .25:
        return 3
    elif 6.125 <= length <= 24 and 11 <= height < 18 and .25 <= thickness <= 0.5:
        return 4
    elif length + 2*height + 2*thickness <= 84:
        return 5
    elif length + 2*height + 2*thickness <= 130:
        return 6
    else:
        return "UNMAILABLE"

def findsize(size,zone):
    #this function determines the cost of the package based on the number returned in dimensions 
    #size - the dimensions
    # zone - the first zipcode subtracted by the second zipcode
    #the if and elif statements take in all the given information and return a cost
    
    if size == 1:
        cost = .20 + .03 * zone                                 #regular post card - .20 dollar initial cost + .03 times the distance of zipcodes
    elif size == 2:
        cost = .37 + .03 * zone                                 #large post card
    elif size == 3:
        cost = .37 + .04 * zone                                 #Envelope
    elif size == 4:
        cost = .60 + .05 * zone                                 #Large Envelope
    elif size == 5:
        cost = 2.95 + .25 * zone                                #Package
    elif size == 6:
        cost = 3.95 + .35 * zone                                #Large Package
    return cost


def main():                                                     #main function
    #Asks the user to input diamaters and zipcodes and then returns the cost
    count = 0
    cost = 0                                                    #cost set to zero
    while count < 5:

        data = input("").split (",")
        L = float(data[0])                                         #converts answer to a float
        H = float(data[1])
        T = float(data[2])

        distance = int(data [3])                                   #converts answer to an intager
        distance1 = int(data [4])
        size = dimensions(L, H, T)

        zone = abs(zipcodezone(distance) - zipcodezone(distance1))
        output = findsize(size,zone)
        
        
        output = str(output).lstrip('0')    
        print(output)
        
main()