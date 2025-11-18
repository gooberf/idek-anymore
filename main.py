import pygame
from pygame import *

# initializes pygame
pygame.init()

# basics for the window
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
run = True

# pretty self explanitory. Sizes and positioning.
char_1_x_pos = 800
char_1_y_pos = 500
char_1_width = 100
char_1_length = 100

char_add_x_pos = 800
char_add_y_pos = 350
char_add_width = 100
char_add_length = 100

char_equal_x_pos = 800
char_equal_y_pos = 200
char_equal_width = 100
char_equal_length = 100

char_2_x_pos = 650
char_2_y_pos = 500
char_2_width = 100
char_2_length = 100

list_of_inputs = []
lisd_of_inputs_2 = []
numbers = []
operator = []
history = []

# Load the image, and getting the rect/hitbox in a sense
char_1 = pygame.image.load("sprites/Char-1.png")
char_1 = pygame.transform.scale(char_1, (char_1_length, char_1_width))  # Resize the image
char_1_rect = char_1.get_rect(topleft=(char_1_x_pos, char_1_y_pos))

char_add = pygame.image.load("sprites/Char-Add.png")
char_add = pygame.transform.scale(char_add, (char_add_length, char_add_width))
char_add_rect = char_add.get_rect(topleft=(char_add_x_pos, char_add_y_pos))

char_equal = pygame.image.load("sprites/Char-Equal.png")
char_equal = pygame.transform.scale(char_equal, (char_equal_length, char_equal_width))
char_equal_rect = char_equal.get_rect(topleft=(char_equal_x_pos, char_equal_y_pos))

char_2 = pygame.image.load("sprites/Char-2.png")
char_2 = pygame.transform.scale(char_2, (char_2_length, char_2_width))
char_2_rect = char_2.get_rect(topleft=(char_2_x_pos, char_2_y_pos))

# this does the math :)
def equation(inputs):
    total = 0
    for item in inputs:
        if isinstance(item, int):
            total += item
        elif item in ['+', '-', '*', '/']:
            operator.append(item)
    return total


while run:

    # turns the background grey, removing any trail that a moving piece would otherwise leave.
    screen.fill((100, 100, 100))
    
    # Shows the characters
    screen.blit(char_1, char_1_rect)

    screen.blit(char_add, char_add_rect)

    screen.blit(char_equal, char_equal_rect)

    screen.blit(char_2, char_2_rect)
    
    # idk what this is for, but it doesnt work without it.
    pygame.display.flip()
    
    # frame limiter, honestly more useful than you'd think.
    clock.tick(800)

    # the actual interactive bits
    for event in pygame.event.get():
        
        # quits if the user closes the program
        if event.type == pygame.QUIT:
            run = False
        
        # logic for determining what the player pressed and if they pressed it
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # the numbers on the calculator GUI
            if char_1_rect.collidepoint(event.pos):
                list_of_inputs.append(1)
                print(list_of_inputs)
                
            elif char_2_rect.collidepoint(event.pos):
                list_of_inputs.append(2)
                print(list_of_inputs)

            # the plus symbol on the calculator GUI
            elif char_add_rect.collidepoint(event.pos):
                list_of_inputs.append("+")
                print(list_of_inputs)

            # the equalization symbol on the calculator GUI
            elif char_equal_rect.collidepoint(event.pos):
                result = equation(list_of_inputs)
                print(result)
                list_of_inputs = []

                
# No clue what this does either, but it was put here in the introductory tutorial that teaches practically nothing except how to put a square on the screen. I trust them :)
pygame.quit()