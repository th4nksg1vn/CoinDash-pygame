==================================================
  ____ ___ ___ _   _   ____    _    ____  _   _ _ 
 / ___/ _ \_ _| \ | | |  _ \  / \  / ___|| | | | |
| |  | | | | ||  \| | | | | |/ _ \ \___ \| |_| | |
| |__| |_| | || |\  | | |_| / ___ \ ___) |  _  |_|
 \____\___/___|_| \_| |____/_/   \_\____/|_| |_(_)

==================================================


-----------
# Overview
-----------
A fast-paced 2D arcade game built with Python and Pygame. Control your character, collect coins, and avoid obstacles before the timer runs out!

It solves the problem of creating a simple but engaging game that demonstrates important programming concepts such as animation, collision detection and object-oriented design. 

The game is intended for beginner or casual players, while also serving as a learning project for students studying Python game development


---------------
# Contributors
---------------
- Aseda Adusi-Poku
- Christina Yvonne Pitt


-----------
# Features
-----------
Basic:
- Dynamic Gameplay: Levels scale in difficulty, spawning more coins and obstacles as you progress.
- Player Movement: Player is able to move up, down, left and right using the specific keys.
- Time Increment: Accurately tracks player level and increases time accordingly
- Score & Time Display: Displays current character score and time left before death, enabling players to keep track of in-game progress.
- Button Functionality: Start, Back, Exit, How to Play buttons are functional, displaying a different page each.
- Animated Sprites: Smooth animations for player movement, coin spinning, and "hurt" states.
- Fair Collisions: Custom colliders smaller than the actual sprites to provide a more forgiving gameplay experience.

Advanced:
- Character Customization: Choose between a Fox or a Knight and select different backgrounds.
- High Score System: Automatically saves and ranks your top 5 local scores in a `scores.txt` file.
- Sound Effects: Coin collection and character death sounds.


-------------
# Tech Stack
-------------
- Programming Language: Python
- Framework: Pygame


--------------------
# Project Structure
--------------------
* `main.py`: The entry point for the application. Manages menus, customization, and high scores.
* `game.py`: Contains the core game loop, spawning logic, and level management.
* `player.py`: Defines the Player class, including movement logic and animations.
* `coin.py`: Handles coin animation and collection logic.
* `cactus.py`: Defines the obstacle behavior and collision boxes.
* `button.py`: A reusable UI component for menu interactions.
* `assets`: Contains player, background, coin and cactus images and game audios.
* `score.txt`: Contains top 5 local game scores.

---------------------
# Setup Instructions
---------------------
1. Ensure all asset folders (`assets/UI/`, `assets/player/`, etc.) are in the same directory as the script files.
2. Run the game using:
   ```bash
   python main.py
   ```
---------------
# Requirements
---------------
- Python 3.x
- Pygame library (`pip install pygame`)


-----------
# Controls
-----------
 Movement: Arrow Keys (Up, Down, Left, Right) or W, A, S, D.
 Menus: Left Mouse Click to interact with buttons.


----------------------
# How to Play (Usage)
----------------------
1. OBJECTIVE: Collect all coins on the screen to advance to the next level.
2. TIMER: You start with 10 seconds. Every time you clear a level, you gain an additional 5 seconds.
3. HAZARDS: Avoid the cacti! Touching a cactus or running out of time results in Game Over.
4. SCORING: Each coin collected increases your score. Try to beat the top scores in the leaderboard.


---------------------------
# Challenges & Limitations
---------------------------
- Difficulty using recursion to implement the countdown timer as stated in the project proposal.
- Difficulty finding and implementing appropriate background game music as stated in the proposal.


----------------------
# Future Improvements
----------------------
- Implement background music.
- Pause button and pause page implementation.
- Introduction of customisable game themes.
- Ability to select game difficulty (Beginner, Advanced, Professional, Expert, etc)
- Integration of in-game sound & audio control.
- Encryption of score.txt file, preventing users from manually changing high scores without playing the game.
- Introduction of power up coins which make the game easier depending on current difficulty level.


----------
# Credits
----------
Christina Yvonne Pitt:
- Coin Module and spawning system using random position generation
- Develop the score tracking system and display the score on screen
- Button implementation and functionality (Start, Exit, etc)
- Assisted with collision detection implementation and testing
- Implement the countdown timer and time display

Aseda Adusi-Poku:
- Implementation of game loop structure and frame updates
- Programming of player movement and keyboard input handling
- Implementation of cactus spawning and obstacle behaviour
- Collision detection system for player, coins, and cactii
- Implement the difficulty scaling algorithm (increasing spawn rates)
- Integration and management of sprite rendering and object updates
- Implement the high score persistence system using file reading and writing

-------------
# References
-------------
Programming With Nick. “Pygame Beginner Tutorial: Adding Buttons to Your Game. (OOP).” 
	YouTube, 20 June 2024, www.youtube.com/watch?v=q_2xwkjefNo. Accessed 22 Apr. 2025.

“Pygame Programming Tutorials.” YouTube, 
	www.youtube.com/playlist?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5.

External assets:
Fox sprites and audio: https://github.com/nadiryuceer/coin_dash/tree/main/assets

Kinght sprites: https://brackeysgames.itch.io/brackeys-platformer-bundle