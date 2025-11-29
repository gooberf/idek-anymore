import pygame

# initializes pygame
pygame.init()

# basics for the window
screen = pygame.display.set_mode((420, 625))
clock = pygame.time.Clock()
run = True

# for the text display
BASE_FONT_SIZE = 100

the_font = pygame.font.SysFont(None, BASE_FONT_SIZE)

# sprite info dict

spriteinfo = {
    "char_0": {"path": "sprites/Char-0.png", "pos": (105, 705 - 290), "size": (105, 105)},
    "char_1": {"path": "sprites/Char-1.png", "pos": (210, 600 - 290), "size": (105, 105)},
    "char_2": {"path": "sprites/Char-2.png", "pos": (105, 600 - 290), "size": (105, 105)},
    "char_3": {"path": "sprites/Char-3.png", "pos": (0, 600 - 290), "size": (105, 105)},
    "char_4": {"path": "sprites/Char-4.png", "pos": (210, 495 - 290), "size": (105, 105)},
    "char_5": {"path": "sprites/Char-5.png", "pos": (105, 495 - 290), "size": (105, 105)},
    "char_6": {"path": "sprites/Char-6.png", "pos": (0, 495 - 290), "size": (105, 105)},
    "char_7": {"path": "sprites/Char-7.png", "pos": (210, 390 - 290), "size": (105, 105)},
    "char_8": {"path": "sprites/Char-8.png", "pos": (105, 390 - 290), "size": (105, 105)},
    "char_9": {"path": "sprites/Char-9.png", "pos": (0, 390 - 290), "size": (105, 105)},
    "char_add": {"path": "sprites/Char-Add.png", "pos": (315, 495 - 290), "size": (105, 105)},
    "char_sub": {"path": "sprites/Char-Subtraction.png", "pos": (315, 390 - 290), "size": (105, 105)},
    "char_div": {"path": "sprites/Char-Division.png", "pos": (210, 705 - 290), "size": (105, 105)},
    "char_mul": {"path": "sprites/Char-Multiplication.png", "pos": (0, 705 - 290), "size": (105, 105)},
    "char_fd": {"path": "sprites/Char-Floored_Division.png", "pos": (315, 600 - 290), "size": (105, 105)},
    "char_equal": {"path": "sprites/Char-Equal.png", "pos": (315, 705 - 290), "size": (105, 105)},
    "char_history": {"path": "sprites/Char-History.png", "pos": (420/2 - 105, 520), "size": (210, 105)},
}

def get_font_size(base_size, text):
    size = base_size - len(text) * 2
    return max(20, size)   # never let the font get too small



def draw_text(text, font, text_col, x, y):
    # allow passing either a color tuple or a color name string
    if isinstance(text_col, str):
        try:
            color = pygame.Color(text_col)
        except Exception:
            color = (0, 0, 0)
    else:
        color = text_col
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


def inputs_to_string(inputs):
    """Convert the list_of_inputs into a human-readable expression string.

    Consecutive digit entries become multi-digit numbers visually (e.g. [1,2,'+','3'] -> '12+3').
    """
    s = ""
    for item in inputs:
        s += str(item)
    return s

list_of_inputs = []
numbers = []
operator = []
history = [] # now i just need to dispay it somehow/somewhere

# Load the image, and getting the rect/hitbox in a sense
char_0 = pygame.image.load(spriteinfo["char_0"]["path"])
char_0 = pygame.transform.scale(char_0, spriteinfo["char_0"]["size"])
char_0_rect = char_0.get_rect(topleft=spriteinfo["char_0"]["pos"])

char_1 = pygame.image.load(spriteinfo["char_1"]["path"])
char_1 = pygame.transform.scale(char_1, spriteinfo["char_1"]["size"])  # Resize the image
char_1_rect = char_1.get_rect(topleft=spriteinfo["char_1"]["pos"])

char_add = pygame.image.load(spriteinfo["char_add"]["path"])
char_add = pygame.transform.scale(char_add, spriteinfo["char_add"]["size"])
char_add_rect = char_add.get_rect(topleft=spriteinfo["char_add"]["pos"])

char_equal = pygame.image.load(spriteinfo["char_equal"]["path"])
char_equal = pygame.transform.scale(char_equal, spriteinfo["char_equal"]["size"])
char_equal_rect = char_equal.get_rect(topleft=spriteinfo["char_equal"]["pos"])

