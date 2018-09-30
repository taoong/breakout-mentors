def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False

#used the by the doRectsOverlap function (won't be called directly from game code)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False



import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

#the game's variables
ball_x = 300
ball_y = 300
ball_radius = 10
ball_color = [222,50,50]
ball_speed_x = 3
ball_speed_y = 5
squares = [[300, 300, 5, -7]]

paddle_x = 200
paddle_y = 440
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 20

score = 0
highscore = 0

myfont = pygame.font.SysFont("Zapf Dingbats", 35)

#drawing bricks
brick_x = 0
brick_y = 0
red = 255
green = 255
blue = 205
bricks = []
for i in range(4):
    brick_x = 0
    for j in range(10):
        bricks.append(pygame.Rect(brick_x, brick_y, 63, 29))
        brick_x += 64
    brick_y += 30
    red -= 20
    green -= 20
    blue -= 20

running = True
#game loop
while running:
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_LEFT]:
        paddle_x = paddle_x - paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x = paddle_x + paddle_speed
        
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False
                

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)

    for square in squares:
        #move the ball
        square[1] = square[1] + square[3]
        square[0] = square[0] + square[2]

        #bounce
        if square[0] > screen.get_width() - 10 or square[0] < 0:
            square[2] = -square[2]
        if square[1] < 0:
            square[3] = -square[3]
            score += 1
            if score > highscore:
                highscore = score
    
        #check if the ball is off the bottom of the screen
        if square[1] > screen.get_height():
            label2 = myfont.render("Loser, also press R to restart loser!", 1, pygame.color.THECOLORS['red']) 
            screen.blit(label2, (140, 240))
            pygame.display.update()
            pygame.mixer.music.load('darkness.mp3')
            pygame.mixer.music.play(-1)
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for sq in squares:
                        sq[1] = 300
                        sq[3] = -7
                    score = 0
                    pygame.mixer.music.stop()
    

    #make the paddle phase through the wall
    if paddle_x > screen.get_width():
        paddle_x = -60
    if paddle_x < -60:
        paddle_x = 640

    #create imaginary rectangles around ball and paddle
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    for square in squares:
        ball_rect = pygame.Rect(square[0], square[1], 10, 10)
        #see if the rectangles overlap
        if doRectsOverlap(ball_rect, paddle_rect):
           square[3] = -square[3]
    

    #draw everything on the screen
    
    #drawing bricks

    for brick in bricks:
        if doRectsOverlap(ball_rect, brick):
            bricks.remove(brick)
            squares[0][3] = -squares[0][3]
    
    for brick in bricks:
        pygame.draw.rect(screen, [red, green, blue], [brick.x, brick.y, 63, 29], 0)
        
    for square in squares:
        pygame.draw.rect(screen, ball_color, [square[0], square[1], 10, 10], 0)
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    label = myfont.render("Score: " + str(score), 1, pygame.color.THECOLORS['blue']) 
    screen.blit(label, (460, 20))
    label = myfont.render("Highscore: " + str(highscore), 1, pygame.color.THECOLORS['blue']) 
    screen.blit(label, (200, 20))


    
    #update the entire display
    pygame.display.update()
