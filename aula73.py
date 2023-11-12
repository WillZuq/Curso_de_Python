"""
Higher order functions
Funçõoes de primeira classe
"""
def saudacao(msg, nome):
    return f'{msg}, {nome} !'
def executa(funcao, *args):
    return funcao(*args)

# v = saudacao_2('Bom dia');
v = executa(saudacao, 'Bom dia', 'Willian');
print(v);
