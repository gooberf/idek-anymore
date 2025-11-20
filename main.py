import pygame
from pygame import *

# initializes pygame
pygame.init()

# basics for the window
screen = pygame.display.set_mode((420, 520))
clock = pygame.time.Clock()
run = True

# pretty self explanitory. Sizes and positioning.
char_0_x_pos = 105
char_0_y_pos = 705 - 290
char_0_width = 105
char_0_length = 105

char_1_x_pos = 210
char_1_y_pos = 600 - 290
char_1_width = 105
char_1_length = 105

char_add_x_pos = 315
char_add_y_pos = 495 - 290
char_add_width = 105
char_add_length = 105

char_equal_x_pos = 315
char_equal_y_pos = 705 - 290
char_equal_width = 105
char_equal_length = 105

char_2_x_pos = 105
char_2_y_pos = 600 - 290
char_2_width = 105
char_2_length = 105

char_3_x_pos = 0
char_3_y_pos = 600 - 290
char_3_width = 105
char_3_length = 105

char_4_x_pos = 210
char_4_y_pos = 495 - 290
char_4_width = 105
char_4_length = 105

char_5_x_pos = 105
char_5_y_pos = 495 - 290
char_5_width = 105
char_5_length = 105

char_6_x_pos = 0
char_6_y_pos = 495 - 290
char_6_width = 105
char_6_length = 105

char_7_x_pos = 210
char_7_y_pos = 390 - 290
char_7_width = 105
char_7_length = 105

char_8_x_pos = 105
char_8_y_pos = 390 - 290
char_8_width = 105
char_8_length = 105

char_9_x_pos = 0
char_9_y_pos = 390 - 290
char_9_width = 105
char_9_length = 105

char_sub_x_pos = 315
char_sub_y_pos = 390 - 290
char_sub_width = 105
char_sub_length = 105

char_div_x_pos = 210
char_div_y_pos = 705 - 290
char_div_width = 105
char_div_length = 105

char_mul_x_pos = 0
char_mul_y_pos = 705 - 290
char_mul_width = 105
char_mul_length = 105

char_fd_x_pos = 315
char_fd_y_pos = 600 - 290
char_fd_width = 105
char_fd_length = 105

list_of_inputs = []
numbers = []
operator = []
history = [] # for making the history later on

# Load the image, and getting the rect/hitbox in a sense
char_0 = pygame.image.load("sprites/Char-0.png")
char_0 = pygame.transform.scale(char_0, (char_0_length, char_0_width))
char_0_rect = char_0.get_rect(topleft=(char_0_x_pos, char_0_y_pos))

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

char_3 = pygame.image.load("sprites/Char-3.png")
char_3 = pygame.transform.scale(char_3, (char_3_length, char_3_width))
char_3_rect = char_3.get_rect(topleft=(char_3_x_pos, char_3_y_pos))

char_4 = pygame.image.load("sprites/Char-4.png")
char_4 = pygame.transform.scale(char_4, (char_4_length, char_4_width))
char_4_rect = char_4.get_rect(topleft=(char_4_x_pos, char_4_y_pos))

char_5 = pygame.image.load("sprites/Char-5.png")
char_5 = pygame.transform.scale(char_5, (char_5_length, char_5_width))
char_5_rect = char_5.get_rect(topleft=(char_5_x_pos, char_5_y_pos))

char_6 = pygame.image.load("sprites/Char-6.png")
char_6 = pygame.transform.scale(char_6, (char_6_length, char_6_width))
char_6_rect = char_6.get_rect(topleft=(char_6_x_pos, char_6_y_pos))

char_7 = pygame.image.load("sprites/Char-7.png")
char_7 = pygame.transform.scale(char_7, (char_7_length, char_7_width))
char_7_rect = char_7.get_rect(topleft=(char_7_x_pos, char_7_y_pos))

char_8 = pygame.image.load("sprites/Char-8.png")
char_8 = pygame.transform.scale(char_8, (char_8_length, char_8_width))
char_8_rect = char_8.get_rect(topleft=(char_8_x_pos, char_8_y_pos))

char_9 = pygame.image.load("sprites/Char-9.png")
char_9 = pygame.transform.scale(char_9, (char_9_length, char_9_width))
char_9_rect = char_9.get_rect(topleft=(char_9_x_pos, char_9_y_pos))

char_sub = pygame.image.load("sprites/Char-Subtraction.png")
char_sub = pygame.transform.scale(char_sub, (char_sub_length, char_sub_width))
char_sub_rect = char_sub.get_rect(topleft=(char_sub_x_pos, char_sub_y_pos))

char_div = pygame.image.load("sprites/Char-Division.png")
char_div = pygame.transform.scale(char_div, (char_div_length, char_div_width))
char_div_rect = char_div.get_rect(topleft=(char_div_x_pos, char_div_y_pos))

