import argparse


def add_two_digits(a, b):

    return a + b


if __name__ == "__main__":

    print(add_two_digits(5, 5))

    parser = argparse.ArgumentParser(
        description="Add two numbers together."
    )

    # * Add positional arguments
    parser.add_argument('a', type=float, help="first number")
    parser.add_argument("b", type=float, help="second number")

    args = parser.parse_args()

    print(args)
