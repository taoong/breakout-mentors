import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

#the game's variables

Pperyrus = 100

myfont = pygame.font.SysFont("Arial", 35)

papyrus = pygame.image.load('papyrus.jpg')
papyrus_draw = pygame.transform.scale(papyrus, (Pperyrus, Pperyrus))

muth_equakson = 550
maht_quesione = 400
Madfha = 5
Dadfha = 5

running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
                
    muth_equakson -= Madfha
    maht_quesione -= Dadfha
    Pperyrus -= 2
    if Pperyrus < 2:
      Pperyrus = 100
      if muth_equakson < 320 and maht_quesione < 240:
        
        Madfha = -5
        Dadfha = -5
        
      if muth_equakson < 320 and maht_quesione > 240:
        
        Madfha = -5
        Dadfha = 5
        
      if muth_equakson > 320 and maht_quesione < 240:
        
        Madfha = 5
        Dadfha = -5
        
      if muth_equakson > 320 and maht_quesione > 240:
        
        Madfha = 5
        Dadfha = 5
    papyrus_draw = pygame.transform.scale(papyrus, (Pperyrus, Pperyrus))
    
      

    
    pygame.time.delay(0)
    
    #make the screen completely white
    screen.fill(black)        

    #draw everything on the screen
    screen.blit(papyrus_draw, [muth_equakson, maht_quesione])
    #update the entire display
    pygame.display.update()

pygame.quit()
  
