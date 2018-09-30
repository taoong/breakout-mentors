import pygame, sys, random

# Function to check whether a point at (x, y) is inside a rectangle rect
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

# Display
pygame.init()
screen = pygame.display.set_mode([1280,800])
black = [0, 0, 0]

# Each card's variables
card_x = 100
card_y = -100
card_width = 80
card_height = 80
card_color = [20,180,180]
incorrect = False

# A list holding imaginary rectangles for each card to detect clicking
squares = []

# A list storing all the squares that were clicked
clickedSquares = []

# A list storing all the icons
icons = []

iconIndexes = []

# Indexes for icons list, used to check equality
currIcon = -1
prevIcon = -1

# Used in the for loop to fill in the list of icons
iconNumber = range(1, 5) + range(1, 5)

# Storing the coordinates of a mouse click
pos = 0

# Filling the icons list with 2x icon1.png to icon14.png in a random order
for _ in range(8):
    currNumber = iconNumber[random.randint(0, len(iconNumber) - 1)]
    iconIndexes.append(currNumber)
    icons.append(pygame.image.load('icon' + str(currNumber) + '.png'))
    iconNumber.remove(currNumber)
    

# Game loop
running = True
while running:

    for event in pygame.event.get():
        # Check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        # Tracking mouse clicks
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            for square in squares:
                if isPointInsideRect(pos[0], pos[1], square):
                    if square not in clickedSquares:
                        clickedSquares.append(square)
                        currIcon = squares.index(square)
            
                        if prevIcon != -1:
                            if iconIndexes[currIcon] != iconIndexes[prevIcon]: # if matching, keep
                                incorrect = True
                            else:
                                print "correct"
                            prevIcon = -1
                        else:
                            prevIcon = currIcon
                    
                    
                        

    # Refreshing the screen
    pygame.time.delay(20)
    screen.fill(black)

    # Emptying the squares list
    squares = []

    # Keeping track of how to index into the list of icons    
    currentImage = 0

    # Drawing all 28 cards and clicked icons
    for x in range(4): #rows
        card_y += 160
        card_x = 100
        for y in range(2): #columns
            currentRect = pygame.Rect(card_x, card_y, card_width, card_height)
            squares.append(currentRect)

            # Actually drawing the blank card
            pygame.draw.rect(screen, card_color, [card_x, card_y, card_width, card_height], 0)
            

            # Draws icon if the square was clicked
            if currentRect in clickedSquares:
                screen.blit(icons[currentImage], [card_x, card_y])

            card_x += 160
            currentImage += 1
    
    # Resetting where cards are drawn
    card_y = -100

    
    
    if incorrect == True:
        pygame.display.flip()
        clock.tick(1)
        clickedSquares.pop()
        clickedSquares.pop()
        incorrect = False
    # Updating the display
    pygame.display.update()
    
    
pygame.quit()
