from collections.abc import Generator
from random import randint

import pytest
from part_2 import get_factors, is_invalid, is_invalid_for_factor, run, sum_invalids


def test_run() -> None:
    input_text = """\
        11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
        1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
        824824821-824824827,2121212118-2121212124
    """
    assert run(input_text) == 4_174_379_265


@pytest.mark.parametrize(
    argnames=("lower", "upper", "expected"),
    argvalues=[
        (11, 22, 33),
        (95, 115, 210),
        (998, 1012, 2009),
        (1188511880, 1188511890, 1188511885),
        (222220, 222224, 222222),
        (1698522, 1698528, 0),
        (446443, 446449, 446446),
        (38593856, 38593862, 38593859),
        (565653, 565659, 565656),
        (824824821, 824824827, 824824824),
        (2121212118, 2121212124, 2121212121),
    ],
)
def test_sum_invalids_example(lower: int, upper: int, expected: int) -> None:
    assert sum_invalids(lower, upper) == expected


@pytest.mark.parametrize(
    argnames=("n"), argvalues=[11, 22, 12341234, 123123123, 1212121212, 1111111]
)
def test_is_invalid_is_true(n: int) -> None:
    assert is_invalid(n)


@pytest.mark.parametrize(argnames=("n"), argvalues=[1])
def test_is_invalid_is_false(n: int) -> None:
    assert not is_invalid(n)


@pytest.mark.parametrize(argnames=("n", "expected"), argvalues=[(2, [1]), (1, [])])
def test_get_factors(n: int, expected: list[int]) -> None:
    assert get_factors(n) == expected


@pytest.mark.parametrize(argnames=("s", "factor"), argvalues=[("11", 1)])
def test_is_invalid_for_factor_returns_true(s: str, factor: int) -> None:
    assert is_invalid_for_factor(s, factor)


@pytest.mark.parametrize(argnames=("s", "factor"), argvalues=[("12", 1)])
def test_is_invalid_for_factor_returns_false(s: str, factor: int) -> None:
    assert not is_invalid_for_factor(s, factor)


def generate_invalid_input(
    count: int, max_unit: int = 999, max_copies: int = 10
) -> Generator[int]:
    for _ in range(count):
        unit = randint(1, max_unit)
        copies = randint(2, max_copies)
        value = str(unit) * copies
        yield int(value)


def generate_valid_input(
    count: int, max_value: int = 999_999_999_999
) -> Generator[int]:
    for _ in range(count):
        yield randint(1, max_value)


@pytest.mark.parametrize(argnames=("n"), argvalues=generate_invalid_input(10))
def test_is_invalid_random_always_invalid(n: int) -> None:
    assert is_invalid(n)


@pytest.mark.parametrize(argnames=("n"), argvalues=generate_valid_input(10))
def test_is_invalid_random_never_invalid(n: int) -> None:
    assert not is_invalid(n)
