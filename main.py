from pygame import *
from random import choice

class GameSprite(sprite.Sprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def collidepoint(self, x,y):
       return self.rect.collidepoint(x,y)

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>10:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<450-10- self.rect.width:
            self.rect.y+=self.speed
    
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>10:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<450-10- self.rect.width:
            self.rect.y+=self.speed

class Ball(GameSprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__(img, x,y, w,h, speed)
        self.direct = [0,0]

    def update(self):
        global score_l, score_r
        self.rect.x += self.speed*self.direct[0]
        self.rect.y += self.speed*self.direct[1]
        if self.rect.y <=0 or self.rect.y>=500-self.rect.height:
            self.direct[1] *= -1
        #if self.rect.x <=0 or self.rect.x>=700-self.rect.height:
            #self.direct[0] *= -1
        if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            self.direct[0] *= -1
        if self.rect.x <=0:
            score_r += 1
            self.start()
        if self.rect.x>=700-self.rect.width:
            score_l += 1
            self.start()


    def start(self):
        self.rect.x = 325
        self.rect.y = 225
        ball.direct[0] = choice([-1,1])
        ball.direct[1] = choice([-1,1])

window = display.set_mode((700,500))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('fon.jpg'), (700,500))

mixer.init()
mixer.music.load('gta.mp3')
mixer.music.play()

player1 = Player1('obz.png', 50,250,68, 100, 10)
player2 = Player2('obz2.png', 600,215,68, 100, 10)
ball = Ball('ball.png', 350-25, 250-25, 50,50,5)
ball.direct[0] = choice([-1,1])
ball.direct[1] = choice([-1,1])
game = True
score_r = 0
score_l = 0
rule = 3
clock = time.Clock()
FPS = 40

while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.update()
    player1.reset()

    player2.update()
    player2.reset()
    
    ball.update()
    ball.reset()

    clock.tick(FPS)
    display.update()