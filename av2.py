clientes = {}

print("Menu")
print("1 - Cadastrar um cliente\n2 - Pesquisar cliente\n3 - Alterar cliente\n4 - Deletar um cliente\n5 - Sair")
decisao = int(input("\nEscolha uma opção: "))

while (decisao != 5):
    if (decisao == 1):
        cpf = str(input("Digite o CPF do cliente: "))
        nome = str(input("Digite o nome do cliente: "))
        telefone = str(input("Digite o telefone do cliente: "))

        clientes.update({cpf: {'nome': nome, 'telefone': telefone}})

    elif (decisao == 2):
        cpf = input("\nDigite o CPF do cliente: ")
        print(f"\n{clientes.get(cpf, 'CPF não encontrado.')}")

    elif (decisao == 3):
        cpf = str(input("\nDigite o CPF do cliente: "))
        resultado = clientes.get(cpf, False)
        if resultado:
            escolha = int(input("ALterar\n1 - Nome\n2 - Telefone\n3 - Sair\nEscolha uma das opções: "))
            if (escolha == 1):
                novoNome = input("Digite o novo nome do cliente: ")
                clientes[cpf].update({'nome': novoNome})
                print('Nome atualizado.')
            elif (escolha == 2):
                novoTelefone = input("Digite o novo telefone do cliente: ")
                clientes[cpf].update({'telefone': novoTelefone})
                print("Telefone atualizado")
            elif (escolha == 3):
                continue
            else:
                print("Opção Inválida.")
        else:
            print("\nCPF não encontrado.")

    elif (decisao == 4):
        cpf = str(input("\nDigite o CPF do cliente para removê-lo: "))
        resultado = clientes.get(cpf, False)
        if resultado:
            del clientes[cpf]
            print("\nCliente removido.")
        else:
            print("\nCPF não encontrado.")

    else:
        print("\nOpção inválida.")

    print("\nMenu")
    print("1 - Cadastrar um cliente\n2 - Pesquisar cliente\n3 - Alterar cliente\n4 - Deletar um cliente\n5 - Sair")
    decisao = int(input("\nEscolha uma opção: "))