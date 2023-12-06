# it's really easier to replace the numbers in python.

import sys
import re

regex = re.compile(
    "(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))+"
)


def map_number(n: str):
    try:
        return int(n)
    except ValueError:
        return {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }[n]


for line in sys.stdin:
    m = list(map(map_number, regex.findall(line)))
    print(m[0], m[-1], sep="")
