# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class of all
class Vehicle:
    def __init__(self):
        pass

# Vehicle base
class FlightVehicle(Vehicle):
    pass

# FlightVehicle base
class Starship(FlightVehicle):
    pass

# FlightVehicle base
class Airplane(FlightVehicle):
    pass

# Vehicle base
class GroundVehicle(Vehicle):
    pass

# GroundVehicle base
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
