# 📌 AI-Powered Tic-Tac-Toe Game  
Welcome to **AI-Powered Tic-Tac-Toe**, a Python-based game where you play against an unbeatable AI using the **Minmax algorithm**. The AI strategically selects the best moves, ensuring a competitive challenge every time!  

---

## 📖 Table of Contents  
- [🎮 How to Play](#-how-to-play)  
- [🛠 Features](#-features)  
- [📂 Project Structure](#-project-structure)  
- [🧠 Minimax Algorithm Explained](#-minimax-algorithm-explained)  
- [🚀 Getting Started](#-getting-started)  
- [🤖 AI Strategy](#-ai-strategy)  
- [📜 License](#-license)  
- [👨‍💻 Author](#-author)  

---

## 🎮 How to Play  
1. Run the script, and the game will start.  
2. You (the human player) will play as **'X'**, while the AI plays as **'O'**.  
3. Input your move by selecting a **row (0-2)** and a **column (0-2)**.  
4. The AI will respond with its move automatically.  
5. The game continues until either:  
   - A player wins 🏆  
   - The board is full (resulting in a draw 🤝)  
6. To **quit** anytime, type `'c'`.  

---

## 🛠 Features  
✅ **Human vs. AI Gameplay** – Play against an AI that makes optimal moves.  
✅ **Unbeatable AI** – The AI uses the **Minimax algorithm**, ensuring it never loses.  
✅ **Simple CLI Interface** – Just run the script and start playing!  
✅ **Error Handling** – Prevents invalid inputs and occupied cell selections.  

---

## 📂 Project Structure  
```
📂 AI_TicTacToe  
 ├── tic_tac_toe.py  # Main game script  
 ├── README.md       # Documentation  
 ├── LICENSE         # Project License  
```

---

## 🧠 Minimax Algorithm Explained  
The **Minimax algorithm** is a decision-making algorithm used in game theory. It simulates all possible game moves and assigns a score based on the outcome:  
- **+10** → AI Wins  
- **-10** → Human Wins  
- **0** → Draw  

The AI maximizes its chances of winning while minimizing the player's chances.  

🔹 **Base Cases:**  
- If AI wins → **Return +10**  
- If Human wins → **Return -10**  
- If Draw → **Return 0**  

🔹 **Recursive Steps:**  
1. The AI tries **all possible moves**.  
2. It simulates the game after each move.  
3. It picks the **best move** based on the Minimax evaluation.  

---

## 🚀 Getting Started  

### 🔧 Prerequisites  
Ensure you have **Python 3.x** installed on your system.  

### 🏃 Run the Game  
```bash
python3 tic_tac_toe.py
```

---

## 🤖 AI Strategy  
- The AI **always plays optimally** and never makes a mistake.  
- If there’s a **winning move**, it takes it.  
- If the player has a **winning move next turn**, it blocks it.  
- If no immediate wins or threats, it **chooses the best long-term move**.  

🚨 **Warning**: The AI **cannot be beaten** because it always finds the best move using Minimax!  

---

## 📜 License  
This project is **open-source** and licensed under the [MIT License](LICENSE).  

---

## 👨‍💻 Author  
Developed by **Owais Khawaja** 🚀  

🔗 **GitHub**: [github.com/OWAIS-KHAWAJA-789](https://github.com/OWAIS-KHAWAJA-789)  

🙌 Contributions and feedback are welcome!  

---