char_2 = pygame.image.load(spriteinfo["char_2"]["path"])
char_2 = pygame.transform.scale(char_2, spriteinfo["char_2"]["size"])
char_2_rect = char_2.get_rect(topleft=spriteinfo["char_2"]["pos"])

char_3 = pygame.image.load(spriteinfo["char_3"]["path"])
char_3 = pygame.transform.scale(char_3, spriteinfo["char_3"]["size"])
char_3_rect = char_3.get_rect(topleft=spriteinfo["char_3"]["pos"])

char_4 = pygame.image.load(spriteinfo["char_4"]["path"])
char_4 = pygame.transform.scale(char_4, spriteinfo["char_4"]["size"])
char_4_rect = char_4.get_rect(topleft=spriteinfo["char_4"]["pos"])

char_5 = pygame.image.load(spriteinfo["char_5"]["path"])
char_5 = pygame.transform.scale(char_5, spriteinfo["char_5"]["size"])
char_5_rect = char_5.get_rect(topleft=spriteinfo["char_5"]["pos"])

char_6 = pygame.image.load(spriteinfo["char_6"]["path"])
char_6 = pygame.transform.scale(char_6, spriteinfo["char_6"]["size"])
char_6_rect = char_6.get_rect(topleft=spriteinfo["char_6"]["pos"])

char_7 = pygame.image.load(spriteinfo["char_7"]["path"])
char_7 = pygame.transform.scale(char_7, spriteinfo["char_7"]["size"])
char_7_rect = char_7.get_rect(topleft=spriteinfo["char_7"]["pos"])

char_8 = pygame.image.load(spriteinfo["char_8"]["path"])
char_8 = pygame.transform.scale(char_8, spriteinfo["char_8"]["size"])
char_8_rect = char_8.get_rect(topleft=spriteinfo["char_8"]["pos"])

char_9 = pygame.image.load(spriteinfo["char_9"]["path"])
char_9 = pygame.transform.scale(char_9, spriteinfo["char_9"]["size"])
char_9_rect = char_9.get_rect(topleft=spriteinfo["char_9"]["pos"])

char_sub = pygame.image.load(spriteinfo["char_sub"]["path"])
char_sub = pygame.transform.scale(char_sub, spriteinfo["char_sub"]["size"])
char_sub_rect = char_sub.get_rect(topleft=spriteinfo["char_sub"]["pos"])

char_div = pygame.image.load(spriteinfo["char_div"]["path"])
char_div = pygame.transform.scale(char_div, spriteinfo["char_div"]["size"])
char_div_rect = char_div.get_rect(topleft=spriteinfo["char_div"]["pos"])

char_mul = pygame.image.load(spriteinfo["char_mul"]["path"])
char_mul = pygame.transform.scale(char_mul, spriteinfo["char_mul"]["size"])
char_mul_rect = char_mul.get_rect(topleft=spriteinfo["char_mul"]["pos"])

char_fd = pygame.image.load(spriteinfo["char_fd"]["path"])
char_fd = pygame.transform.scale(char_fd, spriteinfo["char_fd"]["size"])
char_fd_rect = char_fd.get_rect(topleft=spriteinfo["char_fd"]["pos"])

char_history = pygame.image.load(spriteinfo["char_history"]["path"])
char_history = pygame.transform.scale(char_history, spriteinfo["char_history"]["size"])
char_history_rect = char_history.get_rect(topleft=spriteinfo["char_history"]["pos"])

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

result = None

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

    screen.blit(char_history, char_history_rect)

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
    
    # choose what to display on the top line:
    # - show the current expression while typing
    # - if there's no current expression (e.g. after pressing '='), show the result on the same line
    expr_str = inputs_to_string(list_of_inputs)
    if expr_str:
        top_text = expr_str
    elif result is not None:
        top_text = str(result)
    else:
        top_text = ""

    if top_text:
        top_size = get_font_size(BASE_FONT_SIZE, top_text)
        top_font = pygame.font.SysFont(None, top_size)
        draw_text(top_text, top_font, (0, 0, 0), 0, 0)

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
                history.append(result)
                # clear the current input expression after computing
                list_of_inputs = []
            elif char_history_rect.collidepoint(event.pos):
                print(history)

                
# No clue what this does either, but it was put here in the introductory tutorial that teaches practically nothing except how to put a square on the screen. I trust them :)
pygame.quit()