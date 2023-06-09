import json


def write_order_to_json(item, quantity, price, buyer, date):
   

    with open('source_data/orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('source_data/orders.json', 'w', encoding='utf-8', ) as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
       
        json.dump(data, f_in, indent=4, ensure_ascii=False)


write_order_to_json('принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017')
write_order_to_json('сканер', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('компьютер', '5', '40000', 'Sidorov S.S.', '2.05.2019')