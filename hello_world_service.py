def print_message(message):
    print(message)


def sum_numbers(num_a, num_b):
    return num_a + num_b


def difference(num_a, num_b):
    return num_a - num_b


def multiplication(num_a, num_b):
    return num_a * num_b


def divition(num_a, num_b):
    try:
        return num_a / num_b
    except ZeroDivisionError as e:
        print("Divison by 0 is not allowed")


if __name__ == '__main__':
    print_message('Hello, I love you!')
