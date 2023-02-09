import lib
import csv_sistema
import uuid
import cadastro_cliente

filename = "pedidos.csv"

def listar():
    lib.limpar_tela()
    lista = csv_sistema.ler(filename)
    print("-" * 100)
    for item in lista:
        print("Id: " + item["id"])
        cliente = csv_sistema.busca_por_id(item["cliente_id"], "clientes.csv")
        print("Cliente: " + cliente["nome"])
        print("Produto: " + item["produto"])
        print("Quantidade: " + item["quantidade"])
        print("Valor unitario: R$" + item["valor_unitario"])
        print("Valor total: R$" + item["valor_total"])
        print("-" * 100)
    
    input("Digite enter para continuar")
    lib.limpar_tela()

def cadastrar():
    lib.limpar_tela
    cliente = cadastro_cliente.localiza_cliente()
    pedido = {}
    guid = str(uuid.uuid4())
    pedido["id"] = guid
    pedido["cliente_id"] = cliente["id"]
    pedido["produto"] = input("Digite o nome do produto:\n")
    pedido["quantidade"] = input("Digite a quantidade:\n")
    pedido["valor_unitario"] = input("Digite o valor unitatio:\n")
    pedido["valor_total"] = float(pedido["quantidade"]) * float(pedido["valor_unitario"])

    lista = csv_sistema.ler(filename)
    lista.append(pedido)
    csv_sistema.salvar(lista, filename)
    lib.mensagem("Pedido cadastrado com sucesso!")

