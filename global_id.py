import csv
import logger


def next_id(title):
    ids = list()
    with open('Arec-Bar/global_id.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if line[0] == title:
                g_id = line[1]
                tmp = [line[0], int(id)+1]
                ids.append(tmp)
            else:
                ids.append(line)
    with open('Arec-Bar/global_id.csv', 'w', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n', delimiter=';')
        for i in range(len(ids)):
            data.writerow(ids[i])
    logger.op_logger('next_id', title, g_id)
    return g_id
