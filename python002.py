# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

total = 0
student_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
counter = 0
for student_height in student_heights:
  counter += 1
  total += student_height
print(round(total/counter))

# total_heights += student_height
# print(f"{total_heights}  {counter}")
#Write your code below this row 👇




