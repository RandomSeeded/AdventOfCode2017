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

# Target = 1024
Target = 368078
# Target = 12

CurrentDirection = Down

new_x = 0
new_y = 1
lengthOfCurrentSide = 0
maximumLengthOfCurrentSide = 1
shouldIncreaseLengthOfNextSide = True

for i in range(1, Target+1):
    new_x += CurrentDirection.x_change
    new_y += CurrentDirection.y_change
    # print '{} placed at position {}'.format(i, [new_x, new_y])

    lengthOfCurrentSide += 1
    if lengthOfCurrentSide == maximumLengthOfCurrentSide:
        # print 'Changing directions'
        CurrentDirection = CurrentDirection.next
        lengthOfCurrentSide = 1
        if shouldIncreaseLengthOfNextSide == True:
            maximumLengthOfCurrentSide = maximumLengthOfCurrentSide + 1 if shouldIncreaseLengthOfNextSide else maximumLengthOfCurrentSide
        shouldIncreaseLengthOfNextSide = not shouldIncreaseLengthOfNextSide
    
numSteps = abs(new_x) + abs(new_y)
print 'numSteps: {}'.format(numSteps)

print '-------------- part 2 ---------------'

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

# Target = 1024
# Target = 368078
# Target = 5
Target = 368078

new_x = 0
new_y = 1
lengthOfCurrentSide = 0
maximumLengthOfCurrentSide = 1
shouldIncreaseLengthOfNextSide = True
spiral = {}
new_value = 0
while (new_value <= Target):
    new_x += CurrentDirection.x_change
    new_y += CurrentDirection.y_change
    new_value = 0
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            nearby_value = spiral.get((new_x + x_offset, new_y + y_offset))
            new_value += nearby_value if nearby_value else 0
    new_value = new_value if new_value != 0 else 1
    spiral[(new_x, new_y)] = new_value

    lengthOfCurrentSide += 1
    if lengthOfCurrentSide == maximumLengthOfCurrentSide:
        # print 'Changing directions'
        CurrentDirection = CurrentDirection.next
        lengthOfCurrentSide = 1
        if shouldIncreaseLengthOfNextSide == True:
            maximumLengthOfCurrentSide = maximumLengthOfCurrentSide + 1 if shouldIncreaseLengthOfNextSide else maximumLengthOfCurrentSide
        shouldIncreaseLengthOfNextSide = not shouldIncreaseLengthOfNextSide
print 'first value larger than target {}'.format(new_value)

# This requires actually writing the squares to memory. That sucks
# Also it will probably have 9x as bad runtime in order to get all the values from the surrounding squares
# So biggest question with that is: where do you start? If you try to use arrays as your structure it's going to be really fucking annoying
# You can use a dict of dicts though probably. Tuple representing the index is the key


