# Tomasz Nowak

def read_positive_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if 0 <= user_input:
                return user_input
            else:
                print("Enter positive float number.")
        except ValueError:
            print("Numbers only please.")


def read_positive_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
        except ValueError:
            print("Whole positive numbers only please.")


def read_non_empty_string(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) > 0 and user_input.isalpha():
            return user_input
