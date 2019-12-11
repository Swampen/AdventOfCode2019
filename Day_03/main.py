
def main(wires):
    for wire in wires:
        mapRoute(wire)
    return

def mapRoute(wire):
    for path in wire:
        direction = path[:1]
        steps = path[1:]
        print(direction, steps)



def getInput():
    with open("input.txt") as input:
        text = input.read()
        array = text.split("\n")[:-1]
        wires = []
        for i in array:
            wires.append(i.split(","))
        return wires

if __name__ == "__main__":
    wires = getInput()
    main(wires)