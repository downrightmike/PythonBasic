scores = []
result_f = open("results.txt")
for line in result_f:
	(name, score) = line.split()
	acores.append(float(score))
result_f.close()
scores.sort()
scores.reverse()
print("Top scores are: ")
print(scores[0])
print(scores[1])
print(scores[2])

