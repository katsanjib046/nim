import pygame
import sys
import time
import random
import nim

# Initialize pygame
pygame.init()
size = width, height = 600, 400

# Create the screen
screen = pygame.display.set_mode(size)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define some fonts
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 24)
mediumFont.set_bold(True)

# # Define some images
# pile_image = pygame.image.load("pile.png")

# Define some sounds
click_sound = pygame.mixer.Sound("click.wav")


running = True
level = False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the title
    title = mediumFont.render("Play Nim", True, GREEN)
    titleRect = title.get_rect()
    titleRect.center = (width // 2, height // 2 - 100)
    screen.blit(title, titleRect)

    if level == False:
        # Select the difficulty level
        easyButton = pygame.draw.rect(screen, GREEN, (width // 2 - 100, height // 2 - 50, 200, 50))
        easyText = mediumFont.render("Easy", True, WHITE)
        easyTextRect = easyText.get_rect()
        easyTextRect.center = (width // 2, height // 2 - 25)
        screen.blit(easyText, easyTextRect)

        mediumButton = pygame.draw.rect(screen, GREEN, (width // 2 - 100, height // 2, 200, 50))
        mediumText = mediumFont.render("Medium", True, WHITE)
        mediumTextRect = mediumText.get_rect()
        mediumTextRect.center = (width // 2, height // 2 + 25)
        screen.blit(mediumText, mediumTextRect)

        hardButton = pygame.draw.rect(screen, GREEN, (width // 2 - 100, height // 2 + 50, 200, 50))
        hardText = mediumFont.render("Hard", True, WHITE)
        hardTextRect = hardText.get_rect()
        hardTextRect.center = (width // 2, height // 2 + 75)
        screen.blit(hardText, hardTextRect)

        # Add the event for these buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easyButton.collidepoint(event.pos):
                click_sound.play()
                time.sleep(0.5)
                train_n = 1000
                level = True
            elif mediumButton.collidepoint(event.pos):
                click_sound.play()
                time.sleep(0.5)
                train_n = 5000
                level = True
            elif hardButton.collidepoint(event.pos):
                click_sound.play()
                time.sleep(0.5)
                train_n = 10000
                level = True
        
            # Train the AI
            ai = nim.train(train_n)

    else:
        # Draw the buttons
        playButton = pygame.draw.rect(screen, GREEN, (width // 2 - 100, height // 2 - 50, 200, 50))
        playText = mediumFont.render("Start", True, WHITE)
        playTextRect = playText.get_rect()
        playTextRect.center = (width // 2, height // 2 - 25)
        screen.blit(playText, playTextRect)

    pygame.display.flip()


pygame.quit()


