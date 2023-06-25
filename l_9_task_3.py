"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. 
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном 
формате (использовать модуль tabulate).
"""


from tabulate import tabulate
from l_9_task_2 import host_range_ping


def host_range_ping_tab():
    reachable, unreachable = host_range_ping()
    res_dict = {
        'Доступные узлы': reachable,
        'Недоступные узлы': unreachable
    }

    print(tabulate(res_dict, headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == '__main__':
    host_range_ping_tab()

"""
Введите начальный адрес: 192.168.0.1
Сколько адресов проверить: 3
|  Доступные узлы  |  Недоступные узлы  |
|:----------------:|:------------------:|
|   192.168.0.1    |    192.168.0.2     |
|                  |    192.168.0.3     |
"""