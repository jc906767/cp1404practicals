"""
CP1404/CP5632 Practical
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int,
                 pointer_arithmetic: bool = False):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self) -> str:
        """Return a user friendly string for this language."""
        pointer_text = "supports pointer arithmetic" if self.pointer_arithmetic else "no pointer arithmetic"
        return (f"{self.name} ({self.typing} typing, "
                f"reflection={self.reflection}, {pointer_text}, "
                f"first appeared in {self.year})")

    def __repr__(self) -> str:
        """Return string representation useful for debugging."""
        return (f"ProgrammingLanguage({self.name!r}, {self.typing!r}, "
                f"{self.reflection!r}, {self.year!r}, {self.pointer_arithmetic!r})")

    def is_dynamic(self) -> bool:
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    c = ProgrammingLanguage("C", "Static", False, 1972, True)

    languages = [ruby, python, visual_basic, c]
    print(python)

    print("Dynamically typed languages:")
    for language in languages:
        if language.is_dynamic():
            print(f"- {language.name}")

    print("Languages with pointer arithmetic:")
    for language in languages:
        if language.pointer_arithmetic:
            print(f"- {language.name}")


if __name__ == "__main__":
    run_tests()
