# actually much simpler than part 1 :)

import sys
import re

regex = re.compile("(\d\d?) (green|blue|red)")

total = 0

for index, game in enumerate(sys.stdin):
    max_red = 0
    max_green = 0
    max_blue = 0

    shows = game.split(";")
    for show in shows:
        matches = {color: int(value) for (value, color) in regex.findall(show)}

        max_red = max(matches.get("red", 0), max_red)
        max_green = max(matches.get("green", 0), max_green)
        max_blue = max(matches.get("blue", 0), max_blue)
        
    total += max_red * max_green * max_blue


print(total)
