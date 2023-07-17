import csv
import logger


def menu_exc(num, n, type):
    if num.isdigit() and 0 <= int(num) <= n:
        logger.op_logger('menu_exc', num, type, True)
        return True
    logger.op_logger('menu_exc', num, type, False)
    return False


def id_check(id_с, num_dic):
    if id_с.isdigit():
        if id_с in num_dic and int(id_с) != 0:
            logger.op_logger('id_check', id_с, True)
            return num_dic[id_с]
    logger.op_logger('id_check', id_с, False)
    return 0


def search_exc(search, file_path):
    with open(file_path, 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in data:
            if file_path == 'Arec-Bar/ingredient.csv':
                if line[2].lower() == search.lower():
                    logger.op_logger('search_exc', search, file_path, True)
                    return line[0]
            else:
                if line[1].lower() == search.lower():
                    logger.op_logger('search_exc', search, file_path, True)
                    return line[0]
        logger.op_logger('search_exc', search, file_path, False)
        return 0


def delete_check(id_d, type):
    if type == 'glass':
        with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
            data = csv.reader(data_output, lineterminator='\n', delimiter=';')
            for line in data:
                if line[2] == id_d:
                    logger.op_logger('delete_check', id_d, type, False)
                    return False
    if type == 'measure':
        with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
            data = csv.reader(data_output, lineterminator='\n', delimiter=';')
            for line in data:
                for i in range(7, len(line), 3):
                    if line[i] == id_d:
                        logger.op_logger('delete_check', id_d, type, False)
                        return False
    if type == 'ingredient':
        with open('Arec-Bar/cocktail.csv', 'r', encoding='utf-8') as data_output:
            data = csv.reader(data_output, lineterminator='\n', delimiter=';')
            for line in data:
                for i in range(5, len(line), 3):
                    if line[i] == id_d:
                        logger.op_logger('delete_check', id_d, type, False)
                        return False
    logger.op_logger('delete_check', id_d, type, True)
    return True
