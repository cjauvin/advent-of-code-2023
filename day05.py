import os
import re

s = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def map_value(ranges, v):
    for d, s, k in ranges:
        if v >= s and v < s + k:
            return d + (v - s)
    return v


def map_value_reversed(ranges, v):
    for d, s, k in ranges:
        if v >= d and v < d + k:
            return s + (v - d)
    return v


def parse_problem(s):
    parts = s.split("map")
    seeds = list(map(int, re.findall("\d+", parts[0])))
    maps = []
    for p in parts[1:]:
        a = list(map(int, re.findall("\d+", p)))
        b = [tuple(a[i : i + 3]) for i in range(0, len(a), 3)]
        maps.append(b)
    return seeds, maps


def part1():
    global s
    # seeds, maps = parse_problem(s)
    seeds, maps = parse_problem(open("data/input05.txt").read())
    vs = []
    for s in seeds:
        v = s
        for r in maps:
            v = map_value(r, v)
        vs.append(v)

    print(min(vs))


def part2():
    global s
    # seeds, maps = parse_problem(s)
    seeds, maps = parse_problem(open("data/input05.txt").read())
    seeds = [tuple(seeds[i : i + 2]) for i in range(0, len(seeds), 2)]
    maps = maps[::-1]
    found = False
    l = 0
    while True:
        v = l
        for r in maps:
            v = map_value_reversed(r, v)
        for s, k in seeds:
            if v >= s and v < s + k:
                found = True
                break
        if found:
            print(l)
            break
        l += 1


os.system("clear")
part1()
part2()
