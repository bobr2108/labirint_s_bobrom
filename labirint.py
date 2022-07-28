from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed <0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed >0:
            for p in platforms_touched:
              self.rect.right = min(self.rect.left, p.rect.right)
        elif self.x_speed <0:
            for p in platforms_touched:
        self.rect.left = max(self.rect.left, p.rect.right)
    if packman.rect.y <= win_heidht-80 and packman.y_speed > 0 or packman.rect.y >=0 and packman.y_speed<0:
      self.rect.x += self.x_speed
    platforms_touched = sprite.spritecollide(self, barriers, False)
    if self.y_speed >0:
      for p in platforms_touched:
        self.rect.bottom = min(self.rect.bottom, p.rect.top)
    elif self.y_speed < 0:
      for p in platforms_touched:
        self.rect.top = max(self.rect.top, p.rect.bottom)
  def fire(self):
    bullet = Bullet('bullet.png', self.rect.rignt, self.rect.centery, 15, 20, 15)
    bullets.add(bullet)

class Enemy(GameSprite):

  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
    GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
    self.speed = player_speed
    self.side = "left"

  def update(self):
    if self.rect.x <= 420:
      self.side = "right"
    if self.rect.x >= win_width -85:
      self.side = "left"
    if self.side == "left":
      self.rect.x -= self.speed 
    else:
      self.rect.x += self.speed

class Bullet(GameSprite):
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
    GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
    self.speed = player_speed

  def update(self):
    self.rect.x += self.speed
    if self.rect.x > win_windth+10:
      self.kill()



win_width=700
win_heidht=500
display.set_caption('Лабиринт')
window = display.set_mode((win_width, win_heidht))
back = (119, 210, 223)

barriers= spirte.Group()

bullets = sprite.Group()

monsters = sprite.Group()
w1 = GameSprite('stone.png', win_width / 2 - win_width / 3, win_heidht / 2, 300, 50)
w2 = GameSprite('stone.png', 370, 100, 50, 400)
barriers.add(w1)
barriers.add(w2)
packman = Player('bobr.png', 5, win_heidht - 80, 80, 80, 0, 0)
final_sprite = GameSprite('brevno.png', win_width - 85 , win_heidht- 100, 80, 80)


monster1 = Enemy('AMUGUS.png' win_width- 80, 150, 80, 80, 3)
monster2 = Enemy('AMUGUS.png' win_width- 80, 230, 80, 80, 4)
monsters.add(monster1)
monsters.add(monster2)


finish = False
run = True
while run:
  time.delay(50)

  for e in event.get():
    if e.type == QUIT:
      run = False
    elif e.type == KEYDOWN:
      if e.key == K_LEFT:
        packman.x_speed= -5
      elif e.key == K_RIGHT:
        packman.x_speed= 5
      elif e.key == K_UP:
        packman.y_speed= -5
      elif e.key == K_DOWN:
        packman.y_speed= 5
    elif e.type ==KEYUP:
      if e.key == K_LEFT:
        packman.x_speed= 0
      elif e.key == K_RIGHT:
        packman.x_speed= 0
      elif e.key == K_UP:
        packman.y_speed= 0
      elif e.key == K_DOWN:
        packman.y_speed= 0
  if not finish:
    window.fill(back)

    packman.update()
    bullets.update()

    packman.reset()

    bullets.draw(window)
    barriers.draw(window)
    final_sprite.reset()
    sprite.groupcollide(monsters, bullets, True, False)
    monsters.update()
    monsters.draw(window)
    sprite.groupcollide(bullets, barriers, True, False)



    if sprite_collode_rect(packman, monster):
      finish=True

      img = image.load('block.png')
      d = img.get_width() // img.get_height()
      window.fill((255, 255, 255))
      window.blit(transform.scale(img, (win_heidht * d, win_heidht))), (90,0))
    
    if sprite_collode_rect(packman, final_sprite):
      finish=True

      img = image.load('win.png')
      window.fill((255, 255, 255))
      window.blit(transform.scale(img, (win_heidht * d, win_heidht))), (0,0))
  

  display.update







  