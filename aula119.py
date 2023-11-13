# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listasr');
        print();
        return
    print('Tarefas: ');
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print();

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listasr');
        return
    
    tarefa = tarefas.pop();
    print(f'{tarefa=} removida da lista');
    tarefas_refazer.append(tarefa);
    print();

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para listasr');
        return
    
    tarefa = tarefas_refazer.pop();
    tarefas.append(tarefa);
    print(f'{tarefa=} adicionada na lista');
    print();

def adicionar(tarefa, tarefas):
    print();
    tarefa = tarefa.strip();
    if not tarefa:
        print('Você não digitou uma tarefa');
        return
    tarefas.append(tarefa);
    print(f'{tarefa=} adicionada na lista');
    print();
def ler(tarefas, caminho_arquivo):
    dados = [];
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe');
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar (tarefas, caminho_arquivo):
    dados = tarefas;
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent = 2, ensure_ascii = False);
    return dados
caminho_arquivo = 'aula119.json';
tarefas = ler([], caminho_arquivo);
tarefas_refazer = [];

while True:
    print('Comandos: listar, desfazer, refazer, clear ou sair');
    tarefa = input('Digite uma tarefa ou comando: ');
    if tarefa == 'listar':
        listar(tarefas);
        salvar(tarefas, caminho_arquivo)
        continue
    if tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer);
        salvar(tarefas, caminho_arquivo)
        continue
    if tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer);
        salvar(tarefas, caminho_arquivo)
        continue
    elif tarefa == 'sair':
        print('Você saiu do sistema');
        salvar(tarefas, caminho_arquivo)
        break;re
    elif tarefa == 'clear':
        os.system('cls'); 
    else:
        adicionar(tarefa, tarefas);
        salvar(tarefas, caminho_arquivo)
        continue