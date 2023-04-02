#Student GPA Checker
#Aaron Roberson
#4/2/2023
#This program asks user to input a students name and gpa and determines if they/
#are on the deans list, honor roll, or neither.

#asking user to input students last name
lName = input("Enter students last name or ZZZ to quit: ")
#checking if the users input is valid
while True:
    if lName.isalpha():
        break
    else:
        lName = input("Invalid Entry! Please enter students last name: ")
        continue

#loop that runs if ZZZ is not entered by the user
while lName != "ZZZ":
    
    fName = input("Enter students first name: ") #asking user to input student first name
    #checking if the users input is valid
    while True:
        if fName.isalpha():
            break
        else:
            fName = input("Invalid Entry! Please enter students first name: ")
            continue
        
    
    #loop to get the user to input the students gpa and validate the input is a float
    while True:
        try:
            gpa = float(input("Enter students grade point average: "))

        except ValueError:
            print("Invalid Entry! Please enter students gpa: ")

        else:
            break 

                     
# checking if the gpa entered by user is greater than or equal to 3.5 to see if they are on deans list
    if (gpa >= 3.5):
        print(fName, lName, "made the Dean's list! ")
        lName = input("Enter students last name or ZZZ to quit: ")
# checking if the gpa entered by user is greater than or equal to 3.25 and if they made the honor roll
    elif (gpa >= 3.25):
        print(fName, lName, "has made the Honor Roll! ")
        lName = input("Enter students last name or ZZZ to quit: ")
# informing user that the student entered gpa doesnt allow them on the deans list or honor roll
    else:
        print("Sorry", fName, "didn't make the Dean's List or the Honor Roll. ")
        lName = input("Enter students last name or ZZZ to quit: ") 