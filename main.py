from pygame import *
from random import randint

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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>10:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x<700-10- self.rect.width:
            self.rect.x+=self.speed
    


window = display.set_mode((700,500))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('fon.jpg'), (700,500))

mixer.init()
mixer.music.load('gta.mp3')
mixer.music.play()

player = Player('cool.jpg', 316,400,68, 100, 5)

game = True

clock = time.Clock()
FPS = 40

while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    player.reset()
    
    clock.tick(FPS)
    display.update()