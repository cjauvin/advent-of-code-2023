import math
from collections import defaultdict

s = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def part1():
    g = []

    # for line in s.split("\n"):
    for line in open("data/input03.txt").read().split("\n"):
        if not line.strip():
            continue
        g.append("." + line.strip() + ".")

    g.insert(0, "." * len(g[0]))
    g.append("." * len(g[0]))

    coords_to_value = defaultdict(int)
    symbol_coords = []

    for i, row in enumerate(g):
        val_accum = []
        for j, gij in enumerate(row):
            if gij.isdigit():
                val_accum.append((gij, i, j))
            elif val_accum:
                v = int("".join(c[0] for c in val_accum))
                for c in val_accum:
                    coords_to_value[(c[1], c[2])] = v
                val_accum = []
            if gij != "." and not gij.isdigit():
                symbol_coords.append((i, j))

    # print(coords_to_value)
    # print(symbol_coords)

    total = 0

    for c in symbol_coords:
        vals = set()
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                vals.add(coords_to_value[(c[0] + a, c[1] + b)])
        total += sum(vals)

    print(total)


def part2():
    g = []

    # for line in s.split("\n"):
    for line in open("data/input03.txt").read().split("\n"):
        if not line.strip():
            continue
        g.append("." + line.strip() + ".")

    g.insert(0, "." * len(g[0]))
    g.append("." * len(g[0]))

    coords_to_value = {}
    symbol_coords = []

    for i, row in enumerate(g):
        val_accum = []
        for j, gij in enumerate(row):
            if gij.isdigit():
                val_accum.append((gij, i, j))
            elif val_accum:
                v = int("".join(c[0] for c in val_accum))
                for c in val_accum:
                    coords_to_value[(c[1], c[2])] = v
                val_accum = []
            # if gij != "." and not gij.isdigit():
            if gij == "*":
                symbol_coords.append((i, j))

    total = 0

    for c in symbol_coords:
        vals = set()
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                i, j = c[0] + a, c[1] + b
                if (i, j) in coords_to_value:
                    vals.add(coords_to_value[(i, j)])
        if len(vals) == 2:
            total += math.prod(vals)

    print(total)


part1()
part2()
