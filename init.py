import lib
import cadastro_cliente
import cadastro_pedido

print("-" * 100)
print("Bem vindo ao programa para pedidos de clientes")
print("-" * 100)

while (True):
    print("Selecione uma das opções abaixo:\n")
    print("1 - Cadastro de clientes")
    print("2 - Lista de clientes")
    print("3 - Cadastro de pedidos")
    print("4 - Lista de pedidos")
    print("5 - Sair\n")

    opcao = input("Escolha uma opção:\n")

    if opcao == "1":
        cadastro_cliente.cadastrar()
    elif opcao == "2":
        cadastro_cliente.listar()
    elif opcao == "3":
        cadastro_pedido.cadastrar()
    elif opcao == "4":
        cadastro_pedido.listar()
    elif opcao == "5":
        break
    else:
        lib.mensagem("Opção inválida")
        
    lib.limpar_tela