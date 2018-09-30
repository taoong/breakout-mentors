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

import random
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
white = [255, 255, 255]

#the game's variables
car_x = 500
car_y = 300
car_speed = 5
duck_x = 50
duck_y = 300
gravity = []
score = 0

car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (80, 60))
duck = pygame.image.load('duck.png')
duck = pygame.transform.scale(duck, (60, 60))
sun = pygame.image.load('sun.png')
sun = pygame.transform.scale(sun, (100, 100))
ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, (900, 150))

pygame.mixer.music.load('duck.mp3')
pygame.mixer.music.play(-1)

myfont = pygame.font.SysFont("Zapf Dingbats", 35)

running = True

#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if duck_y == 300:
                    gravity = [-10, -10, -10, -10, -8, -8, -8, -8, -6, -6, -6, -6,
                               -4, -4, -4, -4, -2, -2, -2, -2, 0, 2, 2, 2, 2,
                               4, 4, 4, 4, 6, 6, 6, 6,
                               8, 8, 8, 8,
                               10, 10, 10, 10]
                
    #make the screen completely white
    screen.fill(white)

    #game logic

    #adding the score
    score += 1

    if score == 150 or score == 300 or score == 500 or score == 750 or score == 1000:
        car_speed += 1
    
    #moving the car
    if car_x <= -80:
        car_x = 680
    car_x = car_x - car_speed

    #making the duck jump
    if len(gravity) > 0:
        currentGravity = gravity.pop()
        duck_y = duck_y - currentGravity

    #create imaginary rectangles
    duck_rectangle = pygame.Rect(duck_x, duck_y, 50, 61)
    car_rectangle = pygame.Rect(car_x, car_y, 80, 60)

    if doRectsOverlap(duck_rectangle, car_rectangle) == True:
        running = False
        label = myfont.render("Game Over", 1, pygame.color.THECOLORS['black'])
        screen.blit(label, (260, 100))
        

            
    #draw everything on the screen
    pygame.draw.rect(screen, [125,125,125], [0, 330, 640, 150], 0)
    screen.blit(ground, [0, 285])
    screen.blit(car, [car_x, car_y])
    screen.blit(duck, [duck_x, duck_y])
    screen.blit(sun, [0, 0])
    label2 = myfont.render("Score: " + str(score), 1, pygame.color.THECOLORS['black'])
    screen.blit(label2, (460, 20))
    
    #update the entire display
    pygame.display.update()
pygame.quit()


