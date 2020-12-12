from collections import defaultdict
from helpers import memoize
from copy import deepcopy

# Complex numbers in Python! == i + nj (x + ny), good for coordinates
# complex*i to rotate left/ccw, complex*-i to rotate right/cw

with open("../input/day12.txt", 'r') as inputFile:
    data = [x.rstrip() for x in inputFile.readlines()]
    #data = [int(x) for x in data]

def addTuple(orig, add):
    return (orig[0] + add[0], orig[1] + add[1])

def mulTuple(tup, mult):
    newMult = mult if isinstance(mult, tuple) else (mult, mult)

    return (tup[0] * newMult[0], tup[1] * newMult[1])

def subTuple(orig, sub):
    return (orig[0] - sub[0], orig[1] - sub[1])

def flipTuple(orig, mulTuple):
    return (orig[1] * mulTuple[0], orig[0] * mulTuple[1])

# Part 1
start = (0, 0)
pos   = (0, 0)
slope = (1, 0)
for line in data:
    direction = line[0]
    count     = int(line[1:])

    if direction == 'F':
        pos = addTuple(pos, mulTuple(slope, count))
    elif direction == 'N':
        pos = addTuple(pos, mulTuple((0, 1), count))
    elif direction == 'E':
        pos = addTuple(pos, mulTuple((1, 0), count))
    elif direction == 'W':
        pos = addTuple(pos, mulTuple((-1, 0), count))
    elif direction == 'S':
        pos = addTuple(pos, mulTuple((0, -1), count))
    elif direction == 'L':
        turns = count // 90 - 1
        if slope[0] == 1:
            slope = [ (0, 1), (-1, 0), (0, -1) ][turns]
        elif slope[0] == -1:
            slope = [ (0, -1), (1, 0), (0, 1) ][turns]
        elif slope[1] == 1:
            slope = [ (-1, 0), (0, -1), (1, 0) ][turns]
        elif slope[1] == -1:
            slope = [ (1, 0), (0, 1), (-1, 0) ][turns]
    elif direction == 'R':
        turns = count // 90 - 1
        if slope[0] == 1:
            slope = [ (0, 1), (-1, 0), (0, -1) ][::-1][turns]
        elif slope[0] == -1:
            slope = [ (0, -1), (1, 0), (0, 1) ][::-1][turns]
        elif slope[1] == 1:
            slope = [ (-1, 0), (0, -1), (1, 0) ][::-1][turns]
        elif slope[1] == -1:
            slope = [ (1, 0), (0, 1), (-1, 0) ][::-1][turns]

print(abs(pos[0]) + abs(pos[1]))

# Part 2
start    = (0, 0)
waypoint = (10, 1)
pos      = (0, 0)
for line in data:
    direction = line[0]
    count     = int(line[1:])

    if direction == 'F':
        pos = addTuple(pos, mulTuple(waypoint, count))
    elif direction == 'N':
        waypoint = addTuple(waypoint, mulTuple((0, 1), count))
    elif direction == 'E':
        waypoint = addTuple(waypoint, mulTuple((1, 0), count))
    elif direction == 'W':
        waypoint = addTuple(waypoint, mulTuple((-1, 0), count))
    elif direction == 'S':
        waypoint = addTuple(waypoint, mulTuple((0, -1), count))
    else:
        if line == 'L180' or line == 'R180':
            waypoint = (-waypoint[0], -waypoint[1])
        elif line == 'L90' or line == 'R270':
            waypoint = (-waypoint[1], waypoint[0])
        elif line == 'L270' or line == 'R90':
            waypoint = (waypoint[1], -waypoint[0])
    #print(f"{line} - pos = {pos}, waypoint = {waypoint}")

print(abs(pos[0]) + abs(pos[1]))