import colorama
from colorama import Fore
colorama.init(autoreset=True, convert=True)

ListaUsuários = []


def interface():
    print("\n")
    print(Fore.LIGHTBLUE_EX +
          "+-------------------------------------------------------------------+")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(Fore.LIGHTGREEN_EX +
          "                       EVENTO ANHEMBI 2021                         ", end="")
    print(Fore.LIGHTBLUE_EX + "|")
    print(Fore.LIGHTBLUE_EX +
          "+-------------------------------------------------------------------+")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(Fore.LIGHTCYAN_EX + " 1", end="")
    print(" - Cadastro de novos usuários         ", end="")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(" Nome completo e e-mail   ", end="")
    print(Fore.LIGHTBLUE_EX + "|")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(Fore.LIGHTCYAN_EX + " 2", end="")
    print(" - Usuários cadastrados               ", end="")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(" Ordem de cadastro        ", end="")
    print(Fore.LIGHTBLUE_EX + "|")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(Fore.LIGHTCYAN_EX + " 3", end="")
    print(" - Usuários cadastrados               ", end="")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(" Ordem alfabética         ", end="")
    print(Fore.LIGHTBLUE_EX + "|")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(Fore.LIGHTCYAN_EX + " 4", end="")
    print(" - Verificação de usuários            ", end="")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(" Ordem alfabética         ", end="")
    print(Fore.LIGHTBLUE_EX + "|")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(Fore.LIGHTCYAN_EX + " 5", end="")
    print(" - Remover usuário                    ", end="")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(" Remoção por e-mail       ", end="")
    print(Fore.LIGHTBLUE_EX + "|")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(Fore.LIGHTCYAN_EX + " 6", end="")
    print(" - Alterar nome de usuário cadastrado ", end="")
    print(Fore.LIGHTBLUE_EX + "|", end="")
    print(" Alteração via e-mail     ", end="")
    print(Fore.LIGHTBLUE_EX + "|")
    print(Fore.LIGHTBLUE_EX +
          "+-------------------------------------------------------------------+")
    print("\n")


def opcaoprincipal():
    global numOpcao
    numOpcao = int(input("Insira sua opção: "))


def principal():
    interface()
    opcaoprincipal()


def criarUser():
    global Usuário
    Usuário = {}
    Usuário["Nome"] = input("Digite o nome completo: ")
    Usuário["E-mail"] = input("Digite o e-mail: ")


def opcao1():
    global ListaUsuários
    criarUser()
    ListaUsuários.append(Usuário)
    print(Fore.YELLOW + "Processo concluído com sucesso!")
    return main()


def opcao2():
    print(ListaUsuários)
    print(Fore.YELLOW + "Processo concluído com sucesso!")
    return main()


def opcao3():
    x = sorted(ListaUsuários, key=lambda Usuário: Usuário['Nome'])
    print(x)
    print(Fore.YELLOW + "Processo concluído com sucesso!")
    return main()


def opcao4():
    VerifNome = input("Insira o nome que deseja buscar: ")
    for User in ListaUsuários:
        if User["Nome"] == VerifNome:
            print(Fore.GREEN + "Este usuário faz parte da lista de participantes.")
        else:
            print(Fore.RED + "Este usuário não faz parte da lista de participantes.")
    print(Fore.YELLOW + "Processo concluído com sucesso!")
    return main()


def opcao5():
    RemovUser = input("Insira o e-mail do usuário que deseja remover: ")
    for User in ListaUsuários:
        if User["E-mail"] == RemovUser:
            ListaUsuários.remove(User)
        else:
            print(Fore.LIGHTRED_EX + "Insira um e-mail válido.")
            print("Retornando ao menu principal.")
            return main()
    print(Fore.YELLOW + "Processo concluído com sucesso!")
    return main()


def opcao6():
    global Usuário
    AltUserEmail = input("Insira o e-mail do usuário que deseja renomear: ")
    for User in ListaUsuários:
        if User["E-mail"] == AltUserEmail:
            NovoNome = input("insira o novo nome: ")
            User["Nome"] = NovoNome
        else:
            print(Fore.LIGHTRED_EX + "Insira um e-mail válido.")
            print("Retornando ao menu principal.")
            return main()
    print(Fore.YELLOW + "Processo concluído com sucesso!")
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
