import random

def game():
    user_score = 0
    computer_score = 0
    for i in range(3):
        computer_choice = random.choice(['Schere', 'Stein', 'Papier'])
        user_choice = input('your choice is=')

        print(f'computer choice:{computer_choice}')
        if computer_choice == 'Schere':
            if user_choice == 'Stein':
                user_score += 1
            if user_choice == 'Papier':
                computer_score += 1

        if computer_choice == 'Stein':
            if user_choice == 'Papier':
                user_score += 1
            if user_choice == 'Schere':
                computer_score += 1

        if computer_choice == 'Papier':
            if user_choice == 'Schere':
                user_score += 1
            if user_choice == 'Stein':
                computer_score += 1

        print(f'your score:{user_score}')
        print(f'your opponent score:{computer_score}')

    if user_score == computer_score:
        print('No one won!')
    else:
        if user_score > computer_score:
            print('You have won')
        else:
            print('The computer has won')



game()

