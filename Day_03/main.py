
map = []
pos = [0,0]
def main(wires):
    for wire in wires:
        mapRoute(wire)
    print(map)
    return

def mapRoute(wire):
    global pos
    pos = [0,0]
    for path in wire:
        direction = path[:1]
        steps = path[1:]
        mapStep(direction, steps)
        print(pos)

def mapStep(direction, steps):
    switcher = {
        "L": left,
        "R": right,
        "U": up,
        "D": down
    }

    func = switcher.get(direction)
    func(int(steps))

def left(steps):
    global map
    for i in range(steps):
        return


def right(steps):
    global map
    for i in range(steps):
        return


def up(steps):
    return

def down(steps):
    global map
    for i in range(steps):
        return

def getInput():
    with open("input.txt") as input:
        text = input.read()
    array = text.split("\n")[:-1]
    wires = []
    for i in array:
        wires.append(i.split(","))
    return wires

def getTestInput():
    with open("test.txt") as input:
        text = input.read()
    array = text.split("\n")[:-1]
    wires = []
    for i in array:
        wires.append(i.split(","))
    return wires


if __name__ == "__main__":
    wires = getTestInput()
    main(wires)