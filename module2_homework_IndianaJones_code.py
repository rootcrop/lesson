''' Задание "Слишком древний шифр": Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.

Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)

Пример 1: 9 - число из первой вставки
1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
Пример 2: 11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)
К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движутся на вас (обожаю клише), тем более числа в первой вставке будут попадаться случайно.
Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа.

примеры :
3 - 12
4 - 13
5 - 1423
6 - 121524
7 - 162534
8 - 13172635
9 - 1218273645
10 - 141923283746 '''


p = print;
n = int(input("введите число: "))
result='';
for i in range(1, n):
    #p('#1 i: ',i)
    for i2 in range(i+1, n):
        #p('##2 i2:',i2 )
        if n % (i + i2) == 0:
            result = result + str(i) + str(i2)
            #p('###3 result: ',result, ' because - i: ',i,', i2 : ',i2)

p(result)
