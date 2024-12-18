# Type hints make your code explicitly readable to humans, not just the IDE.
# Without type hints, someone reading your code might not immediately understand what types are expected, especially for functions. This is particularly important in collaborative projects or open-source contributions.

# Example:
# Without type hints:
def process(data):
    # What is 'data'? A list? A dictionary? A string? It's unclear.
    return len(data)

# With type hints:
from typing import List

def process(data: List[int]) -> int:
    # Now it's clear that 'data' is a list of integers, and the function returns an integer.
    return len(data)
