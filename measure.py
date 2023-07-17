import csv
import global_id
import logger


def measure_add(new_measure):
    if not new_measure[0].isdigit():
        id = global_id.next_id('m')
        new_measure.insert(0, id)
    with open('Arec-Bar/measure.csv', 'a', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        data.writerow(new_measure)
    logger.op_logger('measure_add', new_measure[0])


def measure_delete(measure_name):
    measures = list()
    with open('Arec-Bar/measure.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] != measure_name:
                measures.append(line)
    with open('Arec-Bar/measure.csv', 'w', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        for i in range(len(measures)):
            data.writerow(measures[i])
    logger.op_logger('measure_delete', measure_name)


def measure_change(measure_name, change_measure):
    measure_delete(measure_name)
    change_measure.insert(0, measure_name)
    measure_add(change_measure)
    logger.op_logger('measure_change', measure_name)


def measure_list(measure_name):
    with open('Arec-Bar/measure.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == measure_name:
                logger.op_logger('measure_list', measure_name)
                return line[1:]


def measures_show(letter):
    measures = list()
    with open('Arec-Bar/measure.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if letter == 'all':
                measures.append(line)
            if line[1][0].lower() == letter.lower():
                measures.append(line)
    num_dic = {0: 0}
    if not measures:
        logger.op_logger('measures_show', letter, False)
        return num_dic
    measures.sort(key=lambda x: x[1])
    i = 1
    print('')
    for k in range(len(measures)):
        print(f'{i}) {measures[k][1]}')
        num_dic[str(i)] = measures[k][0]
        i += 1
    logger.op_logger('measures_show', letter, True)
    return num_dic


def measure_show(measure_name):
    with open('Arec-Bar/measure.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == measure_name:
                print(f'\nМера измерения: {line[1]}\nОбъём: {line[2]} мл.')
    logger.op_logger('measure_show', measure_name)