import sys


f = open("grades_summed.in", "r")
g = open("initial_grades.out", "w")


def rotate(li, n):
    return li[n:] + li[:n]


def define():
    try:
        file_content = f.read()
        lines = file_content.strip().split("\n")
        nr = lines.pop(0)
        nr = int(nr)
        nested_sums = []
        g_sums = []
        for grade in lines:
            nested_sums.append(grade.split())
        for i in range(0, len(nested_sums[0])):
            g_sums.append(int(nested_sums[0][i]))
        return nr, g_sums
    except Exception as e:
        print("Error occurred parsing the file:", e)
        sys.exit(0)


def calculate(n=None, sums=None):
    # g.seek(0)
    # g.truncate() daca vrem sa stergem continutul din fisier la fiecare test
    if n is None and sums is None:
        n, sums = define()
    solutions = [-1] * n
    if not 4 <= n <= 100000:
        g.write(str(-1))
        return -1

    try:# pentru a putea scrie None in teste
        if n != len(sums):
            g.write(str(-1))
            return -1
    except TypeError:
        g.write(str(-1))
        return -1

    n_sum = 0
    for s_grade in sums:
        n_sum += int(s_grade)  # suma totala a sumelor celor 2 vecini
    n_sum = n_sum // 2  # suma notelor initiale
    s = n_sum  # copie suma note initiale

    if n % 4 == 0:
        g.write(str(-1))
        return -1

    if n % 4 == 1:
        for i in range(0, n-1):
            if i % 4 == 0 or i % 4 == 1:
                s -= sums[i]
        solutions[n - 1] = s
        i = n-1
        while i-3 >= 0:
            solutions[i - 3] = sums[i] - solutions[i]
            solutions[i - 1] = sums[i - 3] - solutions[i - 3]
            i -= 1
        for initial_grade in solutions:
            if not -1000000000 <= initial_grade <= 1000000000:
                g.write(str(-1))
                return -1
        solutions = rotate(solutions, 1)
        g.write(str(solutions))
        return solutions

    if n % 4 == 3:
        for i in range(0, n - 1):
            if (i % 4 == 0 or i % 4 == 1) and n-i >= 4:
                s -= sums[i]
            elif n-i < 4 and i % 4 == 0:
                s -= sums[i]
        solutions[n - 2] = s
        solutions[0] = sums[n - 2] - solutions[n - 2]
        for i in range(2, n, 2):
            solutions[i] = sums[i - 2] - solutions[i - 2]
        solutions[1] = sums[n - 1] - solutions[n - 1]
        for i in range(3, n, 2):
            solutions[i] = sums[i - 2] - solutions[i - 2]

        for initial_grade in solutions:
            if not -1000000000 <= initial_grade <= 1000000000:
                g.write(str(-1))
                return -1
        solutions = rotate(solutions, 1)
        g.write(str(solutions))
        return solutions

    if n % 4 == 2:
        for i in range(0, n, 6):
            solutions[i + 5] = (sums[i + 5] + sums[i + 3] - sums[i + 1]) // 2
            solutions[i + 4] = (sums[i + 4] + sums[i + 2] - sums[i]) // 2
            solutions[i + 1] = sums[i + 5] - solutions[i + 5]
            solutions[i + 3] = sums[i + 1] - solutions[i + 1]
            solutions[i] = sums[i + 4] - solutions[i + 4]
            solutions[i + 2] = sums[i] - solutions[i]
        for initial_grade in solutions:
            if not -1000000000 <= initial_grade <= 1000000000:
                g.write(str(-1))
                return -1
        solutions = rotate(solutions, 1)
        g.write(str(solutions))
        return solutions


if __name__ == "__main__":
    calculate()