char_mul = pygame.image.load("sprites/Char-Multiplication.png")
char_mul = pygame.transform.scale(char_mul, (char_mul_length, char_mul_width))
char_mul_rect = char_mul.get_rect(topleft=(char_mul_x_pos, char_mul_y_pos))

char_fd = pygame.image.load("sprites/Char-Floored_Division.png")
char_fd = pygame.transform.scale(char_fd, (char_fd_length, char_fd_width))
char_fd_rect = char_fd.get_rect(topleft=(char_fd_x_pos, char_fd_y_pos))

# this does the math :)
def equation(inputs):
    # combine consecutive digit clicks into multi-digit numbers, then evaluate
    if not inputs:
        return 0

    nums = []
    ops = []
    current = None

    for item in inputs:
        if isinstance(item, int):
            if current is None:
                current = item
            else:
                current = current * 10 + item
        else:
            # operator encountered
            if current is None:
                # if expression starts with an operator, treat previous as 0
                current = 0
            nums.append(current)
            ops.append(item)
            current = None

    if current is None:
        current = 0
    nums.append(current)

    # handle * and / first (precedence), then + and -
    new_nums = [nums[0]]
    new_ops = []
    for op, n in zip(ops, nums[1:]):
        if op == '*':
            new_nums[-1] = new_nums[-1] * n
        elif op == '/':
            if n == 0:
                return "Error: Division by zero"
            new_nums[-1] = new_nums[-1] / n
        elif op =='//':
            if n == 0:
                return "Error: Division by zero"
            new_nums[-1] = new_nums[-1] // n
        else:
            new_ops.append(op)
            new_nums.append(n)

    result = new_nums[0]
    for op, n in zip(new_ops, new_nums[1:]):
        if op == '+':
            result += n
        elif op == '-':
            result -= n

    # return int when result is a whole number
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result


while run:

    # turns the background grey, removing any trail that a moving piece would otherwise leave.
    screen.fill((100, 100, 100))
    
    # Shows the characters
    screen.blit(char_equal, char_equal_rect)

    screen.blit(char_add, char_add_rect)

    screen.blit(char_sub, char_sub_rect)

    screen.blit(char_div, char_div_rect)

    screen.blit(char_mul, char_mul_rect)

    screen.blit(char_fd, char_fd_rect) 

    screen.blit(char_0, char_0_rect)

    screen.blit(char_1, char_1_rect)

    screen.blit(char_2, char_2_rect)

    screen.blit(char_3, char_3_rect)
    
    screen.blit(char_4, char_4_rect)

    screen.blit(char_5, char_5_rect)

    screen.blit(char_6, char_6_rect)

    screen.blit(char_7, char_7_rect)

    screen.blit(char_8, char_8_rect)

    screen.blit(char_9, char_9_rect)

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
            
            elif char_3_rect.collidepoint(event.pos):
                list_of_inputs.append(3)
                print(list_of_inputs)

            elif char_4_rect.collidepoint(event.pos):
                list_of_inputs.append(4)
                print(list_of_inputs)

            elif char_5_rect.collidepoint(event.pos):
                list_of_inputs.append(5)
                print(list_of_inputs)

            elif char_6_rect.collidepoint(event.pos):
                list_of_inputs.append(6)
                print(list_of_inputs)

            elif char_7_rect.collidepoint(event.pos):
                list_of_inputs.append(7)
                print(list_of_inputs)

            elif char_8_rect.collidepoint(event.pos):
                list_of_inputs.append(8)
                print(list_of_inputs)

            elif char_9_rect.collidepoint(event.pos):
                list_of_inputs.append(9)
                print(list_of_inputs)
            
            elif char_0_rect.collidepoint(event.pos):
                list_of_inputs.append(0)
                print(list_of_inputs)

            # the plus symbol on the calculator GUI
            elif char_add_rect.collidepoint(event.pos):
                list_of_inputs.append("+")
                print(list_of_inputs)

            elif char_sub_rect.collidepoint(event.pos):
                list_of_inputs.append("-")
                print(list_of_inputs)

            elif char_div_rect.collidepoint(event.pos):
                list_of_inputs.append("/")
                print(list_of_inputs)
            
            elif char_mul_rect.collidepoint(event.pos):
                list_of_inputs.append("*")
                print(list_of_inputs)

            elif char_fd_rect.collidepoint(event.pos):
                list_of_inputs.append("//")
                print(list_of_inputs)

            # the equalization symbol on the calculator GUI
            elif char_equal_rect.collidepoint(event.pos):
                result = equation(list_of_inputs)
                print(result)
                list_of_inputs = []

                
# No clue what this does either, but it was put here in the introductory tutorial that teaches practically nothing except how to put a square on the screen. I trust them :)
pygame.quit()