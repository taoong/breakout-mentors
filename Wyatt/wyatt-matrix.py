#setup
import pygame, random
pygame.init()
screen = pygame.display.set_mode((640,640))



screen.fill(pygame.color.THECOLORS['black'])
def one(x, y):
    pygame.draw.line(screen,[0,255,0],(x,y),(x,y+10))
    pygame.draw.line(screen,[0,255,0],(x,y),(x-3,y+3))

def zero(x, y):
    pygame.draw.line(screen,[0,255,0],(x,y),(x,y+10))
    pygame.draw.line(screen,[0,255,0],(x,y),(x+5,y))
    pygame.draw.line(screen,[0,255,0],(x,y+10),(x+5,y+10))
    pygame.draw.line(screen,[0,255,0],(x+5,y),(x+5,y+10))

for i in range(1000):
    one(random.randint(0, 640), random.randint(0, 640))
    zero(random.randint(0, 640), random.randint(0, 640))    

pygame.display.flip()


#closing the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
