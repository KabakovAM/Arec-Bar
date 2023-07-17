import datetime


def op_logger(op, *data):
    time = datetime.datetime.now().strftime('%d.%m.%y || %H:%M')
    with open('Arec-Bar/log.txt', 'a', encoding='utf_8') as data_input:
        data_input.write(f'{time}; {op} {data}\n')