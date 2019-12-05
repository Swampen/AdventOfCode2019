import operator as op

"""
99: halt
1: adds two numbers from two positions, and stores it in a third position.
The three integers immediately after the opcode tell you these three positions -
the first two should be added together, the third should where the sum should be stored.

2: same as 1, but with multiplication
"""
operator = { 1: op.add, 2: op.mul}

def restore_gravity(ints):
    pos = 0

    ints[1] = 12
    ints[2] = 2

    while ints[pos] != 99:
        print(ints)
        action = ints[pos]
        first = ints[pos+1]
        second = ints[pos+2]
        output = ints[pos+3]

        result = operator[action](ints[first], ints[second])
        ints[output] = result

        pos+=4

    return ints[0]

if __name__ == "__main__":
    with open("input.txt") as input:
        strings = input.read().split(",")
        ints = [int(i) for i in strings]

    print(restore_gravity(ints))