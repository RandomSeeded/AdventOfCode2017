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
CurrentDirection = Down

# Target = 368078
new_x = 0
new_y = 1
lengthOfCurrentSide = 0
maximumLengthOfCurrentSide = 1
shouldIncreaseLengthOfNextSide = True

for i in range(1, Target+1):
    new_x += CurrentDirection.x_change
    new_y += CurrentDirection.y_change
    print '{} placed at position {}'.format(i, [new_x, new_y])

    # print lengthOfCurrentSide
    # print maximumLengthOfCurrentSide
    lengthOfCurrentSide += 1
    if lengthOfCurrentSide == maximumLengthOfCurrentSide:
        print 'Changing directions'
        CurrentDirection = CurrentDirection.next
        lengthOfCurrentSide = 1
        if shouldIncreaseLengthOfNextSide == True:
            maximumLengthOfCurrentSide = maximumLengthOfCurrentSide + 1 if shouldIncreaseLengthOfNextSide else maximumLengthOfCurrentSide
        shouldIncreaseLengthOfNextSide = not shouldIncreaseLengthOfNextSide
    
