import pygame
import csv
import random

pygame.font.init()

screen = pygame.display.set_mode((1280, 720))

HEADING_FONT = pygame.font.SysFont('cosolas', 55)
WORD_FONT = pygame.font.SysFont('calibri', 70)
MSG_FONT = pygame.font.SysFont('consolas', 30)

HEADING = HEADING_FONT.render('WORDLE CLONE', True, (255, 255, 255))
HEADING_RECT = HEADING.get_rect(center = (640, 40))

RETRY = HEADING_FONT.render('RETRY', True, (0, 255, 0))
RETRY_RECT = RETRY.get_rect(center = (80, 690))

EXIT = HEADING_FONT.render('EXIT', True, (0, 0, 255))
EXIT_RECT = EXIT.get_rect(center = (1200, 690))

NEL_MSG = MSG_FONT.render("Not Enough Letters", True, (0, 0, 0))
NEL_MSG_RECT = NEL_MSG.get_rect(center = (640, 110))

WGC_MSG = MSG_FONT.render("You Guessed the Word", True, (0, 0, 0))
WGC_MSG_RECT = WGC_MSG.get_rect(center = (640, 110))

WNL_MSG = MSG_FONT.render("Not in Word List", True, (0, 0, 0))
WNL_MSG_RECT = WNL_MSG.get_rect(center = (640, 110))

