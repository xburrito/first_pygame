# Header lines
import pygame
pygame.init()

# Display window of game created
screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Title of Game")

x = 50
y = 50
width_of_rectangle = 40
height_of_rectangle = 60
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
    # Second condition checks to make sure movable object stays within the window's border
    if keyPress[pygame.K_LEFT] and (x > velocity):
      x -= velocity
    if keyPress[pygame.K_RIGHT] and (x < screenWidth - width_of_rectangle):
      x += velocity
    if keyPress[pygame.K_UP] and (y > velocity):
      y -= velocity
    if keyPress[pygame.K_DOWN] and (y < screenHeight - height_of_rectangle):
      y += velocity

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width_of_rectangle, height_of_rectangle))
    pygame.display.update()

pygame.quit()
