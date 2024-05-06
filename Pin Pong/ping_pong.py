from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed, width, height):
        self.image = transform.scale(image.load(img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

window = display.set_mode((700,500))
window.fill((200,250,250))

ball = GameSprite('tenis_ball.png', 300,200, 10, 50,50)

game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.reset()

    display.update()
