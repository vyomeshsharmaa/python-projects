#1
subjects=["Maths","Science","English","Biology","Python"]
print(subjects[0])
print(subjects[-1])

#2
subjects.append("Finance")
subjects.remove("Biology")
print(subjects)


#3
mock_scores=[88,92,79,95,84]
total=0
for score in mock_scores:
    total+=score

average=total/len(mock_scores)
print("Total Score:",total)
print("Average Score:",average)

for score in mock_scores:
    if score>average:
        print(score,"is above average")
    elif score==average:
        print(score,"is average")
    else:
        print(score,"is below average")


print("Maths" in subjects)
print("Biology" in subjects)




