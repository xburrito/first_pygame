# Header lines
import pygame
pygame.init()

# Display window of game created
screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Title of Game")

# Importing Assets
move_Left = [pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_1.png'),pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_2.png'),
              pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_3.png'),pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_4.png'),
              pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_5.png'),pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_6.png'),
              pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_7.png'),pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_8.png'),
              pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_9.png'),pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_10.png'),
              pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_11.png'),pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_12.png'),
              pygame.image.load('Assets/Skeleton/Walking_Left/WalkLeft_13.png')]

move_Right = [pygame.image.load('Assets/Skeleton/Walking_Right/walk_1.png'),pygame.image.load('Assets/Skeleton/Walking_Right/walk_2.png'),
              pygame.image.load('Assets/Skeleton/Walking_Right/walk_3.png'),pygame.image.load('Assets/Skeleton/Walking_Right/walk_4.png'),
              pygame.image.load('Assets/Skeleton/Walking_Right/walk_5.png'),pygame.image.load('Assets/Skeleton/Walking_Right/walk_6.png'),
              pygame.image.load('Assets/Skeleton/Walking_Right/walk_7.png'),pygame.image.load('Assets/Skeleton/Walking_Right/walk_8.png'),
              pygame.image.load('Assets/Skeleton/Walking_Right/walk_9.png'),pygame.image.load('Assets/Skeleton/Walking_Right/walk_10.png'),
              pygame.image.load('Assets/Skeleton/Walking_Right/walk_11.png'),pygame.image.load('Assets/Skeleton/Walking_Right/walk_12.png'),
              pygame.image.load('Assets/Skeleton/Walking_Right/walk_13.png')]

idle = [pygame.image.load('Assets/Skeleton/Idle/Idle_1.png'),pygame.image.load('Assets/Skeleton/Idle/Idle_2.png'),
        pygame.image.load('Assets/Skeleton/Idle/Idle_3.png'),pygame.image.load('Assets/Skeleton/Idle/Idle_4.png'),
        pygame.image.load('Assets/Skeleton/Idle/Idle_5.png'),pygame.image.load('Assets/Skeleton/Idle/Idle_6.png'),
        pygame.image.load('Assets/Skeleton/Idle/Idle_7.png'),pygame.image.load('Assets/Skeleton/Idle/Idle_8.png'),
        pygame.image.load('Assets/Skeleton/Idle/Idle_9.png'),pygame.image.load('Assets/Skeleton/Idle/Idle_10.png'),
        pygame.image.load('Assets/Skeleton/Idle/Idle_11.png')]

bg = [pygame.image.load('Assets/Background/full-background.png')]

clock = pygame.time.Clock()

# Red Rectangle properties
width_of_rectangle = 50
height_of_rectangle = 75

velocity = 5 # Speed of rectangle
x = 50  # Initial position on x-axis
y = 400 # Initial position on y-axis

# Jumping Mechanic
jump_count = 10
walk_count = 0
idle_motion = 0
jumping = False
left = False
right = False
run = True

# Performs real-time alterations to the assets displayed within the window
def refreshGameWindow():
    global walk_count
    global idle_motion

    # Sets background-image
    win.blit(bg, (0,0))

    if (walk_count+1 >= 39):
        walk_count = 0
    if (idle_motion+1 >= 33):
        idle_motion = 0

    if left:
        win.blit(move_Left[walk_count//3], (x,y))
        walk_count += 1
    elif right:
        win.blit(move_Right[walk_count//3], (x,y))
        walk_count += 1
    else:
        win.blit(idle[idle_motion//3], (x,y))

    pygame.display.update()


# Main While Loop
while run:
    # Sets the FPS
    clock.tick(39)

    for event in pygame.event.get():
        # Exits window and terminates application upon quitting program
        if event.type == pygame.QUIT:
            run = False

    keyPress = pygame.key.get_pressed()

    # Created object will move with keypress (Arrow Keys)
    # Second condition checks to make sure movable object stays within the window's border
    if keyPress[pygame.K_LEFT] and (x > velocity):
      x -= velocity
      left = True
      right = False

    elif keyPress[pygame.K_RIGHT] and (x < screenWidth - width_of_rectangle):
      x += velocity
      left = False
      right = True

    else:
        left = False
        right = False
        walk_count = 0

    # Moving rectangle up/down is only allowed when object isn't performing jumping action
    if not(jumping):
      if keyPress[pygame.K_UP] and (y > velocity):
        y -= velocity
      if keyPress[pygame.K_DOWN] and (y < screenHeight - height_of_rectangle):
        y += velocity
      if keyPress[pygame.K_SPACE]:
        jumping = True
        right = False
        left = False
        walk_count = 0

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

    refreshGameWindow()

pygame.quit()
