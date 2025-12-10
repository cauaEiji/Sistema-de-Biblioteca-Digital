import struct
import random

FORMATO = "10s50s50si20s"
TAM_REGISTRO = struct.calcsize(FORMATO)
ARQUIVO = "acervo.bin"


def gerar_codigo_livro(titulo, ano):
    primeira_letra = titulo[0].upper()
    numeros = ''.join(str(random.randint(0, 9)) for _ in range(4))
    ultimos_dois = str(ano)[-2:]
    return f"{primeira_letra}{numeros}-{ultimos_dois}"


def ajustar_bytes(texto, tamanho):
    texto = texto.encode('utf-8')
    return texto[:tamanho].ljust(tamanho, b' ')


def cadastrar_livro():
    print("\n=== Cadastro de Livro ===")

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    categoria = input("Categoria: ")

    codigo = gerar_codigo_livro(titulo, ano)

    # Ajustar cada campo para o tamanho fixo
    codigo_b = ajustar_bytes(codigo, 10)
    titulo_b = ajustar_bytes(titulo, 50)
    autor_b = ajustar_bytes(autor, 50)
    categoria_b = ajustar_bytes(categoria, 20)

    # Empacotar (gravar em binário)
    registro = struct.pack(FORMATO, codigo_b, titulo_b, autor_b, ano, categoria_b)

    # Gravar no arquivo
    with open(ARQUIVO, "ab") as f:
        f.write(registro)

    print(f"\nLivro gravado com código: {codigo}")


def ler_acervo():
    """Lê todos os livros do arquivo e retorna uma lista de dicionários"""
    acervo = []

    try:
        with open(ARQUIVO, "rb") as f:
            while True:
                bytes_lidos = f.read(TAM_REGISTRO)
                if not bytes_lidos:
                    break

                codigo_b, titulo_b, autor_b, ano, categoria_b = struct.unpack(FORMATO, bytes_lidos)

                livro = {
                    "codigo": codigo_b.decode().strip(),
                    "titulo": titulo_b.decode().strip(),
                    "autor": autor_b.decode().strip(),
                    "ano": ano,
                    "categoria": categoria_b.decode().strip()
                }
                acervo.append(livro)

    except FileNotFoundError:
        pass  # Retorna lista vazia se não houver arquivo

    return acervo


def listar_livros():
    print("\n=== LISTAGEM DO ACERVO ===")

    try:
        with open(ARQUIVO, "rb") as f:
            while True:
                bytes_lidos = f.read(TAM_REGISTRO)
                if not bytes_lidos:
                    break

                codigo_b, titulo_b, autor_b, ano, categoria_b = struct.unpack(FORMATO, bytes_lidos)

                print("-------------------------------")
                print("Código:   ", codigo_b.decode().strip())
                print("Título:   ", titulo_b.decode().strip())
                print("Autor:    ", autor_b.decode().strip())
                print("Ano:      ", ano)
                print("Categoria:", categoria_b.decode().strip())

    except FileNotFoundError:
        print("Nenhum livro cadastrado ainda.")
