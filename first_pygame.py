# Header lines
import pygame
pygame.init()

# Display window of game created
window = pygame.display.set_mode((500,500))
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


pygame.quit()
