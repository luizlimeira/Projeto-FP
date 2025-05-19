import json
import os

ARQUIVO_FICHAS = "ficha.json"

# Funções de persistência:
def carregar_fichas():
    if not os.path.exists(ARQUIVO_FICHAS):
        return []
    
    with open(ARQUIVO_FICHAS, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_fichas(fichas):
    with open(ARQUIVO_FICHAS, 'w', encoding='utf-8') as arquivo:
        json.dump(fichas, arquivo, indent=4, ensure_ascii=False)

# Operações CRUD:
def adicionar_ficha(fichas):
    while True:
        print("\n" + "=" * 40)
        print("ADICIONAR NOVA FICHA".center(40))
        print("=" * 40)

        nova_ficha = {
            'categoria': '',
            'nome': '',
            'ingredientes': [],
            'preparo': []
        }

        categoria = input("Categoria: ")
        nova_ficha['categoria'] = categoria

        nome = input("Nome: ")
        nova_ficha['nome'] = nome

        print("\nINGREDIENTES: ")
        while True:
            ingred = input("Ingrediente: ")
            quant = input("Quantidade: ")

            nova_ficha['ingredientes'].append({
                'ingrediente': ingred, 
                'quantidade': quant
            })

            op = input("deseja adiconar  outro ingrediente? (s/n)").lower()
            if op != 's':
                break

        print("\nMODO DE PREPARO:")
        passo_num = 1
        while True:
            descricao = input(f"digite o passo {passo_num}: ")

            nova_ficha['preparo'].append({
                'passo': passo_num,
                'descricao': descricao
            })

            op = input("deseja adiconar  outro passo? (s/n)").lower()
            if op != 's':
                break

            passo_num+=1
            
        fichas.append(nova_ficha)
        salvar_fichas()
        print("Ficha adicionada com sucesso!")

        op = input("Deseja adicionar outra ficha? (s/n)").lower()
        if op != 's':
            break

def visualizar_fichas():
    fichas = carregar_fichas()
    if not fichas:
        print("\nNenhuma ficha cadastrada ainda!")
        return
    
    fichas_por_categoria = {}

    for ficha in fichas:
        categoria = ficha['categoria']
        if categoria not in fichas_por_categoria:
            fichas_por_categoria[categoria] = []
            fichas_por_categoria[categoria].append(ficha)
    
    for categoria, fichas_por_categoria in fichas_por_categoria.items():
        print(f"\n=== CATEGORIA: {categoria.upper()} ===")
        print("-" * (15 + len(categoria)))

    for ficha in fichas_por_categoria:
        print("\n--- FICHA TÉCNICA ---")
        print(f"Nome: {ficha['nome']}")
        
        print(f"\nIngredientes: ")
        for ingred in ficha['ingredientes']:
            print(f"- {ingred['quantidade']} {ingred['ingrediente']}")
                  
        print("\nModo de Preparo: ")
        for passo in ficha['preparo']:
            print(f"{passo['passo']}. {passo['descricao']}")
            print("-" * 40)

# Menu específico (importado peolo main.py)
def menu_fichas():
    fichas = carregar_fichas()
    while True:
        print("\n--- FICHA TÉCNICA ---")
        print("1 - Adicionar Ficha")
        print("2 - Visualizar Fichas")
        print("3 - Editar Ficha")
        print("4 - Excluir Ficha")
        print("0- Voltar")
        op = int(input("Escolha uma opção: "))

        if op == 1:
            adicionar_ficha()
        elif op == 2:
           visualizar_fichas()
        # elif op == 3:
        #    editar_ficha()
        # elif op ==4:
        #     excluir_ficha()
        # elif op == 0:
        #     main()
        else:
            print("opcão invalida.")