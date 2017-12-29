import pygame

def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, white,[35+x, 0+y, 25, 25])
    pygame.draw.ellipse(screen, white,[23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, white,[0+x, 65+y, 100, 100])

pygame.init()

black = [0, 255, 0]
white = [100, 55, 255]

size = [400, 500]

screen=pygame.display.set_mode(size)
draw_snowman(screen,10,10)

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen and set the screen background
    screen.fill(black)

    # Snowman in upper left
    draw_snowman(screen, 10, 10)

    # Snowman in upper right
    draw_snowman(screen, 300, 10)

    # Snowman in lower left
    draw_snowman(screen, 10, 300)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()