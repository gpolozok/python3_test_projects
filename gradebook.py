# lists to organize subjects and scores

# grades from last semester
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# list filled with the classes are taking
subjects = ['physics', 'calculus', 'poetry', 'history']

# list filled with grades
grades = [98, 97, 85, 88]

# add computer science grade
subjects.append('computer science')
grades.append(100)

# combine subjects and grades
gradebook = list(zip(subjects, grades))

# add visual arts grade
gradebook.append(['visual arts', 93])

print(gradebook)

# combine the current gradebook and the gradebook from the last semester
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
