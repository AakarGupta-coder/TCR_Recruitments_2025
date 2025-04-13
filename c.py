import random, math

def random_noise():
    random_characters = ['$', '!', 'p', '-_-', ':D', '~', '@', '#']
    random_index = [random_characters[random.randint(0, len(random_characters) - 1)] for i in range(4)]

    temp = ""
    for i in random_index:
        temp = temp + i

    return temp


def hypotenuse(x, b):
    return math.sqrt(x**2 + y**2)

"""
This print statement should only run when c.py is executed directly,
NOT when it is imported into another file like b.py or a.py.

In Python, the special variable __name__ is set to "__main__" 
when a file is run directly. If the file is imported as a module, 
__name__ is set to the module's name instead.

By wrapping the print statement inside:
    if __name__ == "__main__":
we make sure it only executes when c.py is run directly and not during imports.
"""

if __name__ == "__main__":
    print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT")
