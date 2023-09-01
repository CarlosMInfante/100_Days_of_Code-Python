student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

height_total = 0
count = 0
for i in student_heights:
    height_total += i
    # print(height_total)

for i in student_heights:
    count += 1
    # print(count)

average = round(height_total / count)
print(average)
