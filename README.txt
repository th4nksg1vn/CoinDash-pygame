==================================================
  ____ ___ ___ _   _   ____    _    ____  _   _ _ 
 / ___/ _ \_ _| \ | | |  _ \  / \  / ___|| | | | |
| |  | | | | ||  \| | | | | |/ _ \ \___ \| |_| | |
| |__| |_| | || |\  | | |_| / ___ \ ___) |  _  |_|
 \____\___/___|_| \_| |____/_/   \_\____/|_| |_(_)

==================================================


A fast-paced 2D arcade game built with Python and Pygame. Control your character, collect coins, and avoid obstacles before the timer runs out!

By Aseda Adusi-Poku and Christina Yvonne Pitt

---------
Features
---------
- Dynamic Gameplay: Levels scale in difficulty, spawning more coins and obstacles as you progress.
- Character Customization: Choose between a Fox or a Knight and select different backgrounds.
- High Score System: Automatically saves and ranks your top 5 local scores in a `scores.txt` file.
- Animated Sprites: Smooth animations for player movement, coin spinning, and "hurt" states.
- Fair Collisions: Custom colliders smaller than the actual sprites to provide a more forgiving gameplay experience.

---------
Controls
---------
 Movement: Arrow Keys (Up, Down, Left, Right) or W, A, S, D.
 Menus: Left Mouse Click to interact with buttons.

------------
How to Play
------------
1. OBJECTIVE: Collect all coins on the screen to advance to the next level.
2. TIMER: You start with 10 seconds. Every time you clear a level, you gain an additional 5 seconds.
3. HAZARDS: Avoid the cacti! Touching a cactus or running out of time results in Game Over.
4. SCORING: Each coin collected increases your score. Try to beat the top scores in the leaderboard.

---------------
File Structure
---------------
* `main.py`: The entry point for the application. Manages menus, customization, and high scores.
* `game.py`: Contains the core game loop, spawning logic, and level management.
* `player.py`: Defines the Player class, including movement logic and animations.
* `coin.py`: Handles coin animation and collection logic.
* `cactus.py`: Defines the obstacle behavior and collision boxes.
* `button.py`: A reusable UI component for menu interactions.

-------------
Requirements
-------------
- Python 3.x
- Pygame library (`pip install pygame`)

----------------------
Installation & Running
----------------------
1. Ensure all asset folders (`assets/UI/`, `assets/player/`, etc.) are in the same directory as the script files.
2. Run the game using:
   ```bash
   python main.py



-------
Credits
-------

Chritina Yvonne Pitt:
- Coin Module and spawning system using random position generation
- Implement the high score persistence system using file reading and writing
- Button implementation and functionality (Start, Exit, etc)
- Assisted with collision detection implementation and testing

Aseda Adusi-Poku:
- Implemention of game loop structure and frame updates
- Programming of player movement and keyboard input handling
- Implemention of cactus spawning and obstacle behaviour
- Collision detection system for player, coins, and cactii
- Implement the difficulty scaling algorithm (increasing spawn rates)
- Integration and management of sprite rendering and object updates
- Implement the countdown timer and time display
