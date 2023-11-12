# isinstance - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1},{'nome': 'Luiz'}
];

for item in lista:
    if isinstance(item, set):
        item.add(5);
        print('SET');
        print(item, isinstance(item,set));
    elif isinstance(item, (int, float)):
        print ('NUM');
        print(item, item*2);
    elif isinstance(item, str):
        print('STR');
        print(item.upper());
    else:
        print('OUTRO');