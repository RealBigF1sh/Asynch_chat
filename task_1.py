strs = ['разработка', 'сокет', 'декоратор']

for item in strs:
    print(type(item), item)

strs_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    ]

for item in strs_unicode:
    print(type(item), item)