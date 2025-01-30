# Stealth-Game
**Stealth Game AI** is a stealth-based simulation where AI guards track the player using **Hidden Markov Models (HMM)** and **Bayesian Inference**. Players must evade detection using cover, distractions, and strategic movement while the AI adapts its patrols dynamically. 

# Stealth Game AI - Hidden Markov Model Player Tracking

📌 **Project Overview**

This project implements an AI-powered stealth game where an AI-controlled guard tracks a player using Hidden Markov Models (HMM) and Bayesian Inference. The AI predicts the player's movements based on sensor data such as footsteps, visual glimpses, and environmental changes.

🎮 **Features**

AI Player Tracking: The AI dynamically updates its belief state using probabilistic reasoning.

Hidden Markov Model (HMM): Used to infer the most probable player position.

Bayesian Inference: Helps refine predictions based on prior knowledge and new observations.

Real-time Decision Making: AI adapts patrol routes and behaviors based on player actions.

Interactive Environment: Players can hide, create distractions, and use the terrain to evade detection.

AI Guards & Random Patrols: Additional guards patrol the map, increasing difficulty.

🛠️ **Technologies Used**

Operating System: macOS

Programming Language: Python 3.11

Libraries: Random, Pygame

Development Environment: VS Code

Execution Platform: Local machine

Screen Cast: Screencastify

🔄 **How It Works**

Player moves stealthily using arrow keys.

AI Guard listens for environmental cues (footsteps, objects, doors opening, etc.).

Forward Algorithm updates AI's real-time probability estimates.

Viterbi Algorithm reconstructs past movements if the player disappears from tracking.

Bayesian Inference continuously refines AI's predictions.

AI Guard adjusts patrols or actively chases the player based on confidence levels.

🚀 **Installation & Running the Game**

*🔹 Install Dependencies*

pip install pygame 

*🔹 Run the Game*

python3 p3.py
