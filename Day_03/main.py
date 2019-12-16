import matplotlib.pyplot as plt

route1 = list()
route2 = list()

def main(wires):
    mapRoute(wires[0], route1)
    mapRoute(wires[1], route2)
    intersections = set(route1) & set(route2)
    print(findShortestToOrigo(intersections))
    print(findShortestInLength(intersections, route1, route2))
    plt.scatter(*zip(*route1), s=1)
    plt.scatter(*zip(*route2), s=1)
    plt.scatter(*zip(*list(intersections)), marker='x')
    plt.scatter(*zip((0,0)), marker='o', s=10)
    plt.show()

def findShortestInLength(intersections, route1, route2):
    return min( route1.index(i)+1 +route2.index(i)+1 for i in intersections)

def mapRoute(wire, route):
    pos = [0,0]
    for path in wire:
        direction = path[:1]
        steps = path[1:]
        mapStep(direction, steps, pos, route)

def findShortestToOrigo(intersections):
    shortest = 9999999
    for i in intersections:
        length = abs(i[0]) + abs(i[1])
        if length < shortest:
            shortest = length
    return shortest

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
        route.append(tuple(pos))

def right(steps, pos, route):
    for i in range(steps):
        pos[0] += 1
        route.append(tuple(pos))


def up(steps, pos, route):
    for i in range(steps):
        pos[1] += 1
        route.append(tuple(pos))

def down(steps, pos, route):
    for i in range(steps):
        pos[1] -= 1
        route.append(tuple(pos))

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