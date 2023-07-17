import csv
import global_id
import logger


def ingredient_add(new_ingredient):
    if not new_ingredient[0].isdigit():
        id = global_id.next_id('i')
        new_ingredient.insert(0, id)
    with open('Arec-Bar/ingredient.csv', 'a', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        data.writerow(new_ingredient)
    logger.op_logger('ingredient_add', new_ingredient[0])


def ingredient_delete(ingredient_name):
    ingredients = list()
    with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] != ingredient_name:
                ingredients.append(line)
    with open('Arec-Bar/ingredient.csv', 'w', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        for i in range(len(ingredients)):
            data.writerow(ingredients[i])
    logger.op_logger('ingredient_delete', ingredient_name)


def ingredient_change(ingredient_name, change_ingredient):
    ingredient_delete(ingredient_name)
    change_ingredient.insert(0, ingredient_name)
    ingredient_add(change_ingredient)
    logger.op_logger('ingredient_change', ingredient_name)


def ingredient_list(ingredient_name):
    with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == ingredient_name:
                logger.op_logger('ingredient_list', ingredient_name)
                return line[1:]


def ingredients_show(type, letter):
    ingredients = list()
    with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if type == 'all' and letter == 'all':
                ingredients.append(line) 
            if type == 'all' and line[2][0].lower() == letter.lower():
                ingredients.append(line)
            if type == 'select' and letter == 'all' and line[7] == '1':
                ingredients.append(line)
            if type == 'select' and line[7] == '1' and line[2][0].lower() == letter.lower():
                ingredients.append(line)
    num_dic = {0: 0}
    if not ingredients:
        logger.op_logger('ingredients_show', letter, False)
        return num_dic
    ingredients.sort(key=lambda x: x[2])
    i = 1
    print('')
    for k in range(len(ingredients)):
        if ingredients[k][7] == '1':
            print(f'{i}) * {ingredients[k][2]} {ingredients[k][1]} {ingredients[k][3]} {ingredients[k][4]}')
        else:
            print(f'{i}) {ingredients[k][2]} {ingredients[k][1]} {ingredients[k][3]} {ingredients[k][4]}')
        num_dic[str(i)] = ingredients[k][0]
        i += 1
    logger.op_logger('ingredients_show', letter, True)
    return num_dic


def ingredient_show(ingredient_name):
    with open('Arec-Bar/ingredient.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == ingredient_name:
                print(f'\nБренд - {line[1]}\nВид - {line[2]}\nКатегория - {line[3]}\nКоличество - {line[4]}\nОстаточная стоимость - {line[5]}')
                if line[6] == '1':
                    print(f'Отслеживание - Да')
                else:
                    print(f'Отслеживание - Нет')
                if line[7] == '1':
                    print(f'В наличии - Да')
                else:
                    print(f'В наличии - Нет')
    logger.op_logger('ingredient_show', ingredient_name)


