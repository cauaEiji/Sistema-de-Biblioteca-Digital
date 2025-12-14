from biblioteca import ler_acervo
from emprestimo import emprestados

def gerar_relatorios():
    acervo = ler_acervo()
    total_livros = len(acervo)

    # Agrupar livros por categoria [cite: 77]
    categorias = {}
    for livro in acervo:
        cat = livro['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1

    # Contar emprestados e disponíveis [cite: 78]
    # O conjunto 'emprestados' deve estar atualizado (ver alteração no main.py)
    qtd_emprestados = len(emprestados)
    qtd_disponiveis = total_livros - qtd_emprestados
    if qtd_disponiveis < 0: 
        qtd_disponiveis = 0

    # 6.1 - Relatório Geral (relatorio.txt) [cite: 74]
    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO GERAL DA BIBLIOTECA\n\n")
        f.write(f"1. Total de livros cadastrados: {total_livros}\n")
        f.write("2. Livros por categoria:\n")
        if not categorias:
            f.write("   (Nenhum livro cadastrado)\n")
        for cat, qtd in categorias.items():
            f.write(f"   - {cat}: {qtd}\n")
        
        f.write(f"3. Situação dos livros:\n")
        f.write(f"   - Emprestados: {qtd_emprestados}\n")
        f.write(f"   - Disponíveis: {qtd_disponiveis}\n")
        
        # Item 4: Média das avaliações [cite: 79]
        # Como o sistema não possui entrada de notas, preenchemos conforme instrução:
        f.write("4. Média das avaliações por livro:\n")
        f.write("   - sem avaliações\n") 

    # 6.2 - Relatório Rápido (relatorio_rapido.txt) [cite: 80]
    with open("relatorio_rapido.txt", "w", encoding="utf-8") as f:
        for livro in acervo:
            f.write(f"{livro['titulo']}\n")

    print("\nRelatórios (relatorio.txt e relatorio_rapido.txt) gerados com sucesso!")