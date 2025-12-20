from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

class Solution(ABC):
    input_path = Path("input.txt")

    @abstractmethod
    def solve(self, input_text: str) -> Any:
        pass

    def answer(self) -> None:
        input_text = self.input_path.read_text()
        answer = self.solve(input_text=input_text)
        print(answer)