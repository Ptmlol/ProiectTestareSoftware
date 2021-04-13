import sys


f = open("grades_summed.in", "r")
g = open("initial_grades.out", "w")

try:
    file_content = f.read()
    lines = file_content.strip().split("\n")
    n = lines.pop(0)
    n = int(n)
    nested_sums = []
    sums = []
    solutions = [-1] * n
    for grade in lines:
        nested_sums.append(grade.split())
    for i in range(0, len(nested_sums[0])):
        sums.append(int(nested_sums[0][i]))
except Exception as e:
    print("Error occurred parsing the file:", e)
    sys.exit(0)

n_sum = 0
t1 = 0
t2 = 0
for grade in sums:
    n_sum += int(grade)
n_sum = n_sum // 2
s = n_sum
if n % 4 == 0:
    g.write(str(-1))

if n % 4 == 1:
    for i in range(0, n-1):
        if i % 4 == 0 or i % 4 == 1:
            s -= sums[i]
    solutions[n-1] = s
    i = n-1
    while i-3 >= 0:
        solutions[i-3] = sums[i] - solutions[i]
        solutions[i-1] = sums[i-3] - solutions[i-3]
        i -= 1
    g.write(str(solutions))
    sys.exit()

if n % 4 == 3:
    for i in range(0, n - 1):
        if (i % 4 == 0 or i % 4 == 1) and n-i >= 4:
            s -= sums[i]
        elif n-i < 4 and i % 4 == 0:
            s -= sums[i]
    solutions[n - 2] = s
    solutions[0] = sums[n-2] - solutions[n-2]
    for i in range(2, n, 2):
        solutions[i] = sums[i-2] - solutions[i-2]
    solutions[1] = sums[n-1] - solutions[n-1]
    for i in range(3, n, 2):
        solutions[i] = sums[i - 2] - solutions[i - 2]
    g.write(str(solutions))
    sys.exit()

if n % 4 == 2:
    for i in range(0, n, 6):
        solutions[i+5] = (sums[i+5] + sums[i+3] - sums[i+1])//2
        solutions[i+4] = (sums[i+4] + sums[i+2] - sums[i])//2
        solutions[i+1] = sums[i+5] - solutions[i+5]
        solutions[i+3] = sums[i+1] - solutions[i+1]
        solutions[i] = sums[i+4] - solutions[i+4]
        solutions[i+2] = sums[i] - solutions[i]
    g.write(str(solutions))
    sys.exit()

