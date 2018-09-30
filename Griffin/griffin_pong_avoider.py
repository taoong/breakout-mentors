

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
ball_x = 50
ball_y = 0
ball_radius = 10
ball_color = "white"
ball_speed_y = 20
ball_speed_x = 0

paddle_x = 200
paddle_y = 440
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 20

highscore_e = 0
highscore_m = 0
highscore_h = 0
highscore_x = 0
score = 0

myfont = pygame.font.SysFont("Arial", 35)

x = [10, 38, 77, 188, 364, 399]
y = [0, 0, 0, 0, 0, 0]
speeds = [15, 16, 17, 18, 19, 20]

min_speed = 15
max_speed = 20
difficulty = "m"

running = False
gameplay = True

while gameplay:
    while not running:
        pygame.draw.rect(screen, pygame.color.THECOLORS['black'], [0, 0, 640, 480], 0)
        label = myfont.render("PRESS THE SPACEBAR TO START", 1, pygame.color.THECOLORS['white'])
        screen.blit(label, (120, 200))
        label = myfont.render("Highscores:", 1, pygame.color.THECOLORS['white'])
        screen.blit(label, (220, 250))
        label = myfont.render("Easy: " + str(highscore_e), 1, pygame.color.THECOLORS['green'])
        screen.blit(label, (220, 275))
        label = myfont.render("Medium: " + str(highscore_m), 1, pygame.color.THECOLORS['yellow'])
        screen.blit(label, (220, 300))
        label = myfont.render("Hard: " + str(highscore_h), 1, pygame.color.THECOLORS['orange'])
        screen.blit(label, (220, 325))
        label = myfont.render("Expert: " + str(highscore_x), 1, pygame.color.THECOLORS['red'])
        screen.blit(label, (220, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = True
                if event.key == pygame.K_e:
                    x = [10, 38, 77, 188]
                    y = [0, 0, 0, 0]
                    speeds = [15, 16, 17, 18]
                    min_speed = 15
                    max_speed = 18
                    difficulty = "e"
                    ball_color = "green"
                if event.key == pygame.K_m:
                    x = [10, 38, 77, 188, 364, 399]
                    y = [0, 0, 0, 0, 0, 0]
                    speeds = [15, 16, 17, 18, 19, 20]
                    min_speed = 15
                    max_speed = 20
                    difficulty = "m"
                    ball_color = "yellow"
                if event.key == pygame.K_h:
                    x = [10, 38, 77, 188, 364, 399, 470, 591]
                    y = [0, 0, 0, 0, 0, 0, 0, 0]
                    speeds = [15, 16, 17, 18, 19, 20, 21, 22]
                    min_speed = 15
                    max_speed = 22
                    difficulty = "h"
                    ball_color = "orange"
                if event.key == pygame.K_x:
                    x = [10, 38, 77, 188, 364, 399, 470, 591, 610, 630]
                    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    speeds = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                    min_speed = 15
                    max_speed = 24
                    difficulty = "x"
                    ball_color = "red"

    #game loop
    while running:
        for event in pygame.event.get():
            #check if you've exited the game
            if event.type == pygame.QUIT:
                gameplay = False

            #check if you pressed a key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_x = paddle_x - paddle_speed
                if event.key == pygame.K_RIGHT:
                    paddle_x = paddle_x + paddle_speed
                if event.key == pygame.K_q:
                    score = 0
                    running = False

        #pause for 20 milliseconds
        pygame.time.delay(20)
        #make the screen completely white
        screen.fill(black)

        #move the ball
        for i in range(len(speeds)):
            y[i] += speeds[i]
        #check if the ball is off the bottom of the screen
        for i in range(len(speeds)):
            if y[i] > screen.get_height():
                y[i] = 0
                x[i] = random.randint(10, 630)
                speeds[i] = random.randint(min_speed, max_speed)
                score += 1
                if difficulty == "e":
                    if score > highscore_e:
                        highscore_e = score
                if difficulty == "m":
                    if score > highscore_m:
                        highscore_m = score
                if difficulty == "h":
                    if score > highscore_h:
                        highscore_h = score
                if difficulty == "x":
                    if score > highscore_x:
                        highscore_x = score
        #bouncing off the right side
        if ball_x > screen.get_width():                                
            ball_speed_x = -ball_speed_x
            
        #bouncing off the left side
        if ball_x < 0:                                
            ball_speed_x = -ball_speed_x
        
        #bouncing off the top
        if ball_y < 0:                                
            ball_speed_y = -ball_speed_y
        
        #see if the rectangles overlap
        if paddle_x > 580:
            paddle_x = 580
        if paddle_x < 0:
            paddle_x = 0

        for i in range(len(speeds)):
            #create imaginary rectangles around ball and paddle
            ball_rect = pygame.Rect(x[i]-ball_radius, y[i]-ball_radius, ball_radius*2,ball_radius*2)
            #circles are measured from the center, so have to subtract 1 radius from the x and y
            paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
            if doRectsOverlap(ball_rect, paddle_rect):
                pygame.draw.rect(screen, pygame.color.THECOLORS['black'], [0, 0, 640, 480], 0)
                label = myfont.render("GAME OVER", 1, pygame.color.THECOLORS['red'])
                screen.blit(label, (250, 250))
                for i in range(len(speeds)):
                    y[i] = 0
                pygame.display.flip()
                pygame.time.delay(1000)
                pygame.display.update()
                score = 0
        if event.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos() #gives (x,y) coordinates
            paddle_x = coordinates[0] #sets the paddle_x variable to the first item in coordinates

        
        #draw everything on the screen
        
        pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
        for i in range(len(speeds)):
            pygame.draw.circle(screen, pygame.color.THECOLORS[ball_color], [x[i], y[i]], ball_radius, 0)
        label = myfont.render("Score: " + str(score), 1, pygame.color.THECOLORS['white'])
        screen.blit(label, (20, 30))
        if difficulty == "e":
            highscore = highscore_e
        if difficulty == "m":
            highscore = highscore_m
        if difficulty == "h":
            highscore = highscore_h
        if difficulty == "x":
            highscore = highscore_x
        label = myfont.render("Highscore: " + str(highscore), 1, pygame.color.THECOLORS['white'])
        screen.blit(label, (460, 30))

        #update the entire display
        pygame.display.update()



pygame.quit()



    

    

