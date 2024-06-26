''' Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value, 
которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов, 
заполненную значениями value и возвращать эту матрицу в качестве результата работы. '''
p = print
matrx = []  # list список


def get_matrix(n, m, value):
    matrix_inside = []
    for n in range(1, n + 1):  # start stop step
        # p('#n',n)
        for m in range(1, m + 1):
            # p('#n #m',n,m)
            matrix_inside.append(value)
        # p('#matrix inside',matrix_inside)
        matrx.append(matrix_inside[0:m])
    # matrix_inside.clear()
    # p(matrx)


get_matrix(2, 2, 10)
p(matrx)
