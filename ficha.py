import json
import os

ARQUIVO_FICHAS = os.path.join(os.path.dirname(__file__), 'ficha.json')

def carregar_fichas():
    if not os.path.exists(ARQUIVO_FICHAS):
        with open(ARQUIVO_FICHAS, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
    
    try:
        with open(ARQUIVO_FICHAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Arquivo de fichas está vazio ou corrompido. Criando novo...")
        with open(ARQUIVO_FICHAS, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
        return []

def salvar_fichas(fichas):
    with open(ARQUIVO_FICHAS, 'w', encoding='utf-8') as f:
        json.dump(fichas, f, indent=4, ensure_ascii=False)

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

        categoria = input("Categoria: ").upper()
        nova_ficha['categoria'] = categoria

        nome = input("Nome: ").capitalize()
        nova_ficha['nome'] = nome

        print("\nINGREDIENTES: ")
        while True:
            ingred = input("Ingrediente (deixe em branco para parar): ").capitalize()
            if not ingred:
                break
            quant = input("Quantidade: ")
            
            nova_ficha['ingredientes'].append({
                'ingrediente': ingred, 
                'quantidade': quant
            })

        print("\nMODO DE PREPARO:")
        passo_num = 1
        while True:
            descricao = input(f"Passo {passo_num} (deixe em branco para parar): ").capitalize()
            if not descricao:
                break
            
            nova_ficha['preparo'].append({
                'passo': passo_num,
                'descricao': descricao
            })
            passo_num += 1
            
        fichas.append(nova_ficha)
        salvar_fichas(fichas)
        print("\nFicha adicionada com sucesso!")

        if input("\nAdicionar outra ficha? (s/n): ").lower() != 's':
            break

    return fichas

def visualizar_fichas(fichas):
    if not fichas:
        print("\nNenhuma ficha cadastrada ainda!")
        return
    
    categorias = {}
    for ficha in fichas:
        if ficha['categoria'] not in categorias:
            categorias[ficha['categoria']] = []
        categorias[ficha['categoria']].append(ficha)
    
    for categoria, fichas_cat in categorias.items():
        print("=" * 90)
        print(f"\n{categoria.upper():^90}")
        print("=" * 90)
        
        for ficha in fichas_cat:
            print(f"\nNome: {ficha['nome']}")
            
            print("\nIngredientes:")
            for ingred in ficha['ingredientes']:
                print(f"- {ingred['quantidade']} de {ingred['ingrediente']}")
            
            print("\nModo de Preparo:")
            for passo in ficha['preparo']:
                print(f"{passo['passo']}. {passo['descricao']}")
                print("-" * 90)

def menu_fichas():
    while True:
        fichas = carregar_fichas()
        
        print("\n--- MENU FICHAS ---")
        print("1. Adicionar Ficha")
        print("2. Visualizar Fichas")
        print("3. Editar Ficha")
        print("4. Excluir Ficha")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            fichas = adicionar_ficha(fichas)
        elif opcao == "2":
            visualizar_fichas(fichas)
        elif opcao == "3":
            print("\nEditar ficha (em desenvolvimento)")
        elif opcao == "4":
            print("\nExcluir ficha (em desenvolvimento)")
        elif opcao == "0":
            return
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    menu_fichas()