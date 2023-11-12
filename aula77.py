# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_acertos = 0;
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta']);
    print();
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}');
        print();
    entrada = input('Digite a resposta: ');
    acertou = False;
    entrada_int = None;
    qtd_opcoes = len(pergunta['Opções']);
    if entrada.isdigit():
        entrada_int = int(entrada);
        if entrada_int >= 0 and entrada_int < qtd_opcoes:
            if pergunta['Opções'][entrada_int] == pergunta['Resposta'] :
                acertou = True;
                qtd_acertos += 1;
    if acertou:
        print('VOCÊ ACERTOU ')
    else:
        print('VOCÊ ERROU!');
    print();
print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas');
