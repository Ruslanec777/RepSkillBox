# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
if envelop_x > paper_x and envelop_y > paper_y:
    print('ДА')
elif envelop_x > paper_y and envelop_y > paper_x:
    print('ДА')
else:
    print('НЕТ')


paper_x, paper_y = 9, 8
if envelop_x > paper_x and envelop_y > paper_y:
    print('ДА')
elif envelop_x > paper_y and envelop_y > paper_x:
    print('ДА')
else:
    print('НЕТ')


paper_x, paper_y = 6, 8
if envelop_x > paper_x and envelop_y > paper_y:
     print('ДА')
elif envelop_x > paper_y and envelop_y > paper_x:
     print('ДА')

else:
    print('НЕТ')

paper_x, paper_y = 8, 6
if envelop_x > paper_x and envelop_y > paper_y:
    print('ДА')
elif envelop_x > paper_y and envelop_y > paper_x:
    print('ДА')
else:
    print('НЕТ')

paper_x, paper_y = 3, 4
if envelop_x > paper_x and envelop_y > paper_y:
    print('ДА')
elif envelop_x > paper_y and envelop_y > paper_x:
    print('ДА')
else:
    print('НЕТ')

paper_x, paper_y = 11, 9
if envelop_x > paper_x and envelop_y > paper_y:
    print('ДА')
elif envelop_x > paper_y and envelop_y > paper_x:
    print('ДА')
else:
    print('НЕТ')

paper_x, paper_y = 9, 11
if envelop_x > paper_x and envelop_y > paper_y:
    print('ДА')
elif envelop_x > paper_y and envelop_y > paper_x:
    print('ДА')
else:
    print('НЕТ')

#(просто раскоментировать нужную строку и проверить свой код)

# TODO здесь ваш код

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 11, 10, 2 проходит ')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 11, 10, 2 проходит ')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 11, 10, 2 проходит ')
else:
    print('Кирпич с размером 11, 10, 2  не проходит ')

brick_x, brick_y, brick_z = 11, 2, 10
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 11, 2, 10 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 11, 2, 10 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 11, 2, 10 проходит')
else:
    print('Кирпич с размером 11, 2, 10 не проходит')

brick_x, brick_y, brick_z = 10, 11, 2
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 10, 11, 2 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 10, 11, 2 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 10, 11, 2 проходит')
else:
    print('Кирпич с размером 10, 11, 2 не проходит')

brick_x, brick_y, brick_z = 10, 2, 11
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 10, 2, 11 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 10, 2, 11 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 10, 2, 11 проходит')
else:
    print('Кирпич с размером 10, 2, 11 не проходит')

brick_x, brick_y, brick_z = 2, 10, 11
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 2, 10, 11 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 2, 10, 11 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 2, 10, 11 проходит')
else:
    print('Кирпич с размером 2, 10, 11 не проходит')

brick_x, brick_y, brick_z = 2, 11, 10
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 2, 11, 10 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 2, 11, 10 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 2, 11, 10 проходит')
else:
    print('Кирпич с размером 2, 11, 10 не проходит')

brick_x, brick_y, brick_z = 3, 5, 6
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 3, 5, 6 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 3, 5, 6 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 3, 5, 6 проходит')
else:
    print('Кирпич с размером 3, 5, 6 не проходит')

brick_x, brick_y, brick_z = 3, 6, 5
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 3, 6, 5 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпичс размером 3, 6, 5 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 3, 6, 5 проходит')
else:
    print('Кирпич с размером 3, 6, 5 не проходит')

brick_x, brick_y, brick_z = 6, 3, 5
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 6, 3, 5 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 6, 3, 5 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 6, 3, 5 проходит')
else:
    print('Кирпич с размером 6, 3, 5 не проходит')

brick_x, brick_y, brick_z = 6, 5, 3
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 6, 5, 3 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 6, 5, 3 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 6, 5, 3 проходит')
else:
    print('Кирпич с размером 6, 5, 3 не проходит')

brick_x, brick_y, brick_z = 5, 6, 3
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 5, 6, 3 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 5, 6, 3 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 5, 6, 3 проходит')
else:
    print('Кирпич с размером 5, 6, 3 не проходит')

brick_x, brick_y, brick_z = 5, 3, 6
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 5, 3, 6 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 5, 3, 6 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 5, 3, 6 проходит')
else:
    print('Кирпич с размером 5, 3, 6 не проходит')

brick_x, brick_y, brick_z = 11, 3, 6
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 11, 3, 6 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 11, 3, 6 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 11, 3, 6 проходит')
else:
    print('Кирпич с размером 11, 3, 6 не проходит')

brick_x, brick_y, brick_z = 11, 6, 3
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 11, 6, 3 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 11, 6, 3 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 11, 6, 3 проходит')
else:
    print('Кирпич с размером 11, 6, 3 не проходит')

brick_x, brick_y, brick_z = 6, 11, 3
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 6, 11, 3 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 6, 11, 3 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 6, 11, 3 проходит')
else:
    print('Кирпич с размером 6, 11, 3 не проходит')

brick_x, brick_y, brick_z = 6, 3, 11
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 6, 3, 11 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 6, 3, 11 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 6, 3, 11 проходит')
else:
    print('Кирпич с размером 6, 3, 11 не проходит')

brick_x, brick_y, brick_z = 3, 6, 11
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 3, 6, 11 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 3, 6, 11 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 3, 6, 11 проходит')
else:
    print('Кирпич с размером 3, 6, 11 не проходит')

brick_x, brick_y, brick_z = 3, 11, 6
if hole_x > brick_x and hole_y > brick_y:
    print('Кирпич с размером 3, 11, 6 проходит')
elif hole_x > brick_y and hole_y > brick_z:
    print('Кирпич с размером 3, 11, 6 проходит')
elif hole_x > brick_x and hole_y > brick_z:
    print('Кирпич с размером 3, 11, 6 проходит')
else:
    print('Кирпич с размером 3, 11, 6 не проходит')
# (просто раскоментировать нужную строку и проверить свой код)

# коммент
