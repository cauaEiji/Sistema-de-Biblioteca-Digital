from biblioteca import ler_acervo

def buscar_por_titulo(acervo):
    termo = input("Digite parte do título: ").lower()
    encontrados = [livro for livro in acervo if termo in livro["titulo"].lower()]

    if not encontrados:
        print("\nNenhum livro encontrado com esse título.")
    else:
        print("\nResultados:")
        for l in encontrados:
            print(f"{l['codigo']} - {l['titulo']} ({l['autor']}) [{l['categoria']}]")

def buscar_por_autor(acervo):
    termo = input("Nome do autor: ").lower()
    encontrados = [livro for livro in acervo if termo in livro["autor"].lower()]

    if not encontrados:
        print("\nNenhum livro desse autor.")
    else:
        print("\nResultados:")
        for l in encontrados:
            print(f"{l['codigo']} - {l['titulo']} ({l['autor']}) [{l['categoria']}]")

def buscar_por_categoria(acervo):
    categoria = input("Categoria: ").lower()
    encontrados = [livro for livro in acervo if categoria == livro["categoria"].lower()]

    if not encontrados:
        print("\nNenhum livro nessa categoria.")
    else:
        print("\nResultados:")
        for l in encontrados:
            print(f"{l['codigo']} - {l['titulo']} ({l['autor']}) [{l['categoria']}]")

def menu_busca():
    acervo = ler_acervo()  

    print("""
===== BUSCAR LIVROS =====
1 - Buscar por parte do título
2 - Buscar por autor
3 - Buscar por categoria
0 - Voltar ao menu principal
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        buscar_por_titulo(acervo)
    elif opcao == "2":
        buscar_por_autor(acervo)
    elif opcao == "3":
        buscar_por_categoria(acervo)
    else:
        print("Voltando...")
