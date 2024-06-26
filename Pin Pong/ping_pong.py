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


ball = GameSprite('tenis_ball.png', 300, 200, 10, 50,50)
player1 = GameSprite('racket.png', 0, 200, 10, 50,150)
player2 = GameSprite('racket.png', 650, 200, 10, 50,150)

speed_x = 10
speed_y = 10

font.init()
font = font.Font(None,40)
lose1 = font.render('Победил второй игрок',True,(255,255,255))
lose2 = font.render('Победил первый игрок',True,(255,255,255))

game = True
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:

        window.fill((200,250,250))

        player1.reset()
        player2.reset()


        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        keys = key.get_pressed()
        if keys[K_UP]:
            player1.rect.y -= player1.speed
        if keys[K_DOWN]:
            player1.rect.y += player1.speed

        if ball.rect.y > 450 or ball.rect.y < 0 :
            speed_y *= -1

        if ball.rect.x > 650  or ball.rect.x < 0 :
            speed_x *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            window.blit(lose1,(200,200))
            finish = True

        if ball.rect.x > 650:
            window.blit(lose2,(200,200))
            finish = True


        if player2.rect.y > ball.rect.y:
            player2.rect.y -= 5
        else:
            player2.rect.y += 5

        display.update()
    else:
        finish = False

