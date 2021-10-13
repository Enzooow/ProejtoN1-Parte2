Lista = {
    "Nomes": "",
    "E-mail": ""
}


def opções():
    print("Evento técnico Anhembi 2021")
    print("1 - Cadastro de novos usuários | Nome completo e e-mail")
    print("2 - Usuários cadastrados | Ordem de cadastro")
    print("3 - Usuários cadastrados | Ordem alfabética")
    print("4 - Verificação de usuários | Busca por nome completo")
    print("5 - Remover usuário | Remoção por e-mail")
    print("6 - Alterar nome de usuário cadastrado | Por e-mail")


def interface():
    opções()
    Opcao = 0
    interface.Opcao = int(input("Escolha sua opção: "))


if interface.Opcao == 1:
    Nome = input("Insira o nome completo: ")
    Email = input("Insira o e-mail: ")
    Lista["Nomes"] = Nome
    Lista["E-mail"] = Email
    print("Processo concluído com sucesso!")
    interface()

elif interface.Opcao == 2:
    print(Lista["Nomes", "E-mail"])
    interface()


def main():
    interface()


if __name__ == "__main__":
    main()
