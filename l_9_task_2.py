"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. 
Меняться должен только последний октет каждого адреса. По результатам проверки должно 
выводиться соответствующее сообщение.
"""


from ipaddress import ip_address
from l_9_task_1 import host_ping


def host_range_ping():
    start_ip = input('Введите начальный адрес: ')
    last_oct = int(start_ip.split('.')[3])

    range_ip = int(input('Сколько адресов проверить: '))
    if (last_oct + range_ip) > 254:
        raise ValueError(f'Максимальное число адресов должно быть: {254-last_oct}!')
    
    hosts_list = [str(ip_address(start_ip) + i) for i in range(range_ip)]
    return host_ping(hosts_list)


if __name__ == '__main__':
    reachable, unreachable = host_range_ping()
    for address in reachable:
        print(f'Узел {address} доступен')
    for address in unreachable:
        print(f'Узел {address} недоступен')
    
"""
Введите начальный адрес: 192.168.0.1
Сколько адресов проверить: 3
Узел 192.168.0.1 доступен
Узел 192.168.0.2 недоступен
Узел 192.168.0.3 недоступен
"""