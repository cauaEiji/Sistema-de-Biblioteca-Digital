from biblioteca import cadastrar_livro, listar_livros
from emprestimo import emprestar_livro, inicializar_emprestados


def menu():
    inicializar_emprestados()
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Emprestar livro")
        print('4 - Registrar devolucao')
        print('5 - Buscar livro')
        print('6 - Gerar relatorios')
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_livro()

        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            emprestar_livro()
        elif opcao == "4":
                from devolucao import registrar_devolucao
                registrar_devolucao()
        elif opcao == "5":
            from buscar import menu_busca
            menu_busca()
        elif opcao == "6":
            from relatorios import gerar_relatorios
            gerar_relatorios()

        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
