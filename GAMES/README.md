# AI Game Projects: Tic Tac Toe, 8-Puzzle Solver & Chess AI

This repository contains three AI-based game projects developed as part of an AI course. Each project demonstrates the implementation of fundamental AI algorithms to solve problems and build intelligent game agents.

---

## Projects Overview

### 1. Tic Tac Toe AI
- **Algorithm:** Minimax Algorithm  
- **Description:** A simple two-player game where the AI uses Minimax to never lose and optimally choose moves.
- **Features:**  
  - Player vs AI mode  
  - AI evaluates all possible moves to pick the best outcome  
- **Language:** Python  
- **Library:** Pygame (for GUI)

### 2. 8-Puzzle Solver
- **Algorithm:** A* Search Algorithm  
- **Description:** A sliding puzzle game where the AI finds the shortest path to solve the puzzle using heuristics (Manhattan distance).  
- **Features:**  
  - Interactive puzzle board  
  - Automated solver visualization  
- **Language:** Python  
- **Library:** Pygame (for GUI)

### 3. Chess AI
- **Algorithm:** Minimax with Alpha-Beta Pruning  
- **Description:** A classic chess game implementation with AI opponent using pruning to optimize decision making.  
- **Features:**  
  - Player vs AI gameplay  
  - Basic move validation and AI strategy  
- **Language:** Python  
- **Library:** Pygame, python-chess (optional for move validation)

---

## Implementation Process

### Common Steps:
1. **Set up the environment:**  
   - Install Python 3.x  
   - Install required libraries:
     ```bash
     pip install pygame python-chess
     ```
   - Clone this repository.

2. **Run the game scripts:**  
   Navigate to each project folder and run the main Python file:
   ```bash
   python tictactoe.py
   python eight_puzzle.py
   python chess_ai.py
