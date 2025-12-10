from datetime import datetime, timedelta

# conjunto compartilhado (em geral importado do arquivo principal)
from emprestimo import emprestados  

def registrar_devolucao():
    codigo = input("Código do livro para devolução: ")

    # 1. Verificar se o livro está emprestado
    if codigo not in emprestados:
        print("Este livro não está emprestado.")
        return

    # Buscar o empréstimo no arquivo emprestimos.txt
    encontrado = False
    dados_emprestimo = None

    with open("emprestimos.txt", "r", encoding="utf-8") as arq:
        linhas = arq.readlines()

    for linha in linhas:
        partes = linha.strip().split(";")
        if partes[0] == codigo:
            usuario = partes[1]
            data_emp = datetime.strptime(partes[2], "%Y-%m-%d")
            data_prev = datetime.strptime(partes[3], "%Y-%m-%d")
            encontrado = True
            break

    if not encontrado:
        print("Erro: empréstimo não encontrado no arquivo.")
        return

    # 2. Data real da devolução
    data_real = datetime.today()

    # 3. Calcular atraso
    atraso = (data_real - data_prev).days
    atraso = atraso if atraso > 0 else 0

    # 4. Calcular multa
    multa = atraso * 0.50

    print("\n📘 Livro devolvido!")
    print(f"Usuário: {usuario}")
    print(f"Data empréstimo: {data_emp.date()}")
    print(f"Data prevista: {data_prev.date()}")
    print(f"Data devolução: {data_real.date()}")
    print(f"Atraso: {atraso} dias")
    print(f"Multa: R$ {multa:.2f}")

    # Registrar devolução
    with open("devolucoes.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{codigo};{usuario};{data_emp.date()};{data_prev.date()};{data_real.date()};{atraso};{multa:.2f}\n")

    # 5. Remover do conjunto emprestados
    emprestados.remove(codigo)
    print("\nLivro marcado como devolvido!\n")
