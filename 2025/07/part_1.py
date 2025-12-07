from pathlib import Path

input_text = Path("2025/07/input.txt").read_text()

splits = 0
beam_xs = set()

for line in input_text.split("\n"):
    new_beam_xs = beam_xs.copy()

    for x, char in enumerate(line):
        if char == "S":
            new_beam_xs.add(x)
        elif char == "^" and x in beam_xs:
            splits += 1
            new_beam_xs.remove(x)
            new_beam_xs.add(x - 1)
            new_beam_xs.add(x + 1)

    beam_xs = new_beam_xs

print(splits)
