import sys # pragma: no mutate


f = open("grades_summed.in", "r") # pragma: no mutate
g = open("initial_grades.out", "w") # pragma: no mutate


def rotate(li, n): # pragma: no mutate
    return li[n:] + li[:n] # pragma: no mutate


def print_s(solutions): # pragma: no mutate
    for initial_grade in solutions: # pragma: no mutate
        if not -1000000000 <= initial_grade <= 1000000000: # pragma: no mutate
            g.write(str(-1)) # pragma: no mutate
            return -1 # pragma: no mutate
    solutions = rotate(solutions, 1) # pragma: no mutate
    g.write(str(solutions)) # pragma: no mutate
    return 1 # pragma: no mutate


def define(): # pragma: no mutate
    try: # pragma: no mutate
        file_content = f.read() # pragma: no mutate
        lines = file_content.strip().split("\n") # pragma: no mutate
        nr = lines.pop(0) # pragma: no mutate
        nr = int(nr) # pragma: no mutate
        nested_sums = [] # pragma: no mutate
        g_sums = [] # pragma: no mutate
        for grade in lines: # pragma: no mutate
            nested_sums.append(grade.split()) # pragma: no mutate
        for i in range(0, len(nested_sums[0])): # pragma: no mutate
            g_sums.append(int(nested_sums[0][i])) # pragma: no mutate
        return nr, g_sums # pragma: no mutate
    except Exception as e: # pragma: no mutate
        print("Error occurred parsing the file:", e) # pragma: no mutate
        sys.exit(0) # pragma: no mutate


def calculate(n=None, sums=None):
    # g.seek(0)
    # g.truncate() daca vrem sa stergem continutul din fisier la fiecare test
    try:
        if n is None and sums is None:
            n, sums = define()
        solutions = [-1] * n
        if not 4 <= n <= 100000:
            g.write(str(-1))# pragma: no mutate
            return -1  # pragma: no mutate

        if n != len(sums):
            g.write(str(-1))# pragma: no mutate
            return -1  # pragma: no mutate
    except TypeError:
        g.write(str(-1))# pragma: no mutate
        return -1  # pragma: no mutate

    n_sum = 0
    for s_grade in sums:
        n_sum += int(s_grade)  # suma totala a sumelor celor 2 vecini
    n_sum = n_sum // 2  # suma notelor initiale
    s = n_sum  # copie suma note initiale

    if n % 4 == 0:
        g.write(str(-1))# pragma: no mutate
        return -1  # pragma: no mutate

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
        if print_s(solutions) == 1:
            return rotate(solutions, 1)
        else:
            return -1  # pragma: no mutate

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
        if print_s(solutions) == 1:
            return rotate(solutions, 1)
        else:
            return -1  # pragma: no mutate

    if n % 4 == 2:
        for i in range(0, n, 6):
            solutions[i + 5] = (sums[i + 5] + sums[i + 3] - sums[i + 1]) // 2
            solutions[i + 4] = (sums[i + 4] + sums[i + 2] - sums[i]) // 2
            solutions[i + 1] = sums[i + 5] - solutions[i + 5]
            solutions[i + 3] = sums[i + 1] - solutions[i + 1]
            solutions[i] = sums[i + 4] - solutions[i + 4]
            solutions[i + 2] = sums[i] - solutions[i]
        if print_s(solutions) == 1:
            return rotate(solutions, 1)
        else:
            return -1  # pragma: no mutate


if __name__ == "__main__": # pragma: no mutate
    calculate() # pragma: no mutate
