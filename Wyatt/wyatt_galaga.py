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
paddle_x = 200
paddle_y = 450
paddle_speed = 10
score = 0

# The lazer variables
lasers = []
laser_speed = 8
laser_width = 5
laser_height = 10
laser_color = [255, 255, 0]

# The Trump variables
trump_x = 50
trump_y = 50
trump_xspeed = random.randint(5, 15)
trump_yspeed = random.randint(5, 15)
trump_stop = 0

trumpus_maximus_x = 300
trumpus_maximus_y = 50
trumpus_maximus_xspeed = random.randint(5, 15)
trumpus_maximus_yspeed = random.randint(5, 15)
trumpus_maximus_stop = 0

# importing images and sprites
derp = pygame.image.load('derp.png')
derp = pygame.transform.scale(derp, (10, 10))
trump = pygame.image.load('trump.jpeg')
trump = pygame.transform.scale(trump, (40, 40))
trump_max = pygame.image.load('trump2.jpg')
trump_max = pygame.transform.scale(trump_max, (40, 40))
myfont = pygame.font.SysFont("Arial", 35)

#pygame.mixer.music.load('freddys.mp3')
#pygame.mixer.music.play(-1)

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

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lasers.append([paddle_x, paddle_y])
                
              
                
    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)    

    #make the paddle phase through the wall
    if paddle_x > screen.get_width():
        paddle_x = -60
    if paddle_x < -60:
        paddle_x = 640
        
        
    # making lasers go up
    for laser in lasers:
        laser[1] -= laser_speed
        
    if trump_stop == 1:
      trump_y = 0
    if trumpus_maximus_stop == 1:
      trumpus_maximus_y = 0
    
    # making Trump move
    if trump_stop <= 0:
      trump_x += trump_xspeed
      trump_y += trump_yspeed
      if trump_y <= 0:
        trump_yspeed = random.randint(1, 15)
      if trump_y >= 481:
        trump_yspeed = random.randint(-15, -1)
        trump_stop = 20
      if trump_x <= 0:
        trump_xspeed = random.randint(3, 15)
      if trump_x >= 600:
        trump_xspeed = random.randint(-15, -3)

    # making Trumpus Maximus move
    if trumpus_maximus_stop <= 0:
      trumpus_maximus_x += trumpus_maximus_xspeed
      trumpus_maximus_y += trumpus_maximus_yspeed
      if trumpus_maximus_y <= 0:
        trumpus_maximus_yspeed = random.randint(1, 15)
      if trumpus_maximus_y >= 481:
        trumpus_maximus_yspeed = random.randint(-15, -1)
        trumpus_maximus_stop = 20
      if trumpus_maximus_x <= 0:
        trumpus_maximus_xspeed = random.randint(3, 15)
      if trumpus_maximus_x >= 600:
        trumpus_maximus_xspeed = random.randint(-15, -3)
    
    trump_stop -= 1
    trumpus_maximus_stop -= 1
    
    
    #create imaginary rectangles
    derp_rectangle = pygame.Rect(paddle_x, paddle_y, 10, 10)
    trump_rectangle = pygame.Rect(trump_x, trump_y, 40, 40)
    trumpus_maximus_rectangle = pygame.Rect(trumpus_maximus_x, trumpus_maximus_y, 40, 40)
    for laser in lasers:
      laser_rectangle = pygame.Rect(laser[0], laser[1], 5, 10)
      if doRectsOverlap(laser_rectangle, trump_rectangle) == True:
          score += 10
          trump_stop = 20
          trump_y = 600
      if doRectsOverlap(laser_rectangle, trumpus_maximus_rectangle) == True:
          score += 20
          trumpus_maximus_stop = 20
          trumpus_maximus_y = 600

    if doRectsOverlap(derp_rectangle, trump_rectangle) == True:
        running = False
        label = myfont.render("Game Over", 1, pygame.color.THECOLORS['red'])
        screen.blit(label, (260, 100))

    if doRectsOverlap(derp_rectangle, trumpus_maximus_rectangle) == True:
        trumpus_maximus_stop = 20
        trumpus_maximus_y = 600

    #draw everything on the screen
    
    #draw derp
    screen.blit(derp, [paddle_x, paddle_y])

    #draw trump
    screen.blit(trump, [trump_x, trump_y])
    screen.blit(trump_max, [trumpus_maximus_x, trumpus_maximus_y])
    
    #draw lasers
    for laser in lasers:
        pygame.draw.rect(screen, laser_color, [laser[0], laser[1], laser_width, laser_height])

    label2 = myfont.render("Score: " + str(score), 1, pygame.color.THECOLORS['white'])
    screen.blit(label2, (460, 20))
    #update the entire display  
    pygame.display.update()
pygame.quit()
