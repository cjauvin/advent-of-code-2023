import os
import re

s = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def part1():
    total = 0

    # for line in s.split("\n"):
    for line in open("data/input04.txt"):
        if not line.strip():
            continue
        line = line.strip()
        m = re.match(r"Card +(\d+):(.+)\|(.+)", line)
        c = m.group(1)
        a = set(re.split(r"\W+", m.group(2).strip()))
        b = set(re.split(r"\W+", m.group(3).strip()))
        # print(c, a, b)
        if a & b:
            total += 2 ** (len(a & b) - 1)

    print(total)


def part2():
    d = {}
    e = {}

    # for line in s.split("\n"):
    for line in open("data/input04.txt"):
        if not line.strip():
            continue
        line = line.strip()
        m = re.match(r"Card +(\d+):(.+)\|(.+)", line)
        c = int(m.group(1))
        a = set(re.split(r"\W+", m.group(2).strip()))
        b = set(re.split(r"\W+", m.group(3).strip()))
        d[c] = len(a & b)
        e[c] = 1

    for c in range(1, len(d) + 1):
        for _ in range(e[c]):
            for cc in [c + i + 1 for i in range(d[c])]:
                e[cc] += 1

    print(sum(e.values()))


os.system("clear")
part1()
part2()
