# KBC-GAME-Project
KBC (Kaun Banega Crorepati) game using Python.
# KBC Game
## Introduction
Welcome to the KBC (Kaun Banega Crorepati) Game. This console-based game is inspired by the famous Indian television show. Players answer a series of multiple-choice questions to accumulate a score.

## Code Overview

### 1. Game Data
Python
questions = [
    'Who developed the Python programming language?',
    'What is the latest mission success on the moon in India?',
    'Who is the prime minister of India?'
]

answers = [
    'Guido van Rossum',
    'Chandrayaan-3',
    'Narendra Modi'
]

options = [
    ['Albert', 'Ritchie', 'Guido van Rossum', 'Dennis'],
    ['Chandrayaan-1', 'Chandrayaan-4', 'Chandrayaan-2', 'Chandrayaan-3'],
    ['Narendra Modi', 'Donald Trump', 'Jagan', 'Elon Musk']
]

## 2. Game Functions

### 2.1 `play_game(user_name, questions, answers, options)`

This function initiates a game session for a specific user.

#### Input:

- user_name`: The name of the player.
- questions`: List of questions.
- answers`: List of correct answers.
- options`: List of lists, each containing multiple-choice options for a question.

#### Output:

Returns the user's name and score.

### 2.2 ViewScores(names_and_scores)

This function displays the scores of all players.

#### Input:

- names_and_scores: A dictionary containing player names as keys and their respective scores.

### 2.3 KBC(questions, answers, options)

This function is the main control function for the game, allowing users to play, view scores, or exit.

#### Input:

- questions: List of questions.
- answers: List of correct answers.
- options: List of lists, each containing multiple-choice options for a question.

## 3. Game Execution

python
KBC(questions, answers, options)

## How to Play

1. **Run the Script**
   - Ensure you have Python installed.
   - Run the script in your terminal or command prompt.

2. **Choose an Option**
   - Choose one of the following options:
     - Play (1)
     - View Scores (2)
     - Exit (3)

## Playing the Game

1. **Enter Your Name**
   - Input your name to personalize the game.

2. **Answer Questions**
   - For each question, enter the corresponding option number to make your choice.

3. **Receive Feedback**
   - Receive immediate feedback on each answer.

4. **Final Score**
   - At the end of the game, see your final score.

## Viewing Scores

1. **Choose "View Scores" Option**
   - Select the "View Scores" option to see the names and scores of all players.

## Exiting the Game

1. **Choose "Exit" Option**
   - To end the game, choose the "Exit" option.

Enjoy playing the KBC Game!
