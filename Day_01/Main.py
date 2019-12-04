import math

def calculate_first_sum(list):
    sum = 0
    for mass in list:
        sum += calcurate_fuel(int(mass[0:-1]))
    return sum

def calculate_second_sum(list):
    sum = 0
    for mass in list:
        mass = int(mass[0:-1])
        while mass > 0:
            mass = calcurate_fuel(mass)
            sum += mass
    return sum

def calcurate_fuel(mass):
    """Fuel required to launch a given module is based on its mass.
    Specifically, to find the fuel required for a module, take its mass,
    divide by three, round down, and subtract 2."""
    fuel = math.floor(mass / 3) - 2
    return (0, fuel)[fuel > 0]



if __name__== "__main__":
    with open("input.txt") as input_file:
        input = input_file.readlines()

    print("The fuel required to launch the spaceship the first time:", calculate_first_sum(input))
    print("The fuel required to launch the spaceship the second time:", calculate_second_sum(input))