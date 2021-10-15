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
    print("Processo concluído com sucesso!")
    return main()


def opcao3():
    print(sorted(Lista))
    print("Processo concluído com sucesso!")
    return main()


def opcao4():
    VerifNome = input("Insira o nome que deseja buscar: ")
    if VerifNome in Lista:
        print("Este usuário faz parte da lista de participantes.")
    else:
        print("Este usuário não faz parte da lista de participantes.")
    print("Processo concluído com sucesso!")
    return main()


def opcao5():
    RemovUser = input("Insira o e-mail do usuário que deseja remover: ")
    Lista.pop(RemovUser)
    print("Processo concluído com sucesso!")
    return main()


def opcao6():
    AltUserEmail = input("Insira o e-mail do usuário que deseja renomear: ")
    AltUserNome = input("Insira o novo nome: ")
    Lista[AltUserNome] = AltUserEmail
    print("Processo concluído com sucesso!")
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
        opcao4()
    elif numOpcao == 5:
        opcao5()
    elif numOpcao == 6:
        opcao6()


if __name__ == "__main__":
    main()
