import pygame
import sys
import time
import random
import nim

# Initialize pygame
pygame.init()
size = width, height = 1000, 800

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
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 32)
largeFont.set_bold(True)

# # Define some images
# pile_image = pygame.image.load("pile.png")

# Define some sounds
click_sound = pygame.mixer.Sound("click.wav")
winner = pygame.mixer.Sound("winner.wav")
loser = pygame.mixer.Sound("loser.wav")


running = True
level = False
gameOn = False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Fill the screen with white
    screen.fill(WHITE)

    if not gameOn:

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
                    train_n = 100
                    level = True
                    time.sleep(0.5)
                elif mediumButton.collidepoint(event.pos):
                    click_sound.play()
                    train_n = 5000
                    level = True
                    time.sleep(0.5)
                elif hardButton.collidepoint(event.pos):
                    click_sound.play()
                    train_n = 10000
                    level = True
                    time.sleep(0.5)
            
                # Train the AI
                ai = nim.train(train_n)

        else:
            # Draw the buttons
            playButton = pygame.draw.rect(screen, GREEN, (width // 2 - 100, height // 2 - 50, 200, 50))
            playText = mediumFont.render("Start", True, WHITE)
            playTextRect = playText.get_rect()
            playTextRect.center = (width // 2, height // 2 - 25)
            screen.blit(playText, playTextRect)

            backButton = pygame.draw.rect(screen, GREEN, (width // 2 - 100, height // 2 + 50, 200, 50))
            backText = mediumFont.render("Back", True, WHITE)
            backTextRect = backText.get_rect()
            backTextRect.center = (width // 2, height // 2 + 75)
            screen.blit(backText, backTextRect)

            # Add the event for these buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.collidepoint(event.pos):
                    click_sound.play()
                    time.sleep(0.5)
                    gameOn = True
                    # Start the game
                    game = nim.Nim()
                    # choose a random player to start
                    human_player = random.choice([0, 1])


                elif backButton.collidepoint(event.pos):
                    click_sound.play()
                    level = False
                    time.sleep(0.5)

    else:
        if game.winner is None:

            # print whose turn it is
            if game.player == human_player:
                # show that it is the human player's turn at the bottom of the screen
                playerText = mediumFont.render("Your turn", True, BLACK)
                playerTextRect = playerText.get_rect()
                playerTextRect.center = (width // 2, height - 50)
                screen.blit(playerText, playerTextRect)
            else:
                # show that it is the AI's turn at the bottom of the screen
                playerText = mediumFont.render("AI's turn", True, BLACK)
                playerTextRect = playerText.get_rect()
                playerTextRect.center = (width // 2, height - 50)
                screen.blit(playerText, playerTextRect)

            # get all the actions
            actions = nim.Nim.available_actions(game.piles)

            # Draw the piles with a loop
            for i in range(len(game.piles)):
                pile = game.piles[i]
                # draw small circles for each pile
                for j in range(pile):
                    pygame.draw.circle(screen, BLACK, (100 + i * 200, 100 + j * 50), 20)
                
                # print an info text
                pileText = mediumFont.render("Pile " + str(i + 1), True, BLACK)
                pileTextRect = pileText.get_rect()
                pileTextRect.center = (100 + i * 200, 50)
                screen.blit(pileText, pileTextRect)

                # Draw small buttons for each pile at the bottom of the pile
                for j in range(pile):
                    # buttons for the human player
                    button = pygame.draw.circle(screen, GREEN, (100 + i * 200, 100 + j * 50), 20, 1)
                    # show the number of stones to remove
                    buttonText = mediumFont.render(str(j + 1), True, WHITE)
                    buttonTextRect = buttonText.get_rect()
                    buttonTextRect.center = (100 + i * 200, 100 + j * 50)
                    screen.blit(buttonText, buttonTextRect)

                    # Add the event for these buttons if it's the human player's turn
                    if game.player == human_player:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if button.collidepoint(event.pos):
                                click_sound.play()
                                game.move((i, j + 1))
                    # else if it's the AI's turn, let the AI play and wait for 1 second
                    elif game.player != human_player:
                        time.sleep(2)
                        p,c = ai.choose_action(game.piles)
                        game.move((p, c))
        
        # check if the game is over
        else:
            # show the winner at the top of the screen
            if game.winner == human_player:
                winnerText = largeFont.render("You won!", True, GREEN)
                sound = winner
            else:
                winnerText = largeFont.render("You lost!", True, RED)
                sound = loser
            winnerTextRect = winnerText.get_rect()
            winnerTextRect.center = (width // 2, height - 50)
            screen.blit(winnerText, winnerTextRect)
            sound.play()

            # show the back button
            backButton = pygame.draw.rect(screen, GREEN, (width // 2 - 100, height // 2 + 50, 200, 50))
            backText = mediumFont.render("Back", True, WHITE)
            backTextRect = backText.get_rect()
            backTextRect.center = (width // 2, height // 2 + 75)
            screen.blit(backText, backTextRect)

            # Add the event for this button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.collidepoint(event.pos):
                    click_sound.play()
                    gameOn = False
                    level = False
                    time.sleep(0.5)

    pygame.display.flip()


pygame.quit()


