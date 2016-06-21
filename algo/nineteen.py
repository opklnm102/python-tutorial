#5명 등수 출력

scores = []
while not len(scores) == 5:
    score = int(input("input score: "))
    scores.append(score)

seq = 0
for s in scores:
    seq += 1
    rank = 1
    for ss in scores:
        if s < ss:
            rank += 1
    print("%d번째는 %d점, %d등" % (seq, s, rank))