from pathlib import Path


def solve(input_text: str) -> int:
    beam_xs = {}

    for line in input_text.split("\n"):
        new_beam_xs = beam_xs.copy()

        for x, char in enumerate(line):
            if char == "S":
                new_beam_xs[x] = 1
            elif char == "^" and x in beam_xs:
                timeline_count = beam_xs[x]

                for new_x in x - 1, x + 1:
                    if new_x not in new_beam_xs:
                        new_beam_xs[new_x] = 0

                    new_beam_xs[new_x] += timeline_count

                del new_beam_xs[x]

        beam_xs = new_beam_xs

    return sum(beam_xs.values())


if __name__ == "__main__":
    input_text = Path("2025/07/input.txt").read_text()
    total = solve(input_text)
    print(total)
