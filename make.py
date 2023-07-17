import csv
import ingredient
import global_id
import logger

def make_check(cocktail_name, quantity, replace_dic):
    with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == cocktail_name:
                cocktail = line
    measure = {0: 0}
    with open('Arec-Bar/measure.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[2] == 'н/а':
                measure[line[0]] = (1, line[1])
            else:
                measure[line[0]] = (line[2], line[1])
    replace = list()
    for i in range(6, len(cocktail), 3):
        with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
            data = csv.reader(data_output, lineterminator='\n', delimiter=';')
            for line in data:
                if line[0] == cocktail[i] and line[6] == '1' and line[0] not in replace_dic:
                    if line[4] == '' or line[4] == '0' or line[5] == '' or line[5] == '0':
                        print('\nПриготовление коктейля невозможно. Проверте ингредиенты.')
                        return 0
                    volume = round(float(line[4])-float(cocktail[i+1]) * float(measure[cocktail[i+2]][0])*float(quantity))
                    if volume < 0:
                        print(f'\nДля приготовления коктейля не хватает {volume*-1} {measure[cocktail[i+2]][1]} {line[2]} ({line[1]})')
                        line.insert(0, volume*-1)
                        replace = line
                        logger.op_logger('make_check', cocktail_name, quantity, False)
                        return replace
    logger.op_logger('make_check', cocktail_name, quantity, True)
    return replace


def make_cocktail(cocktail_name, quantity, replace_dic):
    with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == cocktail_name:
                cocktail = line
    measure = {0: 0}
    with open('Arec-Bar/measure.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[2] == 'н/а':
                measure[line[0]] = 1
            else:
                measure[line[0]] = line[2]
    ingredients = list()
    total_price = 0
    for i in range(6, len(cocktail), 3):
        with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output_0:
            data_0 = csv.reader(data_output_0, lineterminator='\n', delimiter=';')
            for line_0 in data_0:
                if line_0[0] in replace_dic:
                    with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output_1:
                        data_1 = csv.reader(data_output_1, lineterminator='\n', delimiter=';')
                        for line_1 in data_1:
                            if line_1[0] == replace_dic[line_0[0]]:
                                value = round(float(line_1[4])-float(cocktail[i+1]) * float(measure[cocktail[i+2]])*float(quantity))
                                price = round(float(line_1[5])-float(line_1[5]) / float(line_1[4])*float(cocktail[i+1])*float(quantity))
                                total_price += float(line_1[5]) / float(line_1[4]) * float(cocktail[i+1])*float(measure[cocktail[i+2]])
                                line_1[4] = value
                                line_1[5] = price
                                ingredients.append(line_1)
                elif line_0[0] == cocktail[i] and line_0[6] == '1':
                    value = round(float(line_0[4])-float(cocktail[i+1]) * float(measure[cocktail[i+2]])*float(quantity))
                    price = round(float(line_0[5])-float(line_0[5]) / float(line_0[4])*float(cocktail[i+1])*float(quantity))
                    total_price += float(line_0[5]) / float(line_0[4]) * float(cocktail[i+1])*float(measure[cocktail[i+2]])
                    line_0[4] = value
                    line_0[5] = price
                    ingredients.append(line_0)
    for i in range(len(ingredients)):
        ingredient.ingredient_change(ingredients[i][0], ingredients[i][1:])
    make_list = list()
    id = global_id.next_id('t')
    make_list.extend([id, cocktail[0], cocktail[1], quantity, round(total_price * float(quantity))])
    with open('Arec-Bar/make.csv', 'a', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        data.writerow(make_list)
    print('\nКоктейль успешно приготовлен.')
    logger.op_logger('make_cocktail', cocktail_name, quantity)


def make_replace(make_name, replace):
    with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == make_name:
                ingredient_change = line
    ingredient_change[4] = int(ingredient_change[4]) + int(replace[5])
    ingredient_change[5] = int(replace[6]) + int(ingredient_change[5])
    ingredient.ingredient_change(replace[1], ingredient_change[1:])
    ingredient.ingredient_delete(ingredient_change[0])
    logger.op_logger('make_replace', make_name)


def makes_show(letter):
    makes = list()
    makes_list = list()
    temp = list()
    count = False
    with open('Arec-Bar/make.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            makes.append(line)
    if not makes:
        logger.op_logger('makes_show', letter)
        return count
    makes.sort(key=lambda x: x[1])
    for i in range(len(makes)):
        if len(temp) == 0:
            temp.extend([makes[i][1], makes[i][2], int(makes[i][3]), int(makes[i][4])])
        elif temp[0] == makes[i][1]:
            temp[2] = int(temp[2]) + int(makes[i][3])
            temp[3] = int(temp[3]) + int(makes[i][4])
        else:
            if letter == 'all' or letter == 'top':
                makes_list.append(temp.copy())
            if temp[1][0].lower() == letter.lower():
                makes_list.append(temp.copy())
            temp.clear()
            temp.extend([makes[i][1], makes[i][2], int(makes[i][3]), int(makes[i][4])])
    if letter == 'all' or letter == 'top':
        makes_list.append(temp.copy())
    if temp[1][0].lower() == letter.lower():
        makes_list.append(temp.copy())
    if letter == 'all':
        makes_list.sort(key=lambda x: x[1])
    if letter == 'top':
        makes_list.sort(reverse=True, key=lambda x: x[2])
    print('')
    for i in range(len(makes_list)):
        print(f'{makes_list[i][1]} - {makes_list[i][2]} раз(раза) Сумма: {makes_list[i][3]}')
        count = True
    logger.op_logger('makes_show', letter)
    return count


def make_show(replace):
    replace_list = list()
    with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[3] == replace[4] and line[6] == '1' and int(line[4]) >= replace[0] and line[0] != replace[1]:
                replace_list.append(line)
    num_dic = {0: 0}
    if not replace_list:
        logger.op_logger('make_show', replace, False)
        return num_dic
    replace_list.sort(key=lambda x: x[1])
    i = 1
    print('\nНайдены ингредиенты для замены:\n')
    for k in range(len(replace_list)):
        print(f'{i}) {replace_list[k][1]} {replace_list[k][2]} {replace_list[k][3]} {replace_list[k][4]}')
        num_dic[str(i)] = replace_list[k][0]
        i += 1
    logger.op_logger('make_show', replace, True)
    return num_dic





