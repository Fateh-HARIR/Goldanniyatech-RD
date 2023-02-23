###################################
# Python Pocket Card - 02 Classes #
###################################
# Classes & Modules

# Built-in Modules 
import os
import sys


#################################
# Basic Classes
#################################

class Animals: 
    """ Class without arguments to create any kind of animal """

    # The built-it __init__ function is always executed when the class is initiated
    def __init__(self): 
        pass # Statement to use as a placeholder. 

# Objects Instantiation
Dolphin = Animals()
Dinosaur = Animals() 


class Vehicles: 
    """ Vehicle Class """
    
    # Variable initialization
    vehicle_name = ""
    vehicle_seats = 0 
    vehicle_transmission = ""

    # Class constructor
    def __init__ (self, carName, carSeats, carTransmission): 
        self.vehicle_name = carName 
        self.vehicle_seats = carSeats
        self.vehicle_transmission = carTransmission
     
    # Class Methods 
    def ConsoleClear(self): 
        """ Clear the IDE Terminal/ Console on Windows """
        if os.name == 'nt': os.system('cls')
        else: os.system('clear')
     
    def showVehicleInformation(self): 
        """ Showing some information about the vehicle """
        self.ConsoleClear()
        print("Vehicle Name: " + str(self.vehicle_name))
        print("Vehicle Seats: " + str(self.vehicle_seats)) 
        print("Vehicle Transmission: " + str(self.vehicle_transmission))
     
    def carDriving(self): 
        pass


Lamborghini = Vehicles("Lamborghini", 2, "Auto")
Lamborghini.showVehicleInformation() 


