from solution import Solution

class Part1(Solution):
    def solve(self, input_text: str) -> int:
        xys = []
        max_area = 0

        for line in input_text.split("\n"):
            x1, y1 = (int(n) for n in line.split(","))

            for x2, y2 in xys:
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)

            xys.append((x1, y1))

        return max_area


if __name__ == "__main__":
    Part1().answer()