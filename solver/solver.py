def pivot(tableau, row, column):
    n = len(tableau[0])
    m = len(tableau) - 1
    pivot_value = tableau[row][column]
    # print("pivot on [{0},{1}] = {2}".format(row, column, pivot_value))

    for i in range(0, n):
        tableau[row][i] = tableau[row][i] / pivot_value

    for i in range(0, m+1):
        if i != row:
            ratio = tableau[i][column]
            for j in range(0, n):
                tableau[i][j] -= ratio * tableau[row][j]

    # print_tableau(tableau)
    return tableau


def simplex(tableau):
    """
    Takes the problem in tableau form, including slack variables:
        [[0 c^T],
         [b A]]
    """

    n = len(tableau[0])
    m = len(tableau) - 1

    optimal = False
    unbounded = False
    while (not optimal) and (not unbounded):
        pivot_column = 0
        min_value = 0.
        for i in range(1, (n-m)+1):
            if tableau[0][i] < min_value:
                min_value = tableau[0][i]
                pivot_column = i

        if pivot_column == 0:
            optimal = True
            continue

        pivot_row = 0
        min_ratio = -1.
        for i in range(1, m+1):
            if tableau[i][pivot_column] > 0:
                if ((tableau[i][0] / tableau[i][pivot_column]) < min_ratio) or (min_ratio == -1.):
                    min_ratio = (tableau[i][0] / tableau[i][pivot_column])
                    pivot_row = i

        if min_ratio == -1.:
            unbounded = True
            continue
        tableau = pivot(tableau, pivot_row, pivot_column)

    # print("Optimal: {0}, Unbounded: {1}".format(optimal, unbounded))
    return tableau


def print_tableau(tableau):
    print("###")
    for row in tableau:
        s = "["
        for d in row:
            s += "%.2f, " % d
        print(s + "]")
    print("###")
    return


def get_basic_solution(tableau):
    n = len(tableau[0])
    m = len(tableau)
    solution = []

    for c in range(1, n):
        non_zeros = 0
        non_zero = -1
        for r in range(0, m):
            if tableau[r][c] != 0:
                non_zeros += 1
                non_zero = r

        if non_zeros != 1:
            solution.append(0)
        else:
            solution.append(tableau[non_zero][0] / tableau[non_zero][c])
    return solution
