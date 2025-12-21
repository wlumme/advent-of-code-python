import pytest
from part_2 import XY, get_green_line, get_green_xys, get_red_xys, solve


@pytest.mark.parametrize(
    argnames=("input_text", "expected"),
    argvalues=[
        ("7,1", 1),
        ("7,1\n11,1", 5),
        # ("7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3", 24),
    ],
)
def test_solve(input_text: str, expected: int) -> None:
    assert solve(input_text) == expected


@pytest.mark.parametrize(
    argnames=("input_text", "expected"),
    argvalues=[
        (
            "7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3",
            [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)],
        ),
    ],
)
def test_get_red_xys(input_text: str, expected: list[XY]) -> None:
    assert get_red_xys(input_text) == expected


@pytest.mark.parametrize(
    argnames=("red_xys", "expected"),
    argvalues=[
        (
            [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)],
            {
                (7, 2),
                (8, 1),
                (9, 1),
                (10, 1),
                (11, 2),
                (11, 3),
                (11, 4),
                (11, 5),
                (11, 6),
                (10, 7),
                (9, 6),
                (3, 5),
                (4, 5),
                (5, 5),
                (6, 5),
                (7, 5),
                (8, 5),
                (2, 4),
                (3, 3),
                (4, 3),
                (5, 3),
                (6, 3),
            },
        ),
    ],
)
def test_get_green_xys(red_xys: list[XY], expected: int) -> None:
    assert get_green_xys(red_xys) == expected


@pytest.mark.parametrize(
    argnames=("xy1", "xy2", "expected"),
    argvalues=[
        ((1, 1), (1, 1), []),
        ((1, 1), (1, 2), []),
        ((1, 1), (2, 1), []),
        ((1, 1), (1, 3), [(1, 2)]),
        ((1, 1), (3, 1), [(2, 1)]),
        ((1, 1), (1, 4), [(1, 2), (1, 3)]),
        ((1, 1), (4, 1), [(2, 1), (3, 1)]),
        ((7, 3), (7, 1), [(7, 2)]),
        ((7, 1), (11, 1), [(8, 1), (9, 1), (10, 1)]),
        ((11, 1), (11, 7), [(11, 2), (11, 3), (11, 4), (11, 5), (11, 6)]),
        ((11, 7), (9, 7), [(10, 7)]),
        ((9, 7), (9, 5), [(9, 6)]),
        ((9, 5), (2, 5), [(3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]),
        ((2, 5), (2, 3), [(2, 4)]),
        ((2, 3), (7, 3), [(3, 3), (4, 3), (5, 3), (6, 3)]),
    ],
)
def test_get_green_line(xy1: XY, xy2: XY, expected: int) -> None:
    x1, y1 = xy1
    x2, y2 = xy2
    assert get_green_line(x1=x1, y1=y1, x2=x2, y2=y2) == expected
    assert get_green_line(x1=x2, y1=y2, x2=x1, y2=y1) == expected
