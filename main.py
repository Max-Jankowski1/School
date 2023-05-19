#Max Jankowski 

class Vehicle:
  #As I usually do. I like to capitalize nouns so I add the .title operation. Otherwise lower case inputs       would drive me crazy.
  #This is also the init method were the attributes of vehicle class will be set
    def __init__(self, make, model):
        self.make = make.title()  
        self.model = model.title()  
    #This is the get feature to display vehicle selection 
    def get_details(self):
        print("Make:", self.make)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call the parent class constructor, Thanks for the youTube playlist
        self.doors = doors

    def get_details(self):
        super().get_details()  
        print("Number of doors:", self.doors)


class Truck(Vehicle):
    def __init__(self, make, model, bed_length):
        super().__init__(make, model)  # Call the parent 
        self.bed_length = bed_length

    def get_details(self):
        super().get_details()  
        print("Truck bed length:", self.bed_length)

#This function follows the main() should user select 1
def create_car():
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors: ")
    car = Car(make, model, doors)  # Create an instance of the Car class
    car.get_details()  # Display the details of the car uses the class function in class Vehicle


def create_truck():
    make = input("Enter the make of the truck: ")
    model = input("Enter the model of the truck: ")
    bed_length = input("Enter the length of the truck bed: ")
    truck = Truck(make, model, bed_length)  # Create an instance of the Truck class
    truck.get_details()  # Display the details of the truck, from class function 


#main function, this function prompts user to input car or truck and then opens or quits program. 
#Had a bit of a hard time grasping Funtions a few weeks ago. I use them when I can now. 
def main():
    while True:
        print("Select the type of vehicle:")
        print("1. Car")
        print("2. Truck")
        print("0. Quit")
        choice = input("Enter your choice (0, 1, or 2): ")

        if choice == "1":
            create_car()  # Calls up the create_car() function
        elif choice == "2":
            create_truck()  # Calls up the create_truck() function
        elif choice == "0":
            print("Quitting the program.")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice!")

# Call the main function to start the program
if __name__ == "__main__":
    main()  

