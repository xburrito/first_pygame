# Header lines
import pygame
pygame.init()

# Display window of game created
screenWidth = 800
screenHeight = 600

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

bg = pygame.image.load('Assets/Background/full-background.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):

        self.x = x                  # init pos on x-axis
        self.y = y                  # init pos on y-axis

        self.width = width
        self.height = height
        self.velocity = 5           # Movement Speed

        # Jumping Mechanic
        self.jump_count = 10
        self.walk_count = 0
        self.idle_motion = 0
        self.jumping = False
        self.left = False
        self.right = False

    def draw(self, win):
        if (self.walk_count+1 >= 39):
            self.walk_count = 0
        if (self.idle_motion+1 >= 33):
            self.idle_motion = 0

        if self.left:
            win.blit(move_Left[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        elif self.right:
            win.blit(move_Right[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        else:
            win.blit(idle[self.idle_motion//3], (self.x,self.y))

# Performs real-time alterations to the assets displayed within the window
def refreshGameWindow():
    # global walk_count
    # global idle_motion

    # Sets background-image
    win.blit(bg, (0,0))

    ourPlayer.draw(win)
    pygame.display.update()


# Main While Loop
ourPlayer = player(300, 540, 64, 64)
run = True
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
    if keyPress[pygame.K_LEFT] and (ourPlayer.x > ourPlayer.velocity):
      ourPlayer.x -= ourPlayer.velocity
      ourPlayer.left = True
      ourPlayer.right = False

    elif keyPress[pygame.K_RIGHT] and (ourPlayer.x < screenWidth - ourPlayer.width):
      ourPlayer.x += ourPlayer.velocity
      ourPlayer.left = False
      ourPlayer.right = True

    else:
        ourPlayer.left = False
        ourPlayer.right = False
        ourPlayer.walk_count = 0

    # Moving rectangle up/down is only allowed when object isn't performing jumping action
    if not(ourPlayer.jumping):
      if keyPress[pygame.K_UP] and (ourPlayer.y > ourPlayer.velocity):
        ourPlayer.y -= ourPlayer.velocity
      if keyPress[pygame.K_DOWN] and (ourPlayer.y < screenHeight - ourPlayer.height):
        ourPlayer.y += ourPlayer.velocity
      if keyPress[pygame.K_SPACE]:
        ourPlayer.jumping = True
        ourPlayer.right = False
        ourPlayer.left = False
        ourPlayer.walk_count = 0

    # Moving left/right is still allowed when jumping motion is in effect
    else:
      if ourPlayer.jump_count >= -10:
        neg = 1
        if ourPlayer.jump_count < 0:
          neg = -1

        # Jumping action is performed with a negative parabola effect
        ourPlayer.y -= (ourPlayer.jump_count ** 2) / 2 * neg
        ourPlayer.jump_count -= 1
      else:
        ourPlayer.jumping = False
        ourPlayer.jump_count = 10

    refreshGameWindow()

pygame.quit()
