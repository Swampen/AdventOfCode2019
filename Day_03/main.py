
route1 = set()
route2 = set()
def main(wires):
    mapRoute(wires[0], route1)
    mapRoute(wires[1], route2)
    intersections = route1 & route2
    compare(intersections)
    return

def compare(intersections):
    shorotest = 9999999
    for i in intersections:
        length = abs(i[0]) + abs(i[1])
        if length < shorotest:
            shorotest = length
    print(shorotest)

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
        route.add(tuple(pos))



def right(steps, pos, route):
    for i in range(steps):
        pos[0] += 1
        route.add(tuple(pos))


def up(steps, pos, route):
    for i in range(steps):
        pos[1] += 1
        route.add(tuple(pos))

def down(steps, pos, route):
    for i in range(steps):
        pos[1] -= 1
        route.add(tuple(pos))

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