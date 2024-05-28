"""
Simple Calculator

Write a function named "calculate" which gets the following arguments passed: 2 integer numbers (operands) and a specific operator as string ('-', '+', '*', '/').
The function then executes the corresponding operation and prints the result to the console.
In the case of a division by 0, "Division by 0 is not allowed." is printed on the console. 
If an invalid operator is passed, "Invalid operator." is printed.
Make use of type hints when declaring the function.

Example calls of function:
calculate(3, 4, "+") >> 7

calculate(2, 8, "-") >> -6

calculate(5, 5, "*") >> 25

calculate(10, 0, "/") >> Division by 0 is not allowed.

calculate(3, 5, "/") >> 0.6

calculate(9, 4, "?") >> Invalid operator.

"""


def calculate(n1: int, n2: int, operator: str):
    if operator == "+":
        print(n1 + n2)
    elif operator == "-":
        print(n1 - n2)
    elif operator == "*":
        print(n1 * n2)
    elif operator == "/":
        if n2 != 0:
            print(n1 / n2)
        else:
            print("Division by 0 is not allowed.")
    else:
        print("invalid operator.")


"""
Reverse Word

Write a function named "reverse_word" which accepts one argument (word) and returns the reversed word. 
Besides reversing the word the first letter of the reversed word should be written with upper case letter, all other letters should be lower case letters.
Make use of type hints when declaring the function.

Example calls of function:
    reverse_word("hello") -> returns "Olleh"
    reverse_word("WORLD") -> returns "Dlrow"
    reverse_word("lEOn") -> returns "Noel"
"""


def reverse_word(word: str) -> str:
    word = word.lower()  # make all letters lower case letters

    reversed = ""

    # using for with len and range
    # range(start, stop, step)
    # start from last index, stop at index -1, always -1 steps
    for i in range(len(word) - 1, -1, -1):
        if i == len(word) - 1:
            reversed += word[i].upper()
        else:
            reversed += word[i]

    # # using a while loop
    # i = len(word) - 1
    # while i >= 0:
    #     if i == len(word) - 1:
    #         reversed += word[i].upper()
    #     else:
    #         reversed += word[i]
    #     i -= 1

    # # using super short form
    # reversed = word[::-1]
    # reversed = reversed[0].upper() + reversed[1:] # capitalizes the first character of the reversed string and retrieves all characters from the second character onwards

    return reversed


if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values.")
    # calculate(3, 4, "+")
    # calculate(2, 8, "-")
    # calculate(5, 5, "*")
    # calculate(10, 0, "/")
    # calculate(3, 5, "/")
    # calculate(9, 4, "?")
    print(reverse_word("hello"))
    print(reverse_word("WORLD"))
    print(reverse_word("lEOn"))
