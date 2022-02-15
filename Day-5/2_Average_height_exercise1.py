# Program that calculates by adding all the height from a list of heights

student_heights = input("Input a list of list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# print(student_heights)
len = sum = 0

for i in student_heights:
    sum += i
    len += 1

aver = sum/len

print(round(aver))

