import json
import os
import itertools

FILE_NAME = 'Score.json'


def format_score(scoreDict=None, scoreStr=None):
    """
    formats the score from str to dict or from dict to str must receive one of the arguments
    :param scoreDict: score dict of 2 players example: {"sagsugi": 5, "dan": 2}
    :param scoreStr: score string of 2 players example: "sagsugi-dan 5-2"
    :return: the formatted score
    """
    if scoreDict:
        p1 = list(scoreDict.keys())[0]
        p2 = list(scoreDict.keys())[1]
        scoreStr = f'{p1}-{p2} {scoreDict[p1]}-{scoreDict[p2]}'
        return scoreStr
    if scoreStr:
        players = scoreStr.split(' ')[0]
        scores = scoreStr.split(' ')[1]
        p1 = players.split('-')[0]
        p2 = players.split('-')[1]
        p1_score = int(scores.split('-')[0])
        p2_score = int(scores.split('-')[1])
        scoreDict = {p1: p1_score, p2: p2_score}
        return scoreDict


def get_score_by_name(name: str):
    """
    returns the wins of one player against all of his opponents
    :param name: name of the player
    :return: a dict of the wins of the player for example: {"itamar": {"dan": 5, "sagsugi":3}}
    """

    f = open(FILE_NAME, 'r')
    data = json.load(f)
    if name not in data:
        return None
    f.close()
    return data[name]


def get_score_by_two_names(p1: str, p2: str) -> dict:
    """
    return the score between two players
    :param p1: player 1 name
    :param p2: player 2 name
    :return: a dict that represents the score. for example: for the score dan-sagsugi 5-3 --> {"dan": 5, "sagsugi": 3}
    """
    p1_score = get_score_by_name(p1)
    p2_score = get_score_by_name(p2)
    if p1 not in p2_score:
        p2_score[p1] = 0
    if p2 not in p1_score:
        p1_score[p2] = 0
    return {p1: p1_score[p2],
            p2: p2_score[p1]}


def update_player_score(score_dict: dict):
    """
    :param p1: player1 name
    :param p2: player2 name
    :param score_dict: updated score wins dict example:
    for the score itamar(p1)-sagsugi(p2) 10-2 --> {"itamar": 10, "sagsugi": 2}
    """
    players = list(score_dict.keys())
    p1 = players[0]
    p1_score = score_dict[p1]
    p2 = players[1]
    p2_Score = score_dict[p2]
    f = open(FILE_NAME, 'r')
    data = json.load(f)

    if p1 not in data:
        data[p1] = {}
    if p2 not in data:
        data[p2] = {}

    if p2 not in data[p1]:
        data[p1][p2] = 0
    if p1 not in data[p2]:
        data[p2][p1] = 0

    data[p1][p2] = data[p1][p2] + score_dict[p1]
    data[p2][p1] = data[p2][p1] + score_dict[p2]
    f.close()

    os.remove(FILE_NAME)
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=6)
    print("score file updated successfully")


def get_all_scores():
    with open(FILE_NAME, 'r') as f:
        data = json.load(f)
    return data

def show_all_scores():
    scoreResponse = "Scores List: \n"
    scores = get_all_scores()
    players = list(scores.keys())
    combinations = list(itertools.combinations(players, 2))
    result = ['-'.join(combination) for combination in combinations]
    for player_pair in result:
        p1 = player_pair.split('-')[0]
        p2 = player_pair.split('-')[1]
        score = get_score_by_two_names(p1, p2)
        if score[p1] == 0 and score[p2] == 0:
            continue
        scoreStr = format_score(scoreDict=score)
        scoreResponse += f"{scoreStr} \n"

    return scoreResponse



