import threading
import pygame, sys
from button import Button
import random


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess_Number_Game\music\music1.mp3")

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Guess Number Game")

icon = pygame.image.load(r'C:\Users\ngllv\.vscode-cli\pygameguessnumber\download.jpg')
pygame.display.set_icon(icon)

BG = pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess_Number_Game\assets\Background.png")
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
    return pygame.font.Font(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess_Number_Game\assets\font.ttf", size)


def play():
    SCREEN.fill(WHITE)
    text = ""
    nums = random.randrange(1000, 10000)

    max_attempts = 6
    attempts_left = max_attempts

    while attempts_left > 0:

        draw_text("Enter your guess:", 50, 200, BLACK)

        draw_text(text, 50, 250, BLACK)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(640, 680),text_input="BACK", font=get_font(30), base_color="black", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)        
        PLAY_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    
                    SCREEN.fill(WHITE)

                    n = int(text)
                    try:
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
                                    draw_text("Correct number - Correct position :", 50,300 )
                                    draw_text(str(correct_position), 50, 350)  # Specify X and Y coordinates
                                    draw_text("Correct number - Wrong position :", 50, 400)
                                    draw_text(str(wrong_position), 50, 450)  # Specify X and Y coordinates

                                    n = int(text)
                                    
                                elif count == 0:
                                    draw_text("None of the numbers match the result. Try again", 400, 600, BLACK)
                                    n = int(text)

                                    # Reset text
                                text = ""

                    except ValueError:
                        # Handle the ValueError if conversion to int fails
                        draw_text("Almost there. Keep Moving! .", 500, 550, BLACK)

                    text = ""
                    attempts_left -= 1
                if event.key == pygame.K_BACKSPACE:
                    SCREEN.fill(WHITE)
                    text = text[:-1]
                else:

                    text += event.unicode



            pygame.display.update()
            pygame.display.flip()
            pygame.time.Clock().tick(30)


def options():
    text1 = font.render("Machine will generate a random number", True, BLACK)
    text2 = font.render("Yor mission is try to find the number given by the machine", True, BLACK)
    text3 = font.render("Each time you enter the number , you'll got hint", True, BLACK)
    text4 = font.render("The player with the fewest attempts will be the winner", True, BLACK)
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        SCREEN.blit(text1, (300, 100))  # Blit the first line at (100, 100)
        SCREEN.blit(text2, (300, 150))  # Blit the second line at (100, 150)
        SCREEN.blit(text3, (300, 200))  # Blit the third line at (100, 200)
        SCREEN.blit(text4, (300, 250))  # Blit the third line at (100, 200)

        OPTIONS_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(30), base_color="Black",
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

        PLAY_BUTTON = Button(image=pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess_Number_Game\assets\Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess_Number_Game\assets\Options Rect.png"), pos=(640, 400),
                                text_input="Rules", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(r"C:\Users\ngllv\.vscode-cli\pygameguessnumber\Guess_Number_Game\assets\Quit Rect.png"), pos=(640, 550),
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