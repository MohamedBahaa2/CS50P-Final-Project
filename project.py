import argparse,sys,csv
from pyfiglet import Figlet
from player import Player
from random_word import RandomWords
from tabulate import tabulate
import random

hinted = set()

def main():
        #Deal with terminal input
    parser = argparse.ArgumentParser(description = "Hangman Game")
    parser.add_argument("-n", default = "",help = "Python project.py -n Name",type = str)

    args = parser.parse_args()
    name = args.n
    if not name:
        sys.exit("-n name argument is required")
    current_player = Player(name)

        #start game menu
    f = Figlet(font = 'larry3d')
    print(f.renderText("Hangman"))
    while True:
        print(current_player)
        print("""
    > Press enter to start game
    > Enter s to go to save and go to the score menu
    > Enter q to save and exit""")

        entry = input()
        if entry not in ['','s','q']:
            print("\nInvalid Input!\n")
        elif not entry:
            word = generate_word()
            current_state = hash_word(word)
            lives = 10
            used = list()
            print("> For hints press '?'")
            while True:
                if '_' in current_state:
                    print('\t',*current_state,'\n')
                    char = input("Guess:")
                    if len(char)>1:
                        print("please enter a single character\n")
                    elif char in used:
                        print("Key already used!")
                    elif char == '?':
                        check_input(char,word)
                    elif check_input(char,word):
                        for i in range(len(word)):
                            if char == word[i]:
                                current_state[i] = char
                                used.append(char)
                    else:
                        if char in used:
                            print("Key already used!")
                        elif lives > 0:
                            lives -=1
                            used.append(char)
                            print(f"\nWrong input, left attempts: {lives}")
                        else:
                            print(f.renderText("Game-over"))
                            print(f"The word was: {word}\n")
                            exit_game(current_player)
                else:
                    current_player.score += 10
                    print(*current_state)
                    print(f"\n> Correct!\n> Current score:  {current_player.score}\n")
                    break

        elif entry.lower() == 's':
                save(current_player)
                players = []

                with open("score/score.csv", "r") as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        players.append({'name': row[0], 'score': int(row[1])})

                players.sort(key=lambda x: x['score'], reverse=True)

                table_data = []
                for idx, player in enumerate(players, start=1):
                    table_data.append([idx, player['name'], player['score']])

                print(tabulate(table_data, headers=["Rank", "Name", "Score"], tablefmt="grid"))


        elif entry.lower() == 'q':
            exit_game(current_player)


def generate_word():
    r = RandomWords()
    word = r.get_random_word()
    return word


def hash_word(word):
    char_list = list(word)
    hashed_list = []
    for _ in char_list:
        hashed_list.append('_')
    return hashed_list

def check_input(c,word):
    if len(c) == 1:
        if c == '?':
            global hinted
            while True:
                hint = word[random.randint(0,len(word)-1)]
                if hint in hinted:
                    continue
                else:
                    print(hint)
                    hinted.add(hint)
                    return True
        else:
            for char in word:
                if c == char:
                    return True
    return False

def exit_game(player):
    if player.score >= player.high_score:
        save(player)
        print(f"\nNew High Score: {player.score}")

    print("\nThank you for playing my game!\n")
    sys.exit(0)


def save(player):

    players = []

    with open("score/score.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            players.append({'name': row[0], 'score': int(row[1])})


    player_found = False
    for p in players:
        if p['name'] == player.name:
            if player.score > p['score']:
                p['score'] = player.score  # Update to higher score
            player_found = True
            break


    if not player_found:
        players.append({'name': player.name, 'score': player.score})


    players.sort(key=lambda x: x['score'], reverse=True)


    with open("score/score.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'score'])  # Write the header
        for p in players:
            writer.writerow([p['name'], p['score']])


if __name__ == "__main__":
    main()