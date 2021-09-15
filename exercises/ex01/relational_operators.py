"""shows user how operational operands function based on two inputs."""

__author__: str = "730321464"

left_hand_number: str = input("Left-hand side: ")
right_hand_number: str = input("Right-hand side: ")
print(left_hand_number + " < " + right_hand_number + " is", int(left_hand_number) < int(right_hand_number))
print(left_hand_number + " >= " + right_hand_number + " is", int(left_hand_number) >= int(right_hand_number))
print(left_hand_number + " == " + right_hand_number + " is", int(left_hand_number) == int(right_hand_number))
print(left_hand_number + " != " + right_hand_number + " is", int(left_hand_number) != int(right_hand_number))