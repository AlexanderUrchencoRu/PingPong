from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_up(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_down(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

font.init()
font1 = font.Font(None, 30)
win = display.set_mode((700, 500))
lose1 = font1.render('Поражение! Игрок 1 проиграл...', True, (0, 0, 0))
lose2 = font1.render('Поражение! Игрок 2 проиграл...', True, (0, 0, 0))

user1 = Player('rocket1.png', 30, 200, 10, 80, 100)
user2 = Player('rocket3.png', 600, 200, 10, 80, 100)
ball = GameSprite('machik.png', 300, 200, 10, 20, 20)

display.set_caption("Пинг Понг")
background = (0, 78, 9)

clock = time.Clock()

win.fill(background)
game_over = True
finish = False

speed_x = 4
speed_y = 6

while game_over:
    for e in event.get():
        if e.type == QUIT:
            game_over = False

    if not(finish):
        win.fill(background)
        user1.update_down()
        user2.update_up()

        user1.reset()
        user2.reset()
        ball.reset()


        if ball.rect.y > 470 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x > 700 or ball.rect.x < 0:
            speed_x *= -1

        if sprite.collide_rect(user1, ball) or sprite.collide_rect(user2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.x < 0:
            win.blit(lose1, (200, 200))
            finish = True

        if ball.rect.x > 665:
            win.blit(lose2, (200, 200))
            finish = True

        ball.rect.y += speed_y
        ball.rect.x += speed_x

    else:
        finish = False
        ball.rect.x = 300
        ball.rect.y = 200
        speed_x = 4
        speed_y = 4
        user1.rect.y = 200
        user2.rect.y = 200
        time.delay(3000)

    display.update()
    clock.tick(60)