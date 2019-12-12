
route1 = []
route2 = []
def main(wires):
    mapRoute(wires[0], route1)
    mapRoute(wires[1], route2)
    compare(route1, route2)
    return

def compare(route1, route2):
    for i in route1:
        for j in route2:
            if i == j:
                print(i, j)

def mapRoute(wire, route):
    pos = [0,0]
    for path in wire:
        direction = path[:1]
        steps = path[1:]
        mapStep(direction, steps, pos, route)

def mapStep(direction, steps, pos, route):
    switcher = {
        "L": left,
        "R": right,
        "U": up,
        "D": down
    }
    func = switcher.get(direction)
    func(int(steps), pos, route)

def left(steps, pos, route):
    for i in range(steps):
        pos[0] -= 1
        route.append(pos)



def right(steps, pos, route):
    for i in range(steps):
        pos[0] += 1
        route.append(pos)


def up(steps, pos, route):
    for i in range(steps):
        pos[1] += 1
        route.append(pos)

def down(steps, pos, route):
    for i in range(steps):
        pos[1] -= 1
        route.append(pos)

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