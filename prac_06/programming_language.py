"""CP1404/CP5632
ProgrammingLanguage class.

Estimate: 20 minutes
Actual: 20 minutes
"""


class ProgrammingLanguage:


    def __init__(self, name: str, typing: str, reflection: bool, year: int):

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:

        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:

        reflection_text = "Yes" if self.reflection else "No"
        return (f"{self.name}, {self.typing} Typing, Reflection={reflection_text}, "
                f"First appeared in {self.year}")