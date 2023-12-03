import re

s1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

s2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def part1():
    total = 0

    # for line in s1.split("\n"):
    for line in open("data/input01.txt"):
        line = line.strip()
        if not line:
            continue
        # print(line)
        a = "".join(re.findall("\d", line))
        n = int(a[0] + a[-1])
        total += n

    print(total)


def part2():
    NS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    total = 0

    # for line in s2.split("\n"):
    for line in open("data/input01.txt"):
        line = line.strip()
        if not line:
            continue
        # print(line)
        # a = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", line)
        ms = re.finditer(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        a = [m.group(1) for m in ms]
        b = []
        for i in [0, -1]:
            if a[i] in NS:
                b.append(str(NS.index(a[i]) + 1))
            else:
                b.append(a[i])
        # print(b)
        n = int(b[0] + b[-1])
        total += n

    print(total)


part1()
part2()
