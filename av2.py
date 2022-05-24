def format_telefone(tel):
    telefone = "({}) {}-{}".format(tel[0] + tel[1], tel[2] + tel[3] + tel[4] + tel[5] + tel[6],tel[7] + tel[8] + tel[9] + tel[10])
    return telefone

clientes = {}

print("Menu")
print("1 - Cadastrar um cliente\n2 - Pesquisar cliente\n3 - Alterar cliente\n4 - Deletar um cliente\n5 - Sair")
decisao = int(input("\nEscolha uma opção: "))

while (decisao != 5):
    if (decisao == 1):
        email = str(input("\nDigite o E-mail do cliente: "))
        nome = str(input("Digite o nome do cliente: "))
        nome = nome.capitalize()
        telefone_nao_formatado = input("Digite o telefone do cliente: ")
        telefone = format_telefone(telefone_nao_formatado)

        clientes.update({email: {'nome': nome, 'telefone': telefone}})

    elif (decisao == 2):
        email = input("\nDigite o E-mail do cliente: ")
        if (email in clientes):
            print(f"Nome: {clientes[email]['nome']}\nTelefone: {clientes[email]['telefone']}")
        else:
            print("E-mail não encontrado.")

    elif (decisao == 3):
        email = str(input("\nDigite o E-mail do cliente: "))
        resultado = clientes.get(email, False)
        escolha = 1

        while (escolha != 3):
            if resultado:
                escolha = int(input("\nAlterar\n\n1 - Nome\n2 - Telefone\n3 - Sair\n\nEscolha uma das opções: "))
                if (escolha == 1):
                    novoNome = input("\nDigite o novo nome do cliente: ")
                    clientes[email].update({'nome': novoNome})
                    print('Nome atualizado.')
                elif (escolha == 2):
                    novoTelefone = input("Digite o novo telefone do cliente: ")
                    clientes[email].update({'telefone': novoTelefone})
                    print("Telefone atualizado")
                elif (escolha == 3):
                    continue
                else:
                    print("Opção Inválida.")
            else:
                print("\nCPF não encontrado.")

    elif (decisao == 4):
        email = str(input("\nDigite o E-mail do cliente para removê-lo: "))
        resultado = clientes.get(email, False)
        if resultado:
            del clientes[email]
            print("\nCliente removido.")
        else:
            print("\nE-mail não encontrado.")

    else:
        print("\nOpção inválida.")

    print("\nMenu")
    print("1 - Cadastrar um cliente\n2 - Pesquisar cliente\n3 - Alterar cliente\n4 - Deletar um cliente\n5 - Sair")
    decisao = int(input("\nEscolha uma opção: "))