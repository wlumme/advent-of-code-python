from textwrap import dedent

import pytest
from part_2 import solve


@pytest.mark.parametrize(
    argnames=("input_text", "expected"),
    argvalues=[
        (".", 0),
        ("@", 1),
        ("..\n@@", 2),
        ("..@\n@@@\n@@@", 7),
        ("..@@\n@@@.\n@@@@\n@.@@", 12),
        (
            """\
            ..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.
            """,
            43,
        ),
    ],
)
def test_solve(input_text: str, expected: int) -> None:
    input_text = dedent(input_text)
    assert solve(input_text) == expected
