# thoughts on how to approach?
# 1: we can create the actual spiral. It's doable.
# Alternately: is there not a better approach we can take? The question is:
# How many rows away are we from the center? How many columns away from the center are we?

# We don't actually need to create the spiral in memory. We just need to know our position relative to the center. So we create the spiral and keep track of our index until we find that position and then we're done

# Target = 5
# # Target = 368078
# 
# CurrentDirection = Down
# NumPlaced = 1
# lastStep = 0
# x_pos = 0
# y_pos = 0

# Place all but the very last row
# OK THE NAVIGATION HERE IS REALLY COMPLICATED
# YOU NEED TO KEEP TRACK OF:
# - what length of the side of the spiral is next? (Increases by 1 every time)
# - what value will I place at that? (Previous value of the this value + the next length of the spiral)
# So the pattern is:
# [1, 1] -> value 1 gets implemented for spiral of length 1
# [2, 2] -> value 1 is next for spiral with side length 2
# [3, 3] -> value 3 is next for spiral with side length 3? No, wrong. Value is next for spiral with side length of ALSO 2. (What??)
# Ahhhhhh...this is because I was remembering the spiral with space, which this is not.
# There's an additional level of complexity here: you only grow the spiral when you go left or right, not up or down.

# while NumPlaced + (lastStep + 1) < Target:
#     print lastStep
#     x_pos += lastStep * CurrentDirection.x_change
#     y_pos += lastStep * CurrentDirection.y_change
#     NumPlaced += lastStep
#     print [x_pos, y_pos]
#     lastStep += 1
#     CurrentDirection = CurrentDirection.next

# Find the position of the last element
# FinalStep = Target - NumPlaced
# x_pos += FinalStep * CurrentDirection.x_change
# y_pos += FinalStep * CurrentDirection.y_change
# print '--- FINAL POS: {}'.format([x_pos, y_pos])


# Yeah I'm bored and went the inefficient easy way out

x = 0
y = 0

# Hey this would be a nice time for a circular linked list

class ListNode:
    def __init__(self, name, x_change, y_change):
        self.name = name
        self.x_change = x_change
        self.y_change = y_change

Right = ListNode('Right', +1, 0)
Up = ListNode('Up', 0, 1)
Left = ListNode('Left', -1, 0)
Down = ListNode('Down', 0, -1)

Right.next = Up
Up.next = Left
Left.next = Down
Down.next = Right

Target = 25
# # Target = 368078

nextStep = 0
CurrentDirection = Down
lastChangedDirectionAt = 0

for i in range(Target):
    print CurrentDirection.name
    if (lastChangedDirectionAt + i) == nextStep:
        print '*****'
        nextStep = nextStep + 1
        CurrentDirection = CurrentDirection.next
        lastChangedDirectionAt = i
    print i

