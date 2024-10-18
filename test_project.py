from project import generate_word,save,exit_game,check_input
from player import Player
from unittest.mock import patch
import csv

def test_generate_word():
    assert isinstance(generate_word(),str)
    assert (generate_word()).isalpha()

def test_check_input():
    assert check_input('c',"cat") == True
    assert check_input('a',"cat") == True
    assert check_input('t',"cat") == True
    assert check_input('b',"cat") == False
    assert check_input('ca',"cat") ==False
    assert check_input('?',"cat") == True

def test_save():
    player_name = "Test_save"
    player = Player(player_name)
    save(player)

    found = False
    with open("score/score.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == player_name:
                found = True
                assert int(row[1]) == player.score
                break

    assert found



def test_exit_game():
    player = Player("Test_exit")
    with patch('sys.exit') as mock_exit:
        exit_game(player)
        mock_exit.assert_called_once_with(0)

#remove test cases from the database
    players = []
    with open("score/score.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            players.append({'name': row[0], 'score': int(row[1])})

    with open("score/score.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'score'])  # Write the header
        for p in players[:-2]:
            writer.writerow([p['name'], p['score']])