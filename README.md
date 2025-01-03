# Snake Game

## Overview
This repository contains a simple implementation of the classic Snake game using Python and Pygame. The game features interactive gameplay, dynamic speed adjustments, and a scoring system.

## Features
- **Interactive Gameplay**:
  - Control the snake using arrow keys or `W`, `A`, `S`, `D`.
  - Eat food to grow the snake and earn points.
  - Avoid colliding with yourself to keep playing.

- **Game Dynamics**:
  - Speed increases as the score rises, adding to the challenge.
  - The snake can wrap around the screen edges.

- **Scoring System**:
  - Earn 10 points for every piece of food eaten.
  - Display your current score during gameplay.

- **Pause and Resume**:
  - Pause the game by pressing `P`.

## Instructions
1. **Setup**:
   Ensure you have Python installed along with the Pygame library. Install Pygame using the following command:
   ```bash
   pip install pygame
   ```

2. **Run the Game**:
   Execute the script in a Python environment:
   ```bash
   python snake_game.py
   ```

3. **Controls**:
   - Move the snake:
     - `Arrow Keys` or `W`, `A`, `S`, `D`
   - Pause/Resume: `P`
   - Adjust Speed:
     - Increase: `M`
     - Decrease: `N`
   - Exit: `ESC`

4. **Gameplay**:
   - Guide the snake to eat food and grow in length.
   - Avoid colliding with your own body to prevent a game over.

## Example Screenshot
![image](https://github.com/user-attachments/assets/0a88d8b6-7793-41d9-9b06-d3f4abe5f5c2)

![image](https://github.com/user-attachments/assets/b683eb5e-b8ad-4a16-adfd-2da31522d9cc)

## Code Overview
- **Game Loop**:
  - Continuously updates the snake's position, checks for collisions, and redraws the screen.

- **Functions**:
  - `show_score`: Displays the current score.
  - `losing`: Handles game-over conditions.

- **Game Dynamics**:
  - Food is randomly placed on the screen.
  - Snake wraps around the edges of the screen.

## License
This project is open-source and available under the MIT License.

---
Enjoy playing Snake!
