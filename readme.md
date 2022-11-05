# Nim: Play Against AI
## Introduction

### What is Nim?
Nim is a mathematical game of strategy in which two players take turns removing objects from distinct heaps. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap. The goal of the game is to avoid taking the last object. 

### What is Nim AI?
This is a Nim game that you can play against an AI. The AI uses the reinforcement learning algorithm Q-learning to learn how to play the game.

### What is Q-learning?
Q-learning is a model-free reinforcement learning algorithm. It learns a policy, which tells an agent what action to take under what circumstances. Q-learning can be used to find an optimal action-selection policy for any given (finite) Markov decision process (MDP).

## How to Play
The following are the rules of the game:
1. There are three different levels of difficulty: easy, medium, and hard.
2. There are 4 heaps of objects. Each heap has a different number of objects. The number of objects in the first pile is 1, the second pile is 3, the third pile is 5, and the fourth pile is 7.
3. The player and the AI will take turns removing objects from the piles. Who will go first is randomly decided.
4. When it is your turn, you will see "Your turn" at the bottom of the screen. You can click on the piles to remove objects from them. You can remove any number of objects from a pile, but you must remove at least one object. If you click on number 5 from pile 4 then you will remove 3 objects from pile 4.
6. The AI will take its turn after you. You will see "AI is thinking..." at the bottom of the screen.
7. The game ends when there are no more objects left in the piles. The player who removes the last object loses. So try not to remove the last object!

## How to Run
In your terminal, run the following command:
```python play.py```

## Description of Files
1. nim.py: This file contains the Nim class, NimAI class and training function. It also has play function if you want to play directly using the terminal as in CS50AI project. Class Nim contains the game logic. It initiates the board for the game and make moves and checks if the game is over. Class NimAI contains the AI logic. It uses the Q-learning algorithm to learn how to play the game. The train function trains the AI for some number of games. The play function is used to play the game directly in the terminal.
2. play.py: It uses the pygame library to create the game interface. If you choose easy level, the AI will be trained for 100 games. If you choose medium level, the AI will be trained for 1000 games. If you choose hard level, the AI will be trained for 10000 games. 
3. click.wav: This is the sound effect when you click on a button or a pile.
4. winner.wav: This is the sound effect when you win the game.
5. loser.wav: This is the sound effect when you lose the game.
6. background.ogg: This is the background music.
7. OpenSans-Regular.ttf: This is the font used in the game.
8. README.md: This is the readme file.
9. requirements.txt: This file contains the list of libraries that you need to install to run the game. It need only one module, pygame. You can install it by running the following command in your terminal: ```pip install pygame```

## References
1. [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning)
2. [CS50AI](https://cs50.harvard.edu/ai/2020)
3. [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
4. [Nim](https://en.wikipedia.org/wiki/Nim)