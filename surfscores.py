scores = []
names = []
result_f = open("results.txt")
for line in result_f:
 (name, score) = line.split()
 scores.append(float(score))
 names.append(name)
result_f.close()
scores.sort()
scores.reverse()
names.sort()
names.reverse()
print("Top scores are: ")
print(names[0] + ' ' + str(scores[0]))
print(names[1] + ' ' + str(scores[1]))
print(names[2] + ' ' + str(scores[2]))

