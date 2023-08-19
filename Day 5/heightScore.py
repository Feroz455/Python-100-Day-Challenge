import random
scores = []
heighest = 0
for i in range(10):
    scores.append(random.randint(500, 1000))
    if scores[i] > heighest:
        heighest = scores[i]
print(scores)
print(heighest)
