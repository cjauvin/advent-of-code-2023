import math
import re
from collections import defaultdict

s1 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def part1():
    bag = {"red": 12, "green": 13, "blue": 14}

    total = 0

    # for line in s1.split("\n"):
    for line in open("data/input02.txt"):
        line = line.strip()
        if not line:
            continue
        i = int(re.match("Game (\d+).+", line).group(1))
        m = re.findall("(\d+) (blue|red|green)", line)
        d = defaultdict(int)
        for v, c in m:
            d[c] = max(d[c], int(v))
        possible = True
        for c in bag:
            if d[c] > bag[c]:
                possible = False
                break
        total += i if possible else 0

    print(total)


def part2():
    total = 0

    # for line in s1.split("\n"):
    for line in open("data/input02.txt"):
        line = line.strip()
        if not line:
            continue
        m = re.findall("(\d+) (blue|red|green)", line)
        d = defaultdict(int)
        for v, c in m:
            d[c] = max(d[c], int(v))
        p = math.prod(d.values())
        total += p

    print(total)


part1()
part2()
