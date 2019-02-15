from test_framework import generic_test

# use stack to store integers
# when operator found, then pop the last two integers apply and repush result
# when the expression is done, pop the final result from the stack
# O(n) time complexity O(n) space
def evaluate(expression: str) -> int:
    stack = []
    for i in expression.split(","):
        if i in "+-*/":
            right: int = stack.pop()
            left: int = stack.pop()
            result: int = 0
            if i == "+":
                result = left + right
            if i == "-":
                result = left - right
            if i == "*":
                result = left * right
            if i == "/":
                result = left // right
            stack.append(result)
        else:
            stack.append(int(i))

    return stack.pop()


# solution from book
# clever use of dict and lambda values
def evaluate(expression):

    intermediate_results = []
    DELIMITER = ","
    OPERATORS = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "*": lambda y, x: x * y,
        "/": lambda y, x: int(x / y),
    }

    for token in expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(
                OPERATORS[token](intermediate_results.pop(), intermediate_results.pop())
            )
        else:  # token is a number.
            intermediate_results.append(int(token))
    return intermediate_results[-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate)
    )
