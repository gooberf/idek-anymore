# brings in pygame, the thing that actually makes things outside of the terminal possible.
import pygame

# initializes pygame.
pygame.init()

# the player sprite.
player = pygame.Rect(500, 500, 50, 50)

# turns the screen, the frame limiter, and the "is this code still running" into something re-callable
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
running = True

while running:
    # painting the screen black every frame. This makes sure the player's sprite doesnt paint the entire thing. Without this, the screen would stay the player's color wherever they went.
    screen.fill("black")

    #drawing the player, specifically after the screen.fill
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    # movement, duh
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    # so the thing will like... close... when the player closes it.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    # caps the framerate at 800 (the player would move at lightspeed otherwise)
    clock.tick(800)

pygame.quit()