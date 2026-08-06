def add_bonus(scores, bonus):
    for i in range(len(scores)):
        finish_score = scores[i] + bonus
        scores[i] = int(finish_score)

scores = [70, 85, 90]

add_bonus(scores, 5)

print(scores)