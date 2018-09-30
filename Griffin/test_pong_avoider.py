
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

import pygame, sys , random
pygame.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

#the game's variables
ball_x = 50
ball_y = 0
ball_radius = 10
ball_color = [222,50,50]
ball_speed_y = 5
ball_speed_x = 0
min_speed = 6
max_speed = 8
paddle_x = 200
paddle_y = 400
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 20
highscore = 0
easy_mode = 0
medium_mode = 0
hard_mode = 0
extreme_mode = 0
score = 0
difficulty = "medium"
myfont = pygame.font.SysFont("Arial", 35)
ballx = [10,58,99,153,204,254,555]
ballz = [0,0,0,0,0,0,0]
speeds = [5,6,7,8,9,10,11]
pygame.key.set_repeat(20, 20)
running = False
gameplay = True

pygame.display.update()
while gameplay:
    while not running:
        pygame.draw.rect(screen, black, [0, 0, 640, 480], 0)
        label = myfont.render("Press Space To Start" , 1, pygame.color.THECOLORS['red'])
        screen.blit(label, (200, 240))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = True
                if event.key == pygame.K_e:
                    ball_color = pygame.color.THECOLORS['green']
                    ballx = [10,153,254,555]
                    ballz = [0,0,0,0]
                    speeds = [5,6,7,6]
                    min_speed = 5
                    max_speed = 7
                    difficulty = "easy"
                if event.key == pygame.K_m:
                    ball_color = pygame.color.THECOLORS['yellow']
                    ballx = [10,58,99,153,204]
                    ballz = [0,0,0,0,0]
                    speeds = [6,7,8,7,7]
                    min_speed = 6
                    max_speed = 8
                    difficulty = "medium"
                if event.key == pygame.K_h:
                    ball_color = pygame.color.THECOLORS['red']
                    ballx = [10,58,99,153,204,254,555]
                    ballz = [0,0,0,0,0,0,0]
                    speeds = [5,6,7,8,9,10,11]
                    min_speed = 5
                    max_speed = 12
                    difficulty = "hard"
                if event.key == pygame.K_x:
                    ball_color = pygame.color.THECOLORS['blue']
                    ballx = [10,58,99,153,204,254,304,354,400,555]
                    ballz = [0,0,0,0,0,0,0,0,0,0]
                    speeds = [7,8,9,10,11,12,14,13,7,7]
                    min_speed = 7
                    max_speed = 14
                    difficulty = "extreme"


#game loop
    while running:
        for event in pygame.event.get():
            #check if you've exited the game
            if event.type == pygame.QUIT:
                running = False

            #check if you pressed a key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_x = paddle_x - paddle_speed
                if event.key == pygame.K_RIGHT:
                    paddle_x = paddle_x + paddle_speed
                if event.key == pygame.K_q:
                    running = False

        #pause for 20 milliseconds
        pygame.time.delay(20)
        #make the screen completely white
        screen.fill(black)

        #move the ball
        for i in range (len(ballz)):
            ballz[i] += speeds[i]
            
        #check if the ball is off the bottom of the screen
        for i in range (len(ballz)):
            if ballz[i] > screen.get_height():
                ballz[i] = 0
                score += 1
                speeds[i] = random.randint(min_speed,max_speed)
                if score >highscore:
                    highscore = score
                if score > easy_mode:
                    easy_mode = score
                if score > medium_mode:
                    medium_mode = score
                if score > hard_mode:
                    hard_mode = score
                if score > extreme_mode:
                    extreme_mode = score
                ballx[i] = random.randint(10,630)
            
            
     
        #bouncing off the right side
        if ball_x > screen.get_width():                                
            ball_speed_x = -ball_speed_x
            
        #bouncing off the left side
        if ball_x < 0:                                
            ball_speed_x = -ball_speed_x
        
        #bouncing off the top
        if ball_y < 0:                                
            ball_speed_y = -ball_speed_y
        for i in range(len(speeds)):
                
                        #create imaginary rectangles around ball and paddle
            ball_rect = pygame.Rect(ballx[i]-ball_radius, ballz[i]-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
            paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
            #see if the rectangles overlap
            if doRectsOverlap(ball_rect, paddle_rect):
                for i in range (len(ballz)):
                    ballz[i] = 0
                #label = myfont.render("Game Over" , 1, pygame.color.THECOLORS['red'])
                #screen.blit(label, (250, 240))
                #label = myfont.render("Wait 10 Seconds To Restart" , 1, pygame.color.THECOLORS['red'])
                #screen.blit(label, (180, 280))
                #pygame.display.update()
                score = 0
        if paddle_x > 580:
            paddle_x = 580
        if paddle_x < 0:
            paddle_x = 0                
        
        if event.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos() #gives (x,y) coordinates
            paddle_x = coordinates[0] #sets the paddle_x variable to the first item in coordinates
            if paddle_x > 580:
                paddle_x = 580
            if paddle_x < 0:
                paddle_x = 0

        
        #draw everything on the screen
        for i in range (len(ballz)):
            pygame.draw.circle(screen, ball_color, [ballx[i],ballz[i]], ball_radius, 0)
        pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)

        label = myfont.render("Score:" + str(score), 1, pygame.color.THECOLORS['red'])
        screen.blit(label, (10, 30))
        if difficulty == "easy":
            label = myfont.render("Highscore:" + str(easy_mode), 1, pygame.color.THECOLORS['red'])
            screen.blit(label, (470, 30))
        if difficulty == "medium":
            label = myfont.render("Highscore:" + str(medium_mode), 1, pygame.color.THECOLORS['red'])
            screen.blit(label, (470, 30))
        if difficulty == "hard":
            label = myfont.render("Highscore:" + str(hard_mode), 1, pygame.color.THECOLORS['red'])
            screen.blit(label, (470, 30))
        if difficulty == "extreme":
            label = myfont.render("Highscore:" + str(extreme_mode), 1, pygame.color.THECOLORS['red'])
            screen.blit(label, (470, 30))
        
        
        #update the entire display
        pygame.display.update()



pygame.quit()

