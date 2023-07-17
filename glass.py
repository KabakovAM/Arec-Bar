import csv
import global_id
import logger


def glass_add(new_glass):
    if not new_glass[0].isdigit():
        id = global_id.next_id('g')
        new_glass.insert(0, id)
    with open('Arec-Bar/glass.csv', 'a', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        data.writerow(new_glass)
    logger.op_logger('glass_add', new_glass[0])


def glass_delete(glass_name):
    glasses = list()
    with open('Arec-Bar/glass.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] != glass_name:
                glasses.append(line)
    with open('Arec-Bar/glass.csv', 'w', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        for i in range(len(glasses)):
            data.writerow(glasses[i])
    logger.op_logger('glass_delete', glass_name)


def glass_change(glass_name, change_glass):
    glass_delete(glass_name)
    change_glass.insert(0, glass_name)
    glass_add(change_glass)
    logger.op_logger('glass_change', glass_name)


def glasses_show(letter):
    glasses = list()
    with open('Arec-Bar/glass.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if letter == 'all':
                glasses.append(line)
            if line[1][0].lower() == letter.lower():
                glasses.append(line)
    num_dic = {0: 0}
    if not glasses:
        logger.op_logger('glasses_show', letter, False)
        return num_dic
    glasses.sort(key=lambda x: x[1])
    i = 1
    print('')
    for k in range(len(glasses)):
        print(f'{i}) {glasses[k][1]}')
        num_dic[str(i)] = glasses[k][0]
        i += 1
    logger.op_logger('glasses_show', letter, True)
    return num_dic


def glass_show(glass_name):
    with open('Arec-Bar/glass.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == glass_name:
                print(f'\n{line[1]}')
    logger.op_logger('glass_show', glass_name)
