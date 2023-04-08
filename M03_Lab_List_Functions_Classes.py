'''
Car Search
Aaron Roberson
4/8/2023
This app will take a users input on the type of car they are looking for with certain specifications
and then output what they have entered.
'''

#Creating the parent super class
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
#Creating the child class and using super to access the vehicle type method from the parent
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type) #super to use method from vehicle class
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
#Asking the user for input and testing if their input is valid
while True:
    vehicle_type= input("What type of vehicle are you looking for?  (Car, Truck): ") #user input
    if not vehicle_type.isalpha(): #testing if the user input is not alphabetical
        print("Invalid Entry! Please only enter letters. ")
    elif vehicle_type not in ["car", "Car", "truck", "Truck"]: #testing if the input isnt Car or Truck in upper or lower case
        print("Invalid Entry! Please enter Car or Truck")
    else: #user input is correct and exiting loop
        break

#Asking the user for input and testing if their input is valid
while True:
    try:  
        year = int(input("What year is the vehicle?: ")) #user input
        break
    except ValueError: #if their input is not an integer then tell them to enter correct date
        print("Invalid Entry! Please enter a valid date. ")

#Asking the user for input and testing if their input is valid
while True:
    make = input("Who is the maker of the vehicle? (Chevrolet, Ford, Nissan, Subaru): ") #user input
    if not make.isalpha(): #checking if user input is not alphabetical
        print("Invalid Entry! Please only enter letters. ")
    elif make not in ["Chevrolet", "chevrolet", "ford", "Ford", "Nissan", "nissan", "Subaru", "subaru"]: #testin if user input is not a valid car maker. In this case I am only testing for 4 makers since there are so many.
        print("Invalid Entry! Please enter a valid car maker. (Chevrolet, Ford, Nissan, Subaru)")           #You could initialize a carMaker list and input all of the different makers and say if make not in carMaker
    else: #user input is correct and exiting loop
        break

#Asking the user for input and testing if their input is valid
while True:
    model = input("What is the model of the vehicle? (Impala, Explorer, Altima, WRX): ") #user input
    if model not in ["Impala", "impala", "Explorer", "explorer", "Altima", "altima", "WRX", "wrx"]: #testing if user input valid car model. In this case I am only testing 4 models since there are many models from each maker.
        print("Invalid Entry! Please enter a valid car model. (Impala, Explorer, Altima, WRX)")     #You could initialize a carModel list and input all of the models of cars made by each maker and is if model not in carModel
    elif not model.isalpha(): #checking if the user input is not alphabetical
        print("Invalid Entry! Please only enter letters. ")
    else: #user input is correct and exiting loop
        break

#Asking the user for input and testing if their input is valid
while True:
        try:            
            doors = int(input("How many doors does the vehicle have? (2 or 4): ")) #user input
            if doors not in [2, 4]:  #checking if user input is not an integer 
                raise ValueError #if user enters a number but it is not 2 or 4 then a ValueError is raised to let user know their input is incorrect 
            break
        except ValueError:
            print("Invalid Entry! Please enter either 2 or 4 doors. ") #letting user know their input is invalid        

#Asking the user for input and testing if their input is valid
while True:    
    roof = input("What kind of roof are you looking for? (Solid, Sunroof) ") #user input
    if not roof.isalpha(): #checking if user input is not alphabetical
        print("Invalid Entry! Please only enter letters. ")
    elif roof not in ["Solid", "solid", "Sunroof", "sunroof"]: #checking if user input is either Solid or Sunroof
        print("Invalid Entry! Please enter a valid option. (Solid or Sunroof)") #lettin user know their input is invalid
    else: #user input is correct and exiting loop
        break

#creating object as an instance of the automobile class
userCar = Automobile(vehicle_type, year, make, model, doors, roof)

#printing the user input and capitalizing each word if the user entered a word in all lowercase letters
print("Vehicle Type:", userCar.vehicle_type.capitalize())
print("Year:", userCar.year)
print("Make:", userCar.make.capitalize())
print("Model:", userCar.model.capitalize())
print("Number of doors:", userCar.doors)
print("Type of roof:", userCar.roof.capitalize())
