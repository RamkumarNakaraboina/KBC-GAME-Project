#KBC game
questions = [
    'Who created Python?',
    'Python was released publicly in which year?',
    'In Python, which keyword is used to start a function?'
]

answers = [
    'Guido van Rossum',
    '1991',
    'def'
]

options = [
    ['Albert', 'Ritche', 'Guido van Rossum', 'Dennis'],
    ['1991', '1981', '1961', '1971'],
    ['import', 'def', 'function', 'try']
]

# Define the monetary reward for each correct answer
rewards = [1000, 2000, 3000]

def play_game(user_name, questions, answers, options, rewards):
    print(f'Hello {user_name.capitalize()}, Welcome to the KBC game')
    score = 0
    total_reward = 0  # Accumulate the total reward
    for i in range(len(questions)):
        correct_question = questions[i]
        correct_answer = answers[i]
        current_question_options = options[i]
        reward = rewards[i]  # Get the reward for the current question
        print("Question : ", correct_question)
        for index, each_option in enumerate(current_question_options):
            print(index + 1, ") ", each_option, sep="")
        user_answer_index = int(input("Enter your choice : ")) - 1  # Adjusted index
        user_answer = current_question_options[user_answer_index]
        if user_answer == correct_answer:  # Comparing user's answer with correct answer
            print("Correct answer!")
            score += 1
            total_reward += reward  # Add the reward to the total
        else:
            print("Wrong answer!")
            break
    print("Congratulations! You have won a total of $", total_reward)
    return user_name, total_reward


def view_scores(names_and_scores):
    for name, score in names_and_scores.items():
        print(name, " has scored ", score)


def kbc(questions, answers, options, rewards):
    names_and_scores = {}
    while True:
        print("1. Play\n2. View Scores\n3. Exit")
        choice = int(input('Enter your choice : '))
        if choice == 1:
            user_name = input("Enter your name: ")
            username, score = play_game(user_name, questions, answers, options, rewards)
            names_and_scores[user_name] = score
        elif choice == 2:
            view_scores(names_and_scores)
        elif choice == 3:
            break
        else:
            print("Invalid input\nTry again")


kbc(questions, answers, options, rewards)