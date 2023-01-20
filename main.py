"""Example Class
    black Tutorial
    black installed
    black . -l79    -   -l79 means, how many characters should be in one line, to go back to 99 need
    to delete trailing comma

    """


class MyClass:
    def display_info(
        self, name: str, age: int | float, description: str | None = None
    ) -> str:
        return f"Name: {name} * Age: {age} * Description: {description}"


def add_numbers(
    num1: int,
    num2: int,
) -> int:
    return num1 + num2


text = 'This is "some" text.'

# fmt: off
letters = ("alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa")
# fmt: on

letters = (
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "zeta",
    "eta",
    "theta",
    "iota",
    "kappa",
)
