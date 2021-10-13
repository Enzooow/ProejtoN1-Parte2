ListaNomes = [""]
ListaEmail = [""]

i = 0


def interface():
    global numOpcao
    print("\n")
    print("Evento técnico Anhembi 2021")
    print("1 - Cadastro de novos usuários | Nome completo e e-mail")
    print("2 - Usuários cadastrados | Ordem de cadastro")
    print("3 - Usuários cadastrados | Ordem alfabética")
    print("4 - Verificação de usuários | Busca por nome completo")
    print("5 - Remover usuário | Remoção por e-mail")
    print("6 - Alterar nome de usuário cadastrado | Por e-mail")
    numOpcao = int(input("Insira sua opção: "))
    print("\n")


def opcao1():
    global Nome
    global Email
    Nome = input("Insira o nome completo: ")
    Email = input("Insira o e-mail: ")
    ListaNomes.append(Nome)
    ListaEmail.append(Email)
    print("Processo concluído com sucesso!")
    interface()


def opcao2():
    print(ListaNomes)
    print(ListaNomes)
    interface()


def opcao3():
    print(ListaNomes.sort())
    interface()


while(i == 0):
    interface()
    if numeroOpcao == 1:
        opcao1()
        numeroOpcao = int(input("Escolha sua opção: "))
    elif numeroOpcao == 2:
        opcao2()
        numeroOpcao = int(input("Escolha sua opção: "))
    elif numeroOpcao == 3:
        opcao3()
        numeroOpcao = int(input("Escolha sua opção: "))

else:
    print("Opção inválida! Insira novamente.")


def main():
    interface()


if __name__ == "__main__":
    main()
