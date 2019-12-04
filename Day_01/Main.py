import math

def calculate_first_sum(list):
    sum = 0
    for mass in list:
        sum += calcurate_fuel(int(mass[0:-1]))
    return sum

def calcurate_fuel(mass):
    """Fuel required to launch a given module is based on its mass.
    Specifically, to find the fuel required for a module, take its mass,
    divide by three, round down, and subtract 2."""
    fuel = math.floor(mass / 3) -2
    return fuel



if __name__== "__main__":
    with open("input.txt") as input_file:
        input = input_file.readlines()

    first_sum = calculate_first_sum(input)
    print("The fuel required to launch the spaceship:", first_sum)