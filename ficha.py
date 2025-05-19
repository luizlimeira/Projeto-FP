# import json
# import os

# ARQUIVO_FICHA = os.path.join(os.path.dirname(__file__), 'ficha.json')
# --------------------------------------------------------------------

def adicionar_ficha():
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
        print("Ficha adicionada com sucesso!")

        op = input("Deseja adicionar outra ficha? (s/n)").lower()
        if op != 's':
            break

# --------------------------------------------------------------------
# def carregar_ficha():
#     if not os.path.exists(ARQUIVO_FICHA):
#         with open(ARQUIVO_FICHA, 'w') as f:
#             json.dump([], f, indent=4)

#     with open(ARQUIVO_FICHA, 'r') as f:
#         return json.load(f)

# def salvar_ficha(ficha):
#     with open(ARQUIVO_FICHA, 'w') as f:
#         json.dump(ficha, f, indent=4, ensure_ascii=False)

# def atualizar_usuario(nome_antigo, novo_nome, nova_idade):
#     usuarios = carregar_usuarios()

#     for usuario in usuarios:
#         if usuario['nome'] == nome_antigo:
#             usuario['nome'] = novo_nome
#             usuario['idade'] = nova_idade
#             break

#     with open(arquivo, 'w') as f:
#         json.dump(usuarios, f, indent=4, ensure_ascii=False)
#     print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")

# def excluir_usuario(nome):
#     usuarios = carregar_usuarios()

#     for usuario in usuarios:  
#         if usuario['nome'] == nome:
#             usuarios.remove(usuario)

#     with open(arquivo, 'w') as f:
#         json.dump(usuarios, f, indent=4, ensure_ascii=False)
#     print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")