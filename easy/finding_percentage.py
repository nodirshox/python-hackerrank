n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

asked_student = student_marks[query_name]

avg = 0
for result in asked_student:
    avg += result

avg = format(avg / len(asked_student), '.2f') # Set precision point for average
print(avg)
