import random

order = ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
         'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors',
         'snake', 'human', 'tree']


def game_result(game_order, user_choice, computer_choice):
    if user_choice == computer_choice:
        return f'There is a draw {user_choice}', 50

    user_choice_index = game_order.index(user_choice, 7)
    lower = game_order[user_choice_index + 1:user_choice_index + 8]
    if computer_choice in lower:
        result = f'Well done. Computer chose {computer_choice} and failed', 100
    else:
        result = f'Sorry but computer chose {computer_choice}', 0

    return result


def get_scores():
    ratings = open('rating.txt').readlines()
    scores = {}
    for rating in ratings:
        player, score = rating.strip().split(' ')
        scores[player] = int(score)
    return scores


def save_scores(scores):
    with open('rating.txt', 'w') as f:
        for name, score in scores.items():
            f.write(f'{name} {score}\n')


def main():
    player_name = input('Enter your name: > ')
    print(f'Hello {player_name}')
    game_options = input('> ').strip().split(',')

    # filter invalid options entered by user
    game_options = [option for option in game_options if option.lower() in order]

    # initialize game with default options
    if not game_options:
        game_options = ['rock', 'paper', 'scissors']

    # build order based on input from user
    game_order = []
    for option in order:
        if option in game_options:
            game_order.append(option)
        else:
            game_order.append('')

    game_order *= 3
    all_scores = get_scores()
    player_score = all_scores.get(player_name, 0)

    print("Okay, let's start")
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
            message, score = game_result(game_order, user_choice, computer_choice)
            print(message)
            player_score += score
        else:
            print('Invalid Input')


if __name__ == "__main__":
    main()
