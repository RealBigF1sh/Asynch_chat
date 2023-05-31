import chardet

strs = ['разработка', 'сокет', 'декоратор']
strs_in_bytes = []

for item in strs:
    item = item.encode('utf-8', errors='namereplace')
    strs_in_bytes.append(item)
    print(item)

for item in strs_in_bytes:
    print(item.decode('ascii', errors='replace'))
    print(item.decode(chardet.detect(item)['encoding']))