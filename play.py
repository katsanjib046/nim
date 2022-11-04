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
ORANGE = (255, 165, 0)
SKY_BLUE = (135, 206, 235)
GRAY = (128, 128, 128)
TORQUOISE = (64, 224, 208)

# Define some fonts
smallFont = pygame.font.SysFont("comicsansms", 15)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 24)
mediumFont.set_bold(True)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 64)
largeFont.set_bold(True)
extraLargeFont = pygame.font.Font("OpenSans-Regular.ttf", 94)
extraLargeFont.set_bold(True)

# Define some sounds
click_sound = pygame.mixer.Sound("click.wav")
winner = pygame.mixer.Sound("winner.wav")
loser = pygame.mixer.Sound("loser.wav")
# background music
pygame.mixer.music.load("background.ogg")
# play the background music indefinitely
pygame.mixer.music.play(-1)


# some variables to handle functions
running = True
level = False
gameOn = False
p = None
c= None
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Fill the screen with white
    screen.fill(SKY_BLUE)

    if not gameOn:

        # Draw the title
        title = extraLargeFont.render("Play Nim With AI", True, ORANGE)
        titleRect = title.get_rect()
        titleRect.center = (width // 2, height // 2 - 300)
        screen.blit(title, titleRect)

        if level == False:
            # Select the difficulty level
            easyButton = pygame.draw.rect(screen, TORQUOISE, (width // 2 - 100, height // 2 - 55, 200, 50))
            easyText = mediumFont.render("Easy", True, WHITE)
            easyTextRect = easyText.get_rect()
            easyTextRect.center = (width // 2, height // 2 - 25)
            screen.blit(easyText, easyTextRect)

            mediumButton = pygame.draw.rect(screen, ORANGE, (width // 2 - 100, height // 2, 200, 50))
            mediumText = mediumFont.render("Medium", True, WHITE)
            mediumTextRect = mediumText.get_rect()
            mediumTextRect.center = (width // 2, height // 2 + 25)
            screen.blit(mediumText, mediumTextRect)

            hardButton = pygame.draw.rect(screen, RED, (width // 2 - 100, height // 2 + 55, 200, 50))
            hardText = mediumFont.render("Hard", True, WHITE)
            hardTextRect = hardText.get_rect()
            hardTextRect.center = (width // 2, height // 2 + 75)
            screen.blit(hardText, hardTextRect)

            # add a quit button
            quitButton = pygame.draw.rect(screen, GRAY, (width // 2 - 100, height // 2 + 200, 200, 50))
            quitText = mediumFont.render("Quit", True, WHITE)
            quitTextRect = quitText.get_rect()
            quitTextRect.center = (width // 2, height // 2 + 225)
            screen.blit(quitText, quitTextRect)

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
                elif quitButton.collidepoint(event.pos):
                    click_sound.play()
                    running = False
                    sys.exit()

                # leave a note that the AI is training
                if level:
                    trainText = mediumFont.render("AI is training...", True, WHITE)
                    trainTextRect = trainText.get_rect()
                    trainTextRect.center = (width // 2, height // 2 + 150)
                    screen.blit(trainText, trainTextRect)
                    pygame.display.update()
                # Train the AI
                ai = nim.train(train_n)

        else:
            # Draw the buttons
            playButton = pygame.draw.rect(screen, TORQUOISE, (width // 2 - 100, height // 2 - 50, 200, 50))
            playText = mediumFont.render("Start", True, ORANGE)
            playTextRect = playText.get_rect()
            playTextRect.center = (width // 2, height // 2 - 25)
            screen.blit(playText, playTextRect)

            backButton = pygame.draw.rect(screen, GRAY, (width // 2 - 100, height // 2 + 50, 200, 50))
            backText = mediumFont.render("Back", True, BLACK)
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
            # empty dict for buttons
            button = {}

            # get all the actions
            actions = nim.Nim.available_actions(game.piles)

            # Draw the piles with a loop
            for i in range(len(game.piles)):
                pile = game.piles[i]
                
                # print an info text for each pile
                pileText = mediumFont.render("Pile " + str(i + 1), True, BLACK)
                pileTextRect = pileText.get_rect()
                pileTextRect.center = (100 + i * 200, 50)
                screen.blit(pileText, pileTextRect)
                
                # Draw small buttons for each pile at the bottom of the pile
                for j in range(pile):
                    # buttons for the human player
                    button[str(i)+str(j)] = pygame.draw.circle(screen, GREEN, (100 + i * 200, 100 + j * 50), 20)
                    # show the number of stones to remove
                    buttonText = mediumFont.render(str(j + 1), True, WHITE)
                    buttonTextRect = buttonText.get_rect()
                    buttonTextRect.center = (100 + i * 200, 100 + j * 50)
                    screen.blit(buttonText, buttonTextRect)

            # Add instructions on how to play
            instructionText = smallFont.render("Instruction: Click on a number to remove that many stones from that pile.", True, BLACK)
            instructionTextRect = instructionText.get_rect()
            instructionTextRect.center = (width // 2, height - 300)
            screen.blit(instructionText, instructionTextRect)
            instructionText2 = smallFont.render("The player who removes the last stone loses.", True, BLACK)
            instructionTextRect2 = instructionText2.get_rect()
            instructionTextRect2.center = (width // 2, height - 280)
            screen.blit(instructionText2, instructionTextRect2)



            
            # Add the event for these buttons if it's the human player's turn
            if game.player == human_player:
                # print an info that it is the human player's turn
                turnText = mediumFont.render("Your turn", True, BLACK)
                turnTextRect = turnText.get_rect()
                turnTextRect.center = (width // 2, height - 50)
                screen.blit(turnText, turnTextRect)
                # print AI's previous move
                if p is not None and c is not None:
                    word = 'stone' if c == 1 else 'stones'
                    aiText = mediumFont.render("AI removed " + str(c) + " "+ word +" from pile " + str(p + 1), True, BLACK)
                    aiTextRect = aiText.get_rect()
                    aiTextRect.center = (width // 2, height - 100)
                    screen.blit(aiText, aiTextRect)
                    pygame.display.update()
                for i in range(len(game.piles)):
                    pile = game.piles[i]
                    for j in range(pile):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if button[str(i)+str(j)].collidepoint(event.pos):
                                click_sound.play()
                                game.move((i, j + 1))
            # else if it's the AI's turn, let the AI play and wait for 1 second
            else:
                # print that it is the AI's turn and wait for 1 second
                aiText = mediumFont.render("AI is thinking...", True, BLACK)
                aiTextRect = aiText.get_rect()
                aiTextRect.center = (width // 2, height - 100)
                screen.blit(aiText, aiTextRect)
                pygame.display.update()
                time.sleep(1)
                # let the AI play
                p,c = ai.choose_action(game.piles)
                game.move((p, c))
                        
        
        # if the game is over
        else:
            # reset p and c
            p = None
            c = None
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
            backButton = pygame.draw.rect(screen, TORQUOISE, (width // 2 - 100, height // 2 + 50, 200, 50))
            backText = mediumFont.render("REPLAY", True, WHITE)
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
            # button to quit the game
            quitButton = pygame.draw.rect(screen, GRAY, (width // 2 - 100, height // 2 + 150, 200, 50))
            quitText = mediumFont.render("Quit", True, WHITE)
            quitTextRect = quitText.get_rect()
            quitTextRect.center = (width // 2, height // 2 + 175)
            screen.blit(quitText, quitTextRect)
            # add the event for this button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitButton.collidepoint(event.pos):
                    click_sound.play()
                    running = False
                    sys.exit()

    pygame.display.flip()

pygame.quit()


