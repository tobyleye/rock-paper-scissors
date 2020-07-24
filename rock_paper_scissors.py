import random

decider = {"scissors": "rock", 'rock': 'paper', 'paper': 'scissors'}
game_options = ['scissors', 'rock', 'paper']


def game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        result = (f'There is a draw {user_choice}', 50)
    elif decider[user_choice] == computer_choice:
        result = f'Sorry but computer chose {computer_choice}', 0
    elif decider[computer_choice] == user_choice:
        result = f'Well done. Computer chose {computer_choice} and failed', 100

    return result


def get_scores():
    ratings = open('rating.txt').readlines()
    scores = {}
    for rating in ratings:
        player, score = rating.strip().split(' ')
        scores[player] = score
    return scores


def save_scores(scores):
    with open('rating.txt', 'w') as f:
        for name, score in scores.items():
            f.write(f'{name} {score}\n')


def main():
    player_name = input('Enter your name: > ')
    print(f'Hello {player_name}')

    all_scores = get_scores()
    player_score = all_scores.get(player_name, 0)

    while True:
        user_choice = input().lower()
        if user_choice == '!exit':
            all_scores[player_name] = player_score
            save_scores(all_scores)
            print('Bye!')
            break
        elif user_choice == '!rating':
            print(player_score)
        elif user_choice in game_options:
            computer_choice = random.choice(game_options)
            message, score = game_result(user_choice, computer_choice)
            print(message)
            player_score += score
        else:
            print('Invalid Input')

if __name__ == '__main__':
    print('Running program', 'like we do it in 1995',)
    main()