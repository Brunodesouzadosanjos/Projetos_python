import os
import time

import customtkinter as ctk

# Criação da janela principal
app = ctk.CTk()
app.geometry("400x300")
app.title("Lista de Compras")

lista = []  # Lista de produtos

# Funções para adicionar, apagar e listar produtos
def adicionar():
    produto = entry.get()
    if produto:
        lista.append(produto)
        label_status.configure(text=f'Produto "{produto}" adicionado.')
        entry.delete(0, ctk.END)

def apagar():
    try:
        indice = int(entry.get())
        if 0 <= indice < len(lista):
            produto = lista.pop(indice)
            label_status.configure(text=f'Produto "{produto}" apagado.')
        else:
            label_status.configure(text="Índice inválido.")
    except ValueError:
        label_status.configure(text="Por favor, insira um número válido.")
    entry.delete(0, ctk.END)

def listar():
    texto = "\n".join([f"{i} - {prod}" for i, prod in enumerate(lista)])
    label_lista.configure(text=texto if texto else "Lista vazia.")

# Layout da interface
label_instrucoes = ctk.CTkLabel(app, text="Digite um produto ou índice:")
label_instrucoes.pack(pady=10)

entry = ctk.CTkEntry(app, width=250)
entry.pack(pady=10)

button_adicionar = ctk.CTkButton(app, text="Adicionar Produto", command=adicionar)
button_adicionar.pack(pady=5)

button_apagar = ctk.CTkButton(app, text="Apagar Produto", command=apagar)
button_apagar.pack(pady=5)

button_listar = ctk.CTkButton(app, text="Listar Produtos", command=listar)
button_listar.pack(pady=5)

label_status = ctk.CTkLabel(app, text="")
label_status.pack(pady=10)

label_lista = ctk.CTkLabel(app, text="")
label_lista.pack(pady=10)

# Rodando o aplicativo
app.mainloop()



lista = []#criação de lista vazia para receber os produtos 

#Criando funções para as opções
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

#Criando loop para mander o codigo rodando
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