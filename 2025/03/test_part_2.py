from pathlib import Path

import pytest
from part_1 import get_max_joltage as part_1
from part_2 import get_max_joltage as part_2


def get_input() -> list[str]:
    return Path("2025/03/input.txt").read_text().split("\n")


@pytest.mark.parametrize(
    argnames=("bank", "expected"),
    argvalues=[
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_get_max_joltage_examples(bank: str, expected: int) -> None:
    assert part_2(bank, 2) == expected


@pytest.mark.parametrize(argnames=("bank"), argvalues=get_input())
def test_get_max_joltage_against_part_1(bank: str) -> None:
    assert part_2(bank, 2) == part_1(bank)
