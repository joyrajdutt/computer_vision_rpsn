def get_prediction(prediction):
    if prediction[0][0] > 0.5:
        player_action = "Rock"
    elif prediction[0][1] > 0.5:
        player_action = "Paper"
    elif prediction[0][2] > 0.5:
        player_action = "Scissors"
    else:
        player_action = "Nothing"
    return player_action