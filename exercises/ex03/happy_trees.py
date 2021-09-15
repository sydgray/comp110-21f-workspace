"""Drawing forests in a loop."""

__author__ = "751000940"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
result: str = ""
i: int = 0
while i < depth:
    if depth > 0:
        print(TREE + result)
        result = result + TREE
    depth = depth - 1
depth = depth - 1