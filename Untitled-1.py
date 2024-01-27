
from pygame import*
window = display.set_mode((700,500))
display.set_caption(("пендбол"))
window.fill((0,255,191))
polt = True
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y,player_speed,width,hanging):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.hanging = hanging
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class player(GameSprite):
    def polter_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed



           
while polt:
    clock.tick(FPS)
    display.update()