def game(word, word_guess_pos):
    screen.blit(HEADING, HEADING_RECT)
    screen.blit(RETRY, RETRY_RECT)
    screen.blit(EXIT, EXIT_RECT)

    # WORD 1
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(420, 170, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(510, 170, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(600, 170, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(690, 170, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(780, 170, 80, 80), 2)

    if word_guess_pos == 1:
        initial_point = 440
        if word:
            for char in word:
                character = WORD_FONT.render(char, True, (255, 255, 255))
                screen.blit(character, (initial_point, 178))
                initial_point += 90

    # WORD 2
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(420, 260, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(510, 260, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(600, 260, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(690, 260, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(780, 260, 80, 80), 2)

    if word_guess_pos == 2:
        initial_point = 440
        if word:
            for char in word:
                character = WORD_FONT.render(char, True, (255, 255, 255))
                screen.blit(character, (initial_point, 268))
                initial_point += 90

    # WORD 3
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(420, 350, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(510, 350, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(600, 350, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(690, 350, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(780, 350, 80, 80), 2)

    if word_guess_pos == 3:
        initial_point = 440
        if word:
            for char in word:
                character = WORD_FONT.render(char, True, (255, 255, 255))
                screen.blit(character, (initial_point, 358))
                initial_point += 90

    # WORD 4
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(420, 440, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(510, 440, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(600, 440, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(690, 440, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(780, 440, 80, 80), 2)

    if word_guess_pos == 4:
        initial_point = 440
        if word:
            for char in word:
                character = WORD_FONT.render(char, True, (255, 255, 255))
                screen.blit(character, (initial_point, 448))
                initial_point += 90

    # WORD 5
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(420, 530, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(510, 530, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(600, 530, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(690, 530, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(780, 530, 80, 80), 2)

    if word_guess_pos == 5:
        initial_point = 440
        if word:
            for char in word:
                character = WORD_FONT.render(char, True, (255, 255, 255))
                screen.blit(character, (initial_point, 538))
                initial_point += 90

    # WORD 6
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(420, 620, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(510, 620, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(600, 620, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(690, 620, 80, 80), 2)
    pygame.draw.rect(screen, (155, 155, 155), pygame.Rect(780, 620, 80, 80), 2)

    if word_guess_pos == 6:
        initial_point = 440
        if word:
            for char in word:
                character = WORD_FONT.render(char, True, (255, 255, 255))
                screen.blit(character, (initial_point, 628))
                initial_point += 90

def check_word(word, word_guess_pos):
    if word_guess_pos == 1:
        for i in range(len(word_guessed_1)):
            if word_guessed_1[i] in word_to_guess:
                if word_guessed_1[i] == word_to_guess[i]:
                    wg1_color.append((0, 255, 0))
                else:
                    wg1_color.append((255, 255, 0))
            else:
                wg1_color.append((155, 155, 155))
    if word_guess_pos == 2:
        for i in range(len(word_guessed_2)):
            if word_guessed_2[i] in word_to_guess:
                if word_guessed_2[i] == word_to_guess[i]:
                    wg2_color.append((0, 255, 0))
                else:
                    wg2_color.append((255, 255, 0))
            else:
                wg2_color.append((155, 155, 155))
    if word_guess_pos == 3:
        for i in range(len(word_guessed_3)):
            if word_guessed_3[i] in word_to_guess:
                if word_guessed_3[i] == word_to_guess[i]:
                    wg3_color.append((0, 255, 0))
                else:
                    wg3_color.append((255, 255, 0))
            else:
                wg3_color.append((155, 155, 155))
    if word_guess_pos == 4:
        for i in range(len(word_guessed_4)):
            if word_guessed_4[i] in word_to_guess:
                if word_guessed_4[i] == word_to_guess[i]:
                    wg4_color.append((0, 255, 0))
                else:
                    wg4_color.append((255, 255, 0))
            else:
                wg4_color.append((155, 155, 155))
    if word_guess_pos == 5:
        for i in range(len(word_guessed_5)):
            if word_guessed_5[i] in word_to_guess:
                if word_guessed_5[i] == word_to_guess[i]:
                    wg5_color.append((0, 255, 0))
                else:
                    wg5_color.append((255, 255, 0))
            else:
                wg5_color.append((155, 155, 155))
    if word_guess_pos == 6:
        for i in range(len(word_guessed_6)):
            if word_guessed_6[i] in word_to_guess:
                if word_guessed_6[i] == word_to_guess[i]:
                    wg6_color.append((0, 255, 0))
                else:
                    wg6_color.append((255, 255, 0))
            else:
                wg6_color.append((155, 155, 155))

def words_guessed_colors(word_guess_pos):

    if word_guess_pos > 1 and len(word_guessed_1) == 5:
        pygame.draw.rect(screen, wg1_color[0], pygame.Rect(420, 170, 80, 80))
        pygame.draw.rect(screen, wg1_color[1], pygame.Rect(510, 170, 80, 80))
        pygame.draw.rect(screen, wg1_color[2], pygame.Rect(600, 170, 80, 80))
        pygame.draw.rect(screen, wg1_color[3], pygame.Rect(690, 170, 80, 80))
        pygame.draw.rect(screen, wg1_color[4], pygame.Rect(780, 170, 80, 80))

    if word_guess_pos > 2 and len(word_guessed_2) == 5:
        pygame.draw.rect(screen, wg2_color[0], pygame.Rect(420, 260, 80, 80))
        pygame.draw.rect(screen, wg2_color[1], pygame.Rect(510, 260, 80, 80))
        pygame.draw.rect(screen, wg2_color[2], pygame.Rect(600, 260, 80, 80))
        pygame.draw.rect(screen, wg2_color[3], pygame.Rect(690, 260, 80, 80))
        pygame.draw.rect(screen, wg2_color[4], pygame.Rect(780, 260, 80, 80))

    if word_guess_pos > 3 and len(word_guessed_3) == 5:
        pygame.draw.rect(screen, wg3_color[0], pygame.Rect(420, 350, 80, 80))
        pygame.draw.rect(screen, wg3_color[1], pygame.Rect(510, 350, 80, 80))
        pygame.draw.rect(screen, wg3_color[2], pygame.Rect(600, 350, 80, 80))
        pygame.draw.rect(screen, wg3_color[3], pygame.Rect(690, 350, 80, 80))
        pygame.draw.rect(screen, wg3_color[4], pygame.Rect(780, 350, 80, 80))

    if word_guess_pos > 4 and len(word_guessed_4) == 5:
        pygame.draw.rect(screen, wg4_color[0], pygame.Rect(420, 440, 80, 80))
        pygame.draw.rect(screen, wg4_color[1], pygame.Rect(510, 440, 80, 80))
        pygame.draw.rect(screen, wg4_color[2], pygame.Rect(600, 440, 80, 80))
        pygame.draw.rect(screen, wg4_color[3], pygame.Rect(690, 440, 80, 80))
        pygame.draw.rect(screen, wg4_color[4], pygame.Rect(780, 440, 80, 80))

    if word_guess_pos > 5 and len(word_guessed_5) == 5:
        pygame.draw.rect(screen, wg5_color[0], pygame.Rect(420, 530, 80, 80))
        pygame.draw.rect(screen, wg5_color[1], pygame.Rect(510, 530, 80, 80))
        pygame.draw.rect(screen, wg5_color[2], pygame.Rect(600, 530, 80, 80))
        pygame.draw.rect(screen, wg5_color[3], pygame.Rect(690, 530, 80, 80))
        pygame.draw.rect(screen, wg5_color[4], pygame.Rect(780, 530, 80, 80))

    if word_guess_pos > 6 and len(word_guessed_6) == 5:
        pygame.draw.rect(screen, wg6_color[0], pygame.Rect(420, 620, 80, 80))
        pygame.draw.rect(screen, wg6_color[1], pygame.Rect(510, 620, 80, 80))
        pygame.draw.rect(screen, wg6_color[2], pygame.Rect(600, 620, 80, 80))
        pygame.draw.rect(screen, wg6_color[3], pygame.Rect(690, 620, 80, 80))
        pygame.draw.rect(screen, wg6_color[4], pygame.Rect(780, 620, 80, 80))

def words_guessed():
    if word_guessed_1:
        initial_point = 440
        for char in word_guessed_1:
            character = WORD_FONT.render(char, True, (255, 255, 255))
            screen.blit(character, (initial_point, 178))
            initial_point += 90

    if word_guessed_2:
        initial_point = 440
        for char in word_guessed_2:
            character = WORD_FONT.render(char, True, (255, 255, 255))
            screen.blit(character, (initial_point, 268))
            initial_point += 90

    if word_guessed_3:
        initial_point = 440
        for char in word_guessed_3:
            character = WORD_FONT.render(char, True, (255, 255, 255))
            screen.blit(character, (initial_point, 358))
            initial_point += 90

    if word_guessed_4:
        initial_point = 440
        for char in word_guessed_4:
            character = WORD_FONT.render(char, True, (255, 255, 255))
            screen.blit(character, (initial_point, 448))
            initial_point += 90

    if word_guessed_5:
        initial_point = 440
        for char in word_guessed_5:
            character = WORD_FONT.render(char, True, (255, 255, 255))
            screen.blit(character, (initial_point, 538))
            initial_point += 90

    if word_guessed_6:
        initial_point = 440
        for char in word_guessed_6:
            character = WORD_FONT.render(char, True, (255, 255, 255))
            screen.blit(character, (initial_point, 628))
            initial_point += 90

word_guessed_1 = ""
wg1_color = []
word_guessed_2 = ""
wg2_color = []
word_guessed_3 = ""
wg3_color = []
word_guessed_4 = ""
wg4_color = []
word_guessed_5 = ""
wg5_color = []
word_guessed_6 = ""
wg6_color = []

WORD_LIST = []

word = ""
word_guess_pos = 1

nel_msg = 0
wgc_msg = 0
wnl_msg = 0

clock = pygame.time.Clock()

with open("word_list.csv") as f:
    WORDS = csv.reader(f)
    for words in WORDS:
        WORD_LIST.append(words[0].upper())

word_to_guess = random.choice(WORD_LIST)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if EXIT_RECT.collidepoint(event.pos):
                    running = False
            if RETRY_RECT.collidepoint(event.pos):
                word_guessed_1 = ""
                wg1_color = []
                word_guessed_2 = ""
                wg2_color = []
                word_guessed_3 = ""
                wg3_color = []
                word_guessed_4 = ""
                wg4_color = []
                word_guessed_5 = ""
                wg5_color = []
                word_guessed_6 = ""
                wg6_color = []

                word = ""
                word_guess_pos = 1
                word_to_guess = random.choice(WORD_LIST)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(word) < 5:
                    nel_msg = 1
                else:
                    if word_guess_pos == 1:
                        word_guessed_1 = word
                    if word_guess_pos == 2:
                        word_guessed_2 = word
                    if word_guess_pos == 3:
                        word_guessed_3 = word
                    if word_guess_pos == 4:
                        word_guessed_4 = word
                    if word_guess_pos == 5:
                        word_guessed_5 = word
                    if word_guess_pos == 6:
                        word_guessed_6 = word

                    check_word(word, word_guess_pos)

                    if word == word_to_guess:
                        wgc_msg = 1

                    if word not in WORD_LIST:
                        wnl_msg = 1
                        if word_guess_pos == 1:
                            word_guessed_1 = ""
                            wg1_color.clear()
                        if word_guess_pos == 2:
                            word_guessed_2 = ""
                            wg2_color.clear()
                        if word_guess_pos == 3:
                            word_guessed_3 = ""
                            wg3_color.clear()
                        if word_guess_pos == 4:
                            word_guessed_4 = ""
                            wg4_color.clear()
                        if word_guess_pos == 5:
                            word_guessed_5 = ""
                            wg5_color.clear()
                        if word_guess_pos == 6:
                            word_guessed_6 = ""
                            wg6_color.clear()
                        word = ""
                        word_guess_pos -= 1

                    word = ""
                    word_guess_pos += 1
            if event.key == pygame.K_BACKSPACE:
                if word:
                    word = word[:-1]
            else:
                if len(word) < 5:
                    if event.key == pygame.K_RETURN:
                        pass
                    else:
                        word += event.unicode.upper()


    screen.fill((0, 0, 0))

    game(word, word_guess_pos)

    words_guessed_colors(word_guess_pos)
    words_guessed()

    if nel_msg == 1:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(480, 90, 320, 38))
        screen.blit(NEL_MSG, NEL_MSG_RECT)
        pygame.display.update()
        pygame.time.delay(1500)
        nel_msg = 0

    if wnl_msg == 1:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(490, 90, 300, 38))
        screen.blit(WNL_MSG, WNL_MSG_RECT)
        pygame.display.update()
        pygame.time.delay(1500)
        wnl_msg = 0

    if wgc_msg == 1:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(460, 90, 360, 38))
        screen.blit(WGC_MSG, WGC_MSG_RECT)
        pygame.display.update()
        pygame.time.delay(2500)
        wgc_msg = 0

        word_guessed_1 = ""
        wg1_color = []
        word_guessed_2 = ""
        wg2_color = []
        word_guessed_3 = ""
        wg3_color = []
        word_guessed_4 = ""
        wg4_color = []
        word_guessed_5 = ""
        wg5_color = []
        word_guessed_6 = ""
        wg6_color = []

        word = ""
        word_guess_pos = 1
        word_to_guess = random.choice(WORD_LIST)

    if word_guess_pos == 7 and word != word_to_guess:
        WNG_MSG = MSG_FONT.render(f"{word_to_guess}", True, (0, 0, 0))
        WNG_MSG_RECT = WNG_MSG.get_rect(center = (640, 110))

        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(590, 90, 100, 38))
        screen.blit(WNG_MSG, WNG_MSG_RECT)
        pygame.display.update()
        pygame.time.delay(2500)

        word_guessed_1 = ""
        wg1_color = []
        word_guessed_2 = ""
        wg2_color = []
        word_guessed_3 = ""
        wg3_color = []
        word_guessed_4 = ""
        wg4_color = []
        word_guessed_5 = ""
        wg5_color = []
        word_guessed_6 = ""
        wg6_color = []

        word = ""
        word_guess_pos = 1
        word_to_guess = random.choice(WORD_LIST)

    pygame.display.update()

pygame.quit()
