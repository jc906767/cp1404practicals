"""
CP1404/CP5632 - Practical
Program for loops practice
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input('Specify the number of "*" you wish to print'))
for i in range(0, n + 1, 1):
    print("*" * i, end='\n')
print()