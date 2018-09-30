import pygame, sys, random
pygame.init()

class PongGame(object):
    paddle_x = 210
    paddle_y = 560
    paddle_width = 60
    paddle_height = 20
    paddle_color = [20,180,180]
    paddle_speed = 5
    ball_x = 235
    ball_y = 315
    ball_speed = 3
    ball_color = [255, 255, 255]
    score1 = 0
    score2 = 0
    enemy_x = 210
    myfont = pygame.font.SysFont("Arial", 35)
    
    def __init__(self):
        self.screen = pygame.display.set_mode([480,640])
        self.black = [0, 0, 0]
        self.ball_rect = pygame.Rect(self.ball_x, self.ball_y, 10, 10)
        self.paddle_rect = pygame.Rect(self.paddle_x, self.paddle_y, self.paddle_width, self.paddle_height) 
        self.enemy_rect = pygame.Rect(self.ball_x, 60, self.paddle_width, self.paddle_height)
        if random.randint(0,1) == 1:
            self.ball_speed_x = self.ball_speed
        else:
            self.ball_speed_x = -self.ball_speed
        if random.randint(0,1) == 1:
            self.ball_speed_y = self.ball_speed
        else:
            self.ball_speed_y = -self.ball_speed

    def doRectsOverlap(self, rect1, rect2):
        for a, b in [(rect1, rect2), (rect2, rect1)]:
            # Check if a's corners are inside b
            if ((self.isPointInsideRect(a.left, a.top, b)) or
                (self.isPointInsideRect(a.left, a.bottom, b)) or
                (self.isPointInsideRect(a.right, a.top, b)) or
                (self.isPointInsideRect(a.right, a.bottom, b))):
                return True
        return False

    def isPointInsideRect(self, x, y, rect):
        if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
            return True
        else:
            return False
            
    def move(self, direction):
        if direction == 1 and self.paddle_x <= 480 - self.paddle_width:
            self.paddle_x += self.paddle_speed
        elif direction == 0 and self.paddle_x >= 0:
            self.paddle_x -= self.paddle_speed
        self.paddle_rect = pygame.Rect(self.paddle_x, self.paddle_y, self.paddle_width, self.paddle_height)
            
    def ballMove(self):
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y
        if self.ball_x <= 0:
            self.ball_speed_x = self.ball_speed
        elif self.ball_x >= 470:
            self.ball_speed_x = -self.ball_speed

        if self.doRectsOverlap(self.ball_rect, self.paddle_rect):
            self.ball_speed_y = -self.ball_speed
        if self.doRectsOverlap(self.ball_rect, self.enemy_rect):
            self.ball_speed_y = self.ball_speed

        self.ball_rect = pygame.Rect(self.ball_x, self.ball_y, 10, 10)

        if self.ball_y < -10:
            self.score1 += 1
            self.ballReset(1)
        if self.ball_y > 640:
            self.score2 += 1
            self.ballReset(2)

    def enemyMove(self):
        if self.ball_x > self.enemy_x + self.paddle_width // 2:
            self.enemy_x += self.ball_speed - 0
        else:
            self.enemy_x -= self.ball_speed - 0
        self.enemy_rect = pygame.Rect(self.ball_x, 60, self.paddle_width, self.paddle_height)

    def ballReset(self, who):
        self.ball_x = 235
        self.ball_y = 315
        if random.randint(0,1) == 1:
            self.ball_speed_x = self.ball_speed
        else:
            self.ball_speed_x = -self.ball_speed
        if who == 1:
            self.ball_speed_y = -self.ball_speed
        else:
            self.ball_speed_y = self.ball_speed

    def run(self):
        while 1:
            self.screen.fill(self.black)
            for event in pygame.event.get():
            #check if you've exited the game
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.move(0)
            if keys[pygame.K_RIGHT]:
                self.move(1)

            self.enemyMove()
            self.ballMove()
            
            pygame.draw.rect(self.screen, self.paddle_color, [self.enemy_x, 60, self.paddle_width, self.paddle_height], 0)
            pygame.draw.rect(self.screen, self.paddle_color, [self.paddle_x, self.paddle_y, self.paddle_width, self.paddle_height], 0)
            pygame.draw.rect(self.screen, self.ball_color, [self.ball_x, self.ball_y, 10, 10], 0)
            label = self.myfont.render(str(self.score2), 1, pygame.color.THECOLORS['white'])
            self.screen.blit(label, (20, 300))
            label = self.myfont.render(str(self.score1), 1, pygame.color.THECOLORS['white'])
            self.screen.blit(label, (20, 340))

            pygame.display.update()
            
if __name__ == '__main__':
    App = PongGame()
    App.run()
