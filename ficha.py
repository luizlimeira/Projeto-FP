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

def editar_fichas(fichas):
    while True:
        ficha_edicao = input("Digite o nome da ficha que você deseja editar: ").strip().lower()
        encontrou = False

        for ficha in fichas:
            if str(ficha['nome']).lower() == ficha_edicao:
                encontrou = True
                print(f"\nEditando ficha: {ficha['nome']}")

                novo_nome = input("Insira o novo nome (pressione enter para manter o atual): ")
                if novo_nome:
                    ficha['nome'] = novo_nome

                nova_categoria = input("Insira a nova categoria (pressione enter para manter a atual): ")
                if nova_categoria:
                    ficha['categoria'] = nova_categoria

                print("\n--- Ingredientes atuais ---")
                for ingred in ficha['ingredientes']:
                    print(f"- {ingred['quantidade']} {ingred['ingrediente']}")

                if input("Deseja editar os ingredientes? (s/n): ").lower() == 's':
                    ficha['ingredientes'] = []
                    while True:
                        ingred = input("Ingrediente (deixe em branco para parar): ").capitalize()
                        if not ingred:
                            break
                        quant = input("Quantidade: ")
            
                        ficha['ingredientes'].append({
                            'ingrediente': ingred, 
                            'quantidade': quant
                        })

                print("\n--- Modo de preparo atual ---")
                for passo in ficha['preparo']:
                    print(f"{passo['passo']}. {passo['descricao']}")
            
                if input("Deseja editar o modo de preparo? (s/n): ").lower() == 's':
                    ficha ['preparo'] = []
                    passo_num = 1
                    while True:
                        descricao = input(f"Passo {passo_num} (deixe em branco para parar): ").capitalize()
                        if not descricao:
                            break
            
                        ficha['preparo'].append({
                            'passo': passo_num,
                            'descricao': descricao
                        })
                        passo_num += 1

                salvar_fichas (fichas)
                print ("\nFicha editada com sucesso!")

        if not encontrou:
            print ("\nFicha não encontrada.")

        continuar = input("\nDeseja editar outra ficha? (s/n): \n").lower()
        if continuar != 's':
            print ("Saindo da edição de fichas.")
            return
            
def excluir_fichas(fichas):
    while True:
        ficha_exclusao = input("Digite o nome da ficha que deseja excluir: ").strip().lower()
        encontrou = False

        for ficha in fichas:
            if str(ficha['nome']).lower() == ficha_exclusao:
                encontrou = True
                print(f"\nFicha: {ficha['nome']}")
                print(f"Categoria: {ficha['categoria']}")
                print("\nIngredientes:")
                for i in ficha['ingredientes']:
                    print(f"- {i['quantidade']} {i['ingrediente']}")
                print("\nModo de Preparo:")
                for p in ficha['preparo']:
                    print(f"{p['passo']}. {p['descricao']}")

                confirmar = input("\nTem certeza que deseja excluir esta ficha? (s/n): ").lower()
                if confirmar == 's':
                    fichas.remove(ficha)
                    salvar_fichas(fichas)
                    print("\nFicha excluída com sucesso.")
                else:
                    print("\nExclusão cancelada.")
                break

        if not encontrou:
            print("\nFicha não encontrada.")

        continuar = input("\nDeseja excluir outra ficha? (s/n): \n").lower()
        if continuar != 's':
            break