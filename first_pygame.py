# Header lines
import pygame
pygame.init()

# Display window of game created
screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Title of Game")

# Red Rectangle properties
width_of_rectangle = 50
height_of_rectangle = 75

velocity = 5 # Speed of rectangle
x = 50  # Initial position on x-axis
y = 400 # Initial position on y-axis


# Jumping Mechanic
jumping = False
jump_count = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        # Exits window and terminates application upon quitting program
        if event.type == pygame.QUIT:
            run = False

    keyPress = pygame.key.get_pressed()

    # Created object will move with keypress (Arrow Keys)
    # Second condition checks to make sure movable object stays within the window's border
    if keyPress[pygame.K_LEFT] and (x > velocity):
      x -= velocity
    if keyPress[pygame.K_RIGHT] and (x < screenWidth - width_of_rectangle):
      x += velocity

    # Moving rectangle up/down is only allowed when object isn't performing jumping action
    if not(jumping):
      if keyPress[pygame.K_UP] and (y > velocity):
        y -= velocity
      if keyPress[pygame.K_DOWN] and (y < screenHeight - height_of_rectangle):
        y += velocity
      if keyPress[pygame.K_SPACE]:
        jumping = True

    # Moving left/right is still allowed when jumping motion is in effect
    else:
      if jump_count >= -10:
        neg = 1
        if jump_count < 0:
          neg = -1

        # Jumping action is performed with a negative parabola effect
        y -= (jump_count ** 2) / 2 * neg
        jump_count -= 1
      else:
        jumping = False
        jump_count = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width_of_rectangle, height_of_rectangle))
    pygame.display.update()

pygame.quit()
