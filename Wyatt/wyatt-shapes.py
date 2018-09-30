#setup
import pygame, random
pygame.init()
screen = pygame.display.set_mode((640,640))



screen.fill(pygame.color.THECOLORS['white'])
def one(x, y):
    pygame.draw.line(screen,[0,255,0],(x,y),(x,y+10))
    pygame.draw.line(screen,[0,255,0],(x,y),(x-3,y+3))

def zero(x, y):
    pygame.draw.line(screen,[0,255,0],(x,y),(x,y+10))
    pygame.draw.line(screen,[0,255,0],(x,y),(x+5,y))
    pygame.draw.line(screen,[0,255,0],(x,y+10),(x+5,y+10))
    pygame.draw.line(screen,[0,255,0],(x+5,y),(x+5,y+10))

def stickboy(x, y):
    pygame.draw.circle(screen, [0,0,0], (x+1, y-4), 5) 
    pygame.draw.line(screen,[0,0,0],(x,y),(x,y+10))
    pygame.draw.line(screen,[0,0,0],(x-3,y+4),(x+3,y+4))
    pygame.draw.line(screen,[0,0,0],(x,y+10),(x-3,y+15))
    pygame.draw.line(screen,[0,0,0],(x,y+10),(x+3,y+15))

def rects(y):
    x = 0
    for i in range(10):
        pygame.draw.rect(screen, [255, 255, 0], [x, y, 50, 10])
        x += 64

pygame.draw.rect(screen, [90, 90, 90], [0, 200, 640, 200])
rects(300)

for i in range(100):
    stickboy(random.randint(0, 640), random.randint(200, 380)) 

pygame.display.flip()


#closing the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
