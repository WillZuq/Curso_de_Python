# Funções decodaradoras e decoradores
# Decorar = Adicionar / remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Pyhton usar as funções decoradoras em outras funçoes
# Decoradores são "Syntax Sugar" (Açucar sintático)
def criar_funcao(func):
    def interna (*args, **kwargs):
        print('Vou te decorar');
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('OK, agora foi decorada');
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string');


invertida = inverte_string('123');
print(invertida)