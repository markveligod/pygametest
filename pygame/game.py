# Импорты
import pygame

# Окно + тайтл
pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Py Game')

#Переменные
walkRight = [pygame.image.load('img/r-1.png'), pygame.image.load('img/r-2.png'), pygame.image.load('img/r-3.png'), pygame.image.load('img/r-4.png'), pygame.image.load('img/r-1.png'), pygame.image.load('img/r-2.png')]
walkLeft = [pygame.image.load('img/L-1.png'), pygame.image.load('img/L-2.png'), pygame.image.load('img/L-3.png'), pygame.image.load('img/L-4.png'), pygame.image.load('img/L-1.png'), pygame.image.load('img/L-2.png')]
playerStand = pygame.image.load('img/stand.png')
playerStand_L = pygame.image.load('img/stand-L.png')
bg = pygame.image.load('img/bg.png')
playerJump_up = pygame.image.load('img/jump-up.png')
bullet = pygame.image.load('img/bullet.png')
clock = pygame.time.Clock()
x = 50
y = 440
widht = 128
height = 128
speed = 5
isJump = False
jumpCount = 10
left = False
right = False
animCount = 0
lastMove = "right"

class Bull():
    def __init__(self, x, y, radius, color, face):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.face = face
        self.speedbull = 8*face

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global animCount
    window.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        window.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        window.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    elif isJump:
        window.blit(playerJump_up, (x, y))
    else:
        if lastMove == "right":
            window.blit(playerStand, (x, y))
        else:
            window.blit(playerStand_L, (x, y))

    for bul in bullets:
        bul.draw(window)
    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bul in bullets:
        if bul.x < 800 and bul.x > 0:
            bul.x += bul.speedbull
        else:
            bullets.pop(bullets.index(bul))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == "right":
            face = 1
        else:
            face = -1
        if len(bullets) < 5:
            bullets.append(Bull(round(x + widht // 2), round(y + height // 2), 5, (255, 0, 0), face))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 800 - widht - 5:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2)/2
            else:
                y -= (jumpCount ** 2)/2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()
