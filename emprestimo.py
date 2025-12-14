import os
import datetime
from biblioteca import listar_livros
from biblioteca import ARQUIVO, FORMATO, TAM_REGISTRO
import struct

emprestados = set()   # códigos dos livros emprestados
def inicializar_emprestados():
    """Lê o histórico de empréstimos e devoluções para reconstruir o conjunto de livros emprestados."""
    global emprestados
    emprestados.clear()
    
    # 1. Adicionar todos que foram emprestados
    if os.path.exists("emprestimos.txt"):
        with open("emprestimos.txt", "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) >= 1:
                    codigo = partes[0]
                    emprestados.add(codigo)
    
    # 2. Remover os que já foram devolvidos (se houver arquivo de devoluções)
    if os.path.exists("devolucoes.txt"):
        with open("devolucoes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) >= 1:
                    codigo = partes[0]
                    if codigo in emprestados:
                        emprestados.remove(codigo)

def carregar_codigos_acervo():
    """Lê o acervo.bin e retorna lista de códigos existentes."""
    codigos = []
    try:
        with open(ARQUIVO, "rb") as f:
            while True:
                dados = f.read(TAM_REGISTRO)
                if not dados:
                    break

                codigo_b, *_ = struct.unpack(FORMATO, dados)
                codigo = codigo_b.decode().strip()
                codigos.append(codigo)
    except FileNotFoundError:
        pass

    return codigos


def registrar_usuario(nome):
    """Adiciona o usuário ao arquivo usuarios.txt sem repetição."""
    usuarios_existentes = set()
    
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linha in f:
                usuarios_existentes.add(linha.strip())
    
    if nome not in usuarios_existentes:
        with open("usuarios.txt", "a", encoding="utf-8") as f:
            f.write(nome + "\n")


def registrar_emprestimo_arquivo(codigo, usuario, data_emp, data_prev):
    """Salva o histórico do empréstimo no arquivo emprestimos.txt."""
    with open("emprestimos.txt", "a", encoding="utf-8") as f:
        linha = f"{codigo};{usuario};{data_emp};{data_prev}\n"
        f.write(linha)


def emprestar_livro():
    print("\n=== REALIZAR EMPRÉSTIMO ===")

    codigo = input("Código do livro: ").strip()
    usuario = input("Nome do usuário: ").strip()

    # 1. Validar se o código existe no acervo
    codigos_acervo = carregar_codigos_acervo()
    if codigo not in codigos_acervo:
        print("Código não existe no acervo.")
        return

    # 2. Verificar se já está emprestado
    if codigo in emprestados:
        print("Este livro já está emprestado.")
        return

    # 3. Gerar datas
    data_emprestimo = datetime.datetime.today()
    data_prevista = data_emprestimo + datetime.timedelta(days=7)

    # 4. Registrar empréstimo (na prática, como tupla — embora seja apenas usado como info interna)
    emprestimo = (codigo, usuario, data_emprestimo, data_prevista)

    # 5. Adicionar ao conjunto de emprestados
    emprestados.add(codigo)

    # 6. Registrar usuário em usuarios.txt
    registrar_usuario(usuario)

    # 7. Registrar empréstimo no arquivo emprestimos.txt
    registrar_emprestimo_arquivo(
        codigo,
        usuario,
        data_emprestimo.strftime("%d/%m/%Y"),
        data_prevista.strftime("%d/%m/%Y"),
    )

    print("\nEmpréstimo realizado com sucesso!")
    print(f"Código: {codigo}")
    print(f"Usuário: {usuario}")
    print(f"Data do empréstimo: {data_emprestimo.strftime('%d/%m/%Y')}")
    print(f"Devolução prevista: {data_prevista.strftime('%d/%m/%Y')}")
