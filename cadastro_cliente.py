import lib
import csv_sistema
import uuid

filename = "clientes.csv"

def cadastrar():
    lib.limpar_tela
    cliente = {}
    guid = str(uuid.uuid4())
    cliente["id"] = guid
    cliente["nome"] = input("Digite o nome do cliente:\n")
    cliente["telefone"] = input("Digite o telefone do cliente:\n")
    cliente["email"] = input("Digite o email do cliente:\n")

    lista = csv_sistema.ler(filename)
    lista.append(cliente)
    csv_sistema.salvar(lista, filename)
    lib.mensagem("Cliente cadastrado com sucesso!")

def listar():
    lib.limpar_tela()
    lista = csv_sistema.ler(filename)
    print("-" * 100)
    for item in lista:
        print("Nome: " + item["nome"])
        print("Telefone: " + item["telefone"])
        print("Email: " + item["email"])
        print("-" * 100)
    
    input("Digite enter para continuar")
    lib.limpar_tela()

def localiza_cliente():
    lib.limpar_tela()
    lista = csv_sistema.ler(filename)
    print("-" * 100)
    for idx, item in enumerate(lista):
        print("Indice: " + str(idx + 1))
        print("Nome: " + item["nome"])
        print("Telefone: " + item["telefone"])
        print("Email: " + item["email"])
        print("-" * 100)

    indice = input("Digite o indice do cliente:\n")
    cliente = lista[int(indice) - 1]
    if cliente == None:
        lib.mensagem("Cliente não encontrado!")
        localiza_cliente()
    return cliente

