Lista = {}


def interface():
    print("\n")
    print("Evento técnico Anhembi 2021")
    print("1 - Cadastro de novos usuários | Nome completo e e-mail")
    print("2 - Usuários cadastrados | Ordem de cadastro")
    print("3 - Usuários cadastrados | Ordem alfabética")
    print("4 - Verificação de usuários | Busca por nome completo")
    print("5 - Remover usuário | Remoção por e-mail")
    print("6 - Alterar nome de usuário cadastrado | Por e-mail")
    print("\n")


def opcaoprincipal():
    global numOpcao
    numOpcao = int(input("Insira sua opção: "))


def principal():
    interface()
    opcaoprincipal()


def opcao1():
    global Lista
    Nome = input("Insira seu nome: ")
    Email = input("Insira seu email: ")
    Lista.update({Nome: Email})
    print("Processo concluído com sucesso!")
    return main()


def opcao2():
    print(Lista)
    return main()


def opcao3():
    print(sorted(Lista))
    return main()


def main():
    principal()
    if numOpcao == 1:
        opcao1()
    elif numOpcao == 2:
        opcao2()
    elif numOpcao == 3:
        opcao3()
    elif numOpcao == 4:
        pass
    elif numOpcao == 5:
        pass
    elif numOpcao == 6:
        pass


if __name__ == "__main__":
    main()
