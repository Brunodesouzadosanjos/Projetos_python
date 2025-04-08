import os
import time
lista = []
def adicionar():
    adicionar_produto = input('Produto: ')
    lista.append(adicionar_produto)
def apagar():
    try:
        apagar_produto = int(input("Produto que sera apagado, digite o indice: "))
        if apagar_produto in lista:
            del lista[apagar_produto]
    except:
        print('opção incorreta, por favor apenas numeros')
def listar():
    for produto in enumerate(lista):
        indice,nome = produto
        print(indice,nome)


while True == True:
    opcao = input('''
    *******************************************
    *          Lista de compras               * 
    *   [1]Adicionar                          * 
    *   [2]Apagar                             * 
    *   [3]Listar                             *
    *   [4]Sair                               *                                       
    *******************************************
    :   ''')
    if opcao == '4':
        print('Obrigado, até mais!')
        time.sleep(3)
        break
    elif opcao == '1':
        print('Adicionar')
        adicionar()
        time.sleep(2)
        os.system('cls')
    elif opcao == "2":
        print('Apagar')
        apagar()
        time.sleep(2)
        os.system('cls')
    elif opcao == "3":
        print('Listar')
        listar()
    else:
        print("Digite apenas as opções informada")
        time.sleep(2)
        os.system('cls')
    
os.system('cls')

