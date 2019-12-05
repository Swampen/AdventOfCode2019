import operator as op

"""
99: halt
1: adds two numbers from two positions, and stores it in a third position.
The three integers immediately after the opcode tell you these three positions -
the first two should be added together, the third should where the sum should be stored.

2: same as 1, but with multiplication
"""
operator = { 1: op.add, 2: op.mul}

def restore_gravity(ints, noun, verb):
    pos = 0

    ints[1] = noun
    ints[2] = verb

    while ints[pos] != 99:
        action = ints[pos]
        first = ints[pos+1]
        second = ints[pos+2]
        output = ints[pos+3]

        result = operator[action](ints[first], ints[second])
        ints[output] = result

        pos+=4

    return ints[0]

def restore_gravity_memory():
    for noun in range(99):
        for verb in range(99):
            ints = get_input()
            result = restore_gravity(ints, noun, verb)
            if (result == 19690720):
                return 100 * noun + verb


def get_input():
    with open("input.txt") as input:
        strings = input.read().split(",")
        ints = [int(i) for i in strings]
    return ints


if __name__ == "__main__":
    ints = get_input()
    print("First star:", restore_gravity(ints, 12, 2))

    print("Second star:", restore_gravity_memory())
