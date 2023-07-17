import csv
import global_id
import textwrap
import logger


def cocktail_add(new_cocktail):
    if not new_cocktail[0].isdigit():
        id = global_id.next_id('c')
        new_cocktail.insert(0, id)
    with open('Arec-Bar/cocktail.csv', 'a', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        data.writerow(new_cocktail)
    logger.op_logger('cocktail_add', new_cocktail[0])


def cocktail_delete(cocktail_name):
    cocktails = list()
    with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] != cocktail_name:
                cocktails.append(line)
    with open('Arec-Bar/cocktail.csv', 'w', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        for i in range(len(cocktails)):
            data.writerow(cocktails[i])
    logger.op_logger('cocktail_delete', cocktail_name)


def cocktail_change(cocktail_name, change_cocktail):
    cocktail_delete(cocktail_name)
    change_cocktail.insert(0,cocktail_name)
    cocktail_add(change_cocktail)
    logger.op_logger('cocktail_change', cocktail_name)


def cocktail_list(cocktail_name):
    with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == cocktail_name:
                return line


def cocktails_show(type, letter, filter):
    cocktails = list()
    with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if type == 'cocktail' and letter == 'all':
                cocktails.append(line)
            if type == 'cocktail' and line[1][0].lower() == letter.lower():
                cocktails.append(line)
            if type == 'select' and letter == 'all' and line[5] == '1':
                cocktails.append(line)
            if type == 'select' and line[1][0].lower() == letter.lower() and line[5] == '1':
                cocktails.append(line)
            if type == 'glass' and letter == 'all' and line[2] == filter:
                cocktails.append(line)
            if type == 'glass' and line[1][0].lower() == letter.lower() and line[2] == filter:
                cocktails.append(line)
            if type == 'ingredient' and letter == 'all':
                for i in range(6, len(line), 3):
                    if line[i] == filter:
                        cocktails.append(line)
            if type == 'ingredient' and line[1][0].lower() == letter.lower():
                for i in range(6, len(line), 3):
                    if line[i] == filter:
                        cocktails.append(line)
    num_dic = {0: 0}
    if not cocktails:
        logger.op_logger('cocktails_show', type, letter, filter, False)
        return num_dic
    cocktails.sort(key=lambda x: x[1])
    i = 1
    print('')
    for k in range(len(cocktails)):
        if cocktails[k][5] == '0':
            print(f'{i}) {cocktails[k][1]}')
        if cocktails[k][5] == '1':
            print(f'{i}) {cocktails[k][1]} *')
        num_dic[str(i)] = cocktails[k][0]
        i += 1
    logger.op_logger('cocktails_show', type, letter, filter, True)
    return num_dic


def cocktail_show(cocktail_name, quantity):
    with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == cocktail_name:
                cocktail = line
                print(f'\n{cocktail[1]}')
                if line[5] == '1':
                    print(f'\nВ списке "Избранное"')
    with open('Arec-Bar/glass.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == cocktail[2]:
                print(f'\nБокал - {line[1]}')
    if cocktail[3] != '':
        print(f'\n{textwrap.fill(cocktail[3],100)}')
    print(f'\nМетод приготовления:\n{textwrap.fill(cocktail[4],100)}')
    if quantity != 1:
        print(f'\n{quantity} порции(ий)')
    print('\nИнгредиенты:')
    measure = {0: 0}
    with open('Arec-Bar/measure.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[2] == 'н/а':
                measure[line[0]] = (line[1],1)
            else:
                measure[line[0]] = (line[1],line[2])
    price = 0
    price_check = True
    for i in range(6, len(cocktail), 3):
        with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
            data = csv.reader(data_output, lineterminator='\n', delimiter=';')
            for ingredient in data:
                if ingredient[0] == cocktail[i]:
                    if ingredient[1] == '':
                        if ingredient[7] == '1':
                            print(f'{ingredient[2]} - {round(float(cocktail[i+1])*float(quantity))} {measure[cocktail[i+2]][0]} *')
                        else:
                            print(f'{ingredient[2]} - {round(float(cocktail[i+1])*float(quantity))} {measure[cocktail[i+2]][0]}')
                    if ingredient[1] != '':
                        if ingredient[7] == '1':    
                            print(f'{ingredient[2]} ({ingredient[1]}) - {round(float(cocktail[i+1])*float(quantity))} {measure[cocktail[i+2]][0]} *')
                        else:
                            print(f'{ingredient[2]} ({ingredient[1]}) - {round(float(cocktail[i+1])*float(quantity))} {measure[cocktail[i+2]][0]}')
                    if ingredient[6] == '1':
                        if ingredient[4] == '0' or (ingredient[5]) == '0' or ingredient[4] == '' or (ingredient[5]) == '':
                            price_check = False
                        else:
                            price += float(ingredient[5]) / float(ingredient[4])*float(cocktail[i+1])*float(measure[cocktail[i+2]][1])
    if price_check == False:
        print(f'\nСтоимость коктейля расчитать невозможно.')
    elif price != 0:
        print(f'\nСтоимость коктейля: {round(price * float(quantity))} рублей')
    logger.op_logger('cocktail_show', cocktail_name, quantity)


def cocktail_ingredients_show(cocktail_name):
    ingredients = list()
    temp = list()
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
                measure[line[0]] = (line[1],1)
            else:
                measure[line[0]] = (line[1],line[2])
    for i in range(6, len(cocktail), 3):
        with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
            data = csv.reader(data_output, lineterminator='\n', delimiter=';')
            for ingredient in data:
                if ingredient[0] == cocktail[i]:
                    temp.extend([i, ingredient[1], ingredient[2], cocktail[i+1], measure[cocktail[i+2]][0]])
                    ingredients.append(temp.copy())
                    temp.clear()
    num_dic = {0:0}
    i = 1
    print('')
    for k in range(len(ingredients)):
        if ingredients[k][1] == '':
            print(f'{i}) {ingredients[k][2]} - {ingredients[k][3]} {ingredients[k][4]}')
        if ingredients[k][1] != '':
            print(f'{i}) {ingredients[k][2]} ({ingredients[k][1]}) - {ingredients[k][3]} {ingredients[k][4]}')
        num_dic[i] = ingredients[k][0]
        i += 1
    logger.op_logger('cocktails_show', cocktail_name, False)
    return num_dic