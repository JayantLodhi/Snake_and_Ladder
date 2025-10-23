# 🎲 Snake and Ladder Game (Console-Based)

A **Python console-based Snake and Ladder game** implemented using **Object-Oriented Programming (OOP)** concepts.  
This project simulates the classic board game for **2 to 4 players**, featuring random snake and ladder placement, turn-based dice rolls, and automatic winner detection.

---

## 🧩 Features

- 🎮 **Turn-Based Gameplay:** Players take turns rolling a six-sided dice.
- 🐍 **Randomized Snakes and Ladders:** Automatically generated within valid board positions.
- 🎲 **Dice Rolling Mechanism:** Rolls range from 1–6, with safeguards against exceeding position 100.
- 🪜 **Interactive Moves:** Landing on a snake moves you down, landing on a ladder moves you up.
- 🏁 **Winning Condition:** The first player to reach exactly position 100 wins.
- 👥 **Player Input Validation:** Supports between 2 and 4 players.
- ⚙️ **Modular OOP Design:** Classes for snakes, ladders, and game management.

---

## 🧠 Code Overview

### 1️⃣ `Board_entity` Class
- Base class for both snakes and ladders.  
- Stores `start` and `end` positions.  
- Methods:
  - `get_start()` → Returns start position  
  - `get_end()` → Returns end position

### 2️⃣ `Snake` Class
- Inherits from `Board_entity`.  
- Method:  
  - `bite()` → Moves the player down if they land on the snake’s head.

### 3️⃣ `Ladder` Class
- Inherits from `Board_entity`.  
- Method:  
  - `climb()` → Moves the player up if they land at the ladder’s bottom.

### 4️⃣ `MainGame` Class
- Controls the entire gameplay logic.
- Handles:
  - Player turns  
  - Dice rolling  
  - Snakes and ladders generation  
  - Position updates  
  - Winner determination  
- Key functions:
  - `Snake_ladder_position()` → Randomly generates snake and ladder positions.
  - `Show_snake_ladder_positions()` → Displays all snake and ladder positions.
  - `Player_move(player)` → Rolls the dice and updates player position.
  - `Play()` → Runs the main game loop.

### 5️⃣ `Run_game()` Function
- Entry point of the script.  
- Takes number of players as input (2–4).  
- Initializes and starts the game.

---

## 🏗️ Future Improvements

- 🧮 Add graphical board visualization.
- 🐍 Display snakes and ladders dynamically.
- 🎨 Create GUI version using Tkinter or Pygame.
- 💾 Add save/load game functionality.

---

## 💡 Concepts Used

- Object-Oriented Programming (OOP)
- Randomization and Input Validation
- Conditional Logic and Loops
- Console-Based User Interaction

---

## 🧑‍💻 Author

**Jayant Lodhi**  
(2024210009)

---

