# Handles the high scores

high_scores_file = "high_scores.txt"
saved_scores = 10


def get_high_scores():
    scores = {}
    with open(high_scores_file) as file:
        for line in file:
            name, score = line.split(",")
            score = int(score)
            scores[name] = score
    return scores


def try_add_score(score):
    scores = get_high_scores()
    