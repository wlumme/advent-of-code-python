from itertools import combinations
from pathlib import Path


def calculate_distance(
    connection: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> float:
    (x1, y1, z1), (x2, y2, z2) = connection
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


input_text = Path("2025/08/input.txt").read_text()

xyzs = []

for line in input_text.split("\n"):
    x, y, z = (int(n) for n in line.split(","))
    xyzs.append((x, y, z))

connections = combinations(xyzs, 2)
connections = sorted(connections, key=calculate_distance)[:1000]

groups: list[set[tuple[int, int, int]]] = []

for xyz1, xyz2 in connections:
    i1 = None
    i2 = None
    for i, group in enumerate(groups):
        if xyz1 in group:
            i1 = i
        if xyz2 in group:
            i2 = i
    if i1 is not None and i2 is not None:
        if i1 != i2:
            groups[i1] |= groups[i2]
            groups.pop(i2)
    elif i1 is not None:
        groups[i1].add(xyz2)
    elif i2 is not None:
        groups[i2].add(xyz1)
    else:
        groups.append({xyz1, xyz2})

group_sizes = sorted([len(group) for group in groups], reverse=True)
print(group_sizes[0] * group_sizes[1] * group_sizes[2])
