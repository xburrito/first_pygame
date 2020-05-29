# Header lines
import pygame
pygame.init()

# Display window of game created
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Title of Game")

x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        # Exits window and terminates application upon quitting program
        if event.type == pygame.QUIT:
            run = False

    keyPress = pygame.key.get_pressed()

    # Created object will move with keypress
    if keyPress[pygame.K_LEFT]:
      x -= velocity
    if keyPress[pygame.K_RIGHT]:
      x += velocity
    if keyPress[pygame.K_UP]:
      y -= velocity
    if keyPress[pygame.K_DOWN]:
      y += velocity

    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
