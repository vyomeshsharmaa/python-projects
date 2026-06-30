#1
subjects_studied=["Maths","Science","English","Maths","Python","Science","Biology","English"]
unique_subjects=set(subjects_studied)
print("Original Subjects List:",subjects_studied)
print("Unique Subjects Set:",unique_subjects)



#2
friends_group_a={"Alice","Bob","Charlie","David","Vyomesh"}
friends_group_b={"Charlie","David","Eve","Frank","Grace"}
print(set(friends_group_a).union(set(friends_group_b)))
print(set(friends_group_a).intersection(set(friends_group_b)))
print(set(friends_group_a).difference(set(friends_group_b)))

#3
#unique_subjects[0]