"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    all_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        all_data.append(parts)

        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        #print(parts)  # See what the parts look like (notice the integer is a string)
        #print(parts)  # See if that worked
        #print("----------")

    input_file.close()
    return all_data

main()