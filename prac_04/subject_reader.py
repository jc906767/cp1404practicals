"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    nested_info = load_data(FILENAME)
    display_subject_details(nested_info)

def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    nests = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        nests.append(parts)

        # Parts removed to complete Things to do step 2
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        #print(parts)  # See what the parts look like (notice the integer is a string)
        #print(parts)  # See if that worked
        #print("----------")

    input_file.close()
    return nests

def display_subject_details(nested_info):
    """Display subject details."""
    for subject_info in nested_info:
        print(f"{subject_info[0]} is taught by {subject_info[1]} and has {subject_info[2]} students")
main()