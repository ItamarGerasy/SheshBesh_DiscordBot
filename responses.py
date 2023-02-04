import scoreHandler


def handle_respons(message: str) -> str:
    p_message = message.lower()

    if 'sheshbesh' in p_message and 'show score' in p_message and "-" in p_message:
        player = p_message.split(' ')[-1]
        response = f"{player} Wins:\n"
        print(f'player to show score: {player}')
        score = scoreHandler.get_score_by_name(player)
        if score == None:
            return f'player name {player} has no data'

        for name, wins in score.items():
            response += f"{name} - {wins}\n"
        print(response)
        return response

    if 'sheshbesh' in p_message and 'show score' in p_message and 'all' in p_message:
        return scoreHandler.show_all_scores()

    if p_message == "sheshbesh":
        return "https://cardgames.io/backgammon/"

    if "sheshbesh add score" in p_message:
        # extract relevant information
        scoreStr = " ".join(p_message.split(" ")[3:])
        scoreDict = scoreHandler.format_score(scoreStr=scoreStr)
        scoreHandler.update_player_score(scoreDict)

        p1 = list(scoreDict.keys())[0]
        p2 = list(scoreDict.keys())[1]
        updatedScore = scoreHandler.get_score_by_two_names(p1, p2)
        updatedScoreString = scoreHandler.format_score(scoreDict=updatedScore)
        response = f"players score has been updated: \n {updatedScoreString}"
        return response


