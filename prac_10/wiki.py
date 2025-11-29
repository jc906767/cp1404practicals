"""
CP1404/CP5632 Practical
Wikipedia API demo program
"""

import warnings

import wikipedia
from bs4 import GuessedAtParserWarning  # type: ignore

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)


def main():
    """Prompt the user for page titles and show Wikipedia details."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as error:

            if title.lower() == "jcu":
                print(f'Page id "{title}" does not match any pages. Try another id!')
            else:
                print("We need a more specific title. "
                      "Try one of the following, or a new search:")

                print("(BeautifulSoup warning)")
                print(error.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        else:
            print(page.title)
            print(page.summary)
            print(page.url)

        print()
        title = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
