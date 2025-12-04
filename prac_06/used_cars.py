"""
CP1404- Client code to use the Car class.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use the Car class."""
    # Create a car called "My car" with 100 fuel, drive it 40 km
    my_car = Car("My car", 100)
    my_car.drive(40)
    print(f"Fuel left in my_car: {my_car.fuel}")
    print(my_car)  # This will call Car.__str__()

    print()  # spacer for readability

    # Create a new Car called "Limo" with 100 fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to limo
    limo.add_fuel(20)

    # Print the amount of fuel in limo
    print(f"Fuel in limo after refuel: {limo.fuel}")

    # Attempt to drive limo 115 km
    limo.drive(115)

    # Print limo details (name, fuel left, odometer)
    print(limo)


main()
