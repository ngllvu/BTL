import threading

import pygame, sys
from button import Button
import random


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess Number Game\music\music1.mp3")

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Guess Number Game")

icon = pygame.image.load(r'C:\Users\ngllv\.vscode-cli\pygameguessnumber\download.jpg')
pygame.display.set_icon(icon)

BG = pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess Number Game\assets\Background.png")
font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def count_digits_at_wrong_position(nums, n):
    count = 0
    for i in range(len(nums)):
        if n[i] in nums and n[i] != nums[i]:
            count += 1

    return count


def count_digits_at_right_position(nums, n):
    count = 0
    for i in range(len(nums)):
        if n[i] == nums[i]:
            count += 1

    return count


def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True , color)
    SCREEN.blit(text_surface, (x, y))


def get_font(size):
    return pygame.font.Font(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess Number Game\assets\font.ttf", size)


def play():

    user_input_text = ""
    nums = random.randrange(1000, 10000)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    
                    n = int(user_input_text)
                                       
                    try:

                        n = int(user_input_text)

                        if n == nums:
                            draw_text("Excellent! You won in the first try!", 100, 300, BLACK)
                        else:
                            tried = 0

                            while n != nums:
                                count = 0
                                tried += 1
                                n = str(n)
                                nums = str(nums)
                                result = []

                                for i in range(0, 4):
                                    if n[i] == nums[i]:
                                        count += 1
                                        result.append(n[i])
                                    else:
                                        continue

                                if count < 4 and count != 0:
                                    correct_position = count_digits_at_right_position(nums, n)
                                    wrong_position = count_digits_at_wrong_position(nums, n)

                                    # Display results
                                    draw_text("Correct number - Correct position :", 150, 250)
                                    draw_text(str(correct_position), 200, 300)  # Specify X and Y coordinates
                                    draw_text("Correct number - Wrong position :", 250, 350)
                                    draw_text(str(wrong_position), 300, 400)  # Specify X and Y coordinates

                                    n = int(user_input_text)

                                elif count == 0:
                                    draw_text("None of the numbers match the result. Try again", 300, 550, BLACK)
                                    n = int(user_input_text)

                                # Reset user_input_text
                                user_input_text = ""

                    except ValueError:
                        # Handle the ValueError if conversion to int fails
                        draw_text("Almost there. Keep Moving! .", 300, 450, BLACK)
                        user_input_text = ""

                    user_input_text = ""

                if event.key == pygame.K_BACKSPACE:

                    user_input_text = user_input_text[:-1]

                else:
                    # Thêm ký tự vào ô nhập liệu
                    user_input_text += event.unicode

            SCREEN.fill(WHITE)
            draw_text("Enter your guess:", 50, 200, BLACK)
            draw_text(user_input_text, 50, 250, BLACK)
            
            pygame.display.flip()
\

def options():
    text = 'The player with the fewest attempts will be the winner'
    lines = text.split('/n')
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        for i, line in enumerate(lines):
            OPTIONS_TEXT = get_font(20).render(line, True, "Black")

            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))

            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(30), base_color="Black",
                              hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()





def main_menu():
    while True:
        def play_music():
            pygame.mixer.music.play()

        music_thread = threading.Thread(target=play_music())

        music_thread.start()



        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render(" GAME MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess Number Game\assets\Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess Number Game\assets\Options Rect.png"), pos=(640, 400),
                                text_input="Rules", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess Number Game\assets\Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



main_menu()
pygame.quit()
