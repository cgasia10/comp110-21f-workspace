"""allows user to input variables and then demonstrates how different operands would interact with them."""

__author__: str = "730321464"

left: str = input("Left-hand side: ")
right: str = input('Right-hand side: ')
print(left + " ** " + right + " is", int(left) ** int(right))
print(left + " / " + right + " is", int(left) / int(right))
print(left + " // " + right + " is", int(left) // int(right))
print(left + " % " + right + " is", int(left) % int(right))