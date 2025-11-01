"""CP1404/CP5632 Practical - Using ProgrammingLanguage.

Estimate: 15 minutes
Actual: 10 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    #
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Make sure __str__ works (should match the example format)
    print(python)

    # Make a list of the languages
    languages = [python, ruby, visual_basic]

    # Print the names of dynamically typed languages using is_dynamic()
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
