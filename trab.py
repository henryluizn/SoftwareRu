import os 
######################### Classes: #########################

class ItemEstoque:

    items = []
    item_len = 0

    def __init__(self, nome_prod, unidade, qtd_estoque, preco):
        self.id = 0
        self.nome_prod = str(nome_prod)
        self.unidade = str(unidade)
        self.qtd_estoque = int(qtd_estoque)
        self.preco = float(preco)

    def setItem(self):
        self.__class__.item_len += 1
        self.id = self.__class__.item_len
        self.__class__.items.append(self)

    def atualizaEstoque(self, id, qtd_estoque):
        self.items[id].qtd_estoque = qtd_estoque

    def __repr__(self):
        return '\n<{}: {} - {} - {} - {} - {}>'.format(self.__class__.__name__, self.id, self.nome_prod, self.unidade, self.qtd_estoque, self.preco)
    
    def getItem(self, id):
        return self.items[id]

    @classmethod
    def all(cls):
        return cls.items


class Estoque:
    
    estoque = []
    estoque_len = 0
    def __init__(self):
        self.estoque = []
    
    def setEstoque(self, item):
        self.estoque.append(item)
        self.__class__.estoque_len += 1

    def getEstoque(self, item_id):
        return self.estoque[item_id]

    def estoqueVazio(self):
        if len(self.estoque) == 0:
            return 0
        else:
            return 1

    def listaEstoque(self):
        for i in range(0, len(self.estoque)):
            print('\n<{}: {} - {} - {} - {} - {}>'.format(self.__class__.__name__, self.estoque[i].id, self.estoque[i].nome_prod, self.estoque[i].unidade, self.estoque[i].qtd_estoque, self.estoque[i].preco))

    @classmethod
    def all(cls):
        return cls.estoque


class Ingredientes:

    ingredients = []
    ingredients_len = 0

    def __init__(self, unidade, qtd_estoque ):
        self.id_ingrediente = 0
        self.unidade = unidade
        self.qtd_estoque = qtd_estoque
        self.item_estoque = None

    def setIngredient(self, item_estoque):
        self.__class__.ingredients_len += 1
        self.id_ingrediente = self.__class__.ingredients_len
        self.item_estoque = item_estoque
        self.__class__.ingredients.append(self)


    def getIngredient(self, id_ingrediente):
        return self.ingredients[id_ingrediente]

    def __repr__(self):
        return '\n<Class{}: id_ingredient{} - {} - {} - nome: {} >'.format(self.__class__.__name__, self.id_ingrediente, self.unidade, self.qtd_estoque, self.item_estoque.nome_prod)

    @classmethod
    def all(cls):
        return cls.ingredients


class Receita:
    
    ingredientes_receita = []
    receita = []
    recec_len = 0

    def __init__(self):
        self.nome = ''
        self.modo_preparo = ''
        self.ingredientes_receita = []
        self.no_porcoes = 0
        self.valor_calorico = 0

    def setReceita(self, nome, modo_preparo, no_porcoes, valor_calorico, ingredientes_receita):
        self.nome = nome
        self.modo_preparo = modo_preparo
        self.no_porcoes = no_porcoes
        self.valor_calorico = valor_calorico
        self.__class__.receita.append(self)
        self.__class__.recec_len += 1
        self.id = self.__class__.recec_len 
        self.ingredientes_receita = ingredientes_receita

    def getReceita(self, id):
        return  self.receita[id]

    def caloriaReceitas(self, id):
        return (self.receita[id].no_porcoes * self.receita[id].valor_calorico)

    def __repr__(self):
        return '\n<{}: {} - {}\n\t{}\n\tporçoes {} \tcalorias p/ porção {} >'.format(self.__class__.__name__, self.id, self.nome, self.modo_preparo, self.no_porcoes, self.valor_calorico)

    @classmethod
    def all(cls):
        return cls.receita


class Refeicao:
    
    refec = []
    receitas = []

    def __init__(self):
        self.qtd_refec = 0
        self.custo_total = 0

    def setRefeicao(self, qtd_refec, custo_total, receitas):
        self.qtd_refec = qtd_refec
        self.custo_total = custo_total
        self.__class__.refec.append(self)
        self.__class__.receitas.append(receitas)

    def getRefeicao(self, id):
        return  self.refec[id]

    def __repr__(self):
        return '\n<Quantidade de refeição: {} - Custo total: R${} {}>'.format(self.__class__.__name__, self.qtd_refec, self.custo_total, self.receitas)

    @classmethod
    def all(cls):
        return cls.refec


class Pedidos:
    refec = []
    receitas = []

    def __init__(self):
        self.qtd_refec = 0
        self.custo_pedido = 0
        self.no_refeicoes = 0
        self.ingredientes = []
        self.id_ingredientes = []
        self.id = 0

    def setPedido(self, refeicao, custo_pedido, ingredientes, id_ingredientes):
        self.qtd_refec = refeicao.qtd_refec
        self.custo_pedido = custo_pedido
        self.id_ingredientes = id_ingredientes
        self.ingredientes = ingredientes
        self.__class__.refec.append(self)
        self.__class__.receitas.append(refeicao.receitas)
        self.id = len(self.__class__.refec)


    def getRefeicao(self, id):
        return  self.refec[id]

    # def __repr__(self):
        # return '<{}: {} - {} - {}>\n'.format(self.__class__.__name__, self.,self.qtd_refec, self.custo_total, self.receitas)


class RU:
    pedidos = []
    refeicoes = []
    receitas = []
    estoque = None

    def __init__(self):
        self.refeicoes = []
        self.pedidos = []
        self.receitas = []
        self.estoque = None
        self.user = 'Administrador'

    def setPedido(self, pedido):
        self.pedidos.append(pedido)

    def setRefeicao(self, refeicao):
        self.refeicoes.append(refeicao)

    def setReceita(self, receita):
        self.receitas.append(receita)

    def setEstoque(self, estoque_att):
        self.estoque = estoque_att

############################################################

# Functions :

def criarItems():
    print('\n\nTELA: CRIAR ITEM\n\n')
    # os.system('clear')
    print('\n\nCriando Itens em estoque')
    print('Vocẽ deve inserir os seguintes dados em ordem:\n\n\tNome do Produto\tENTER\n\tUnidade\tENTER\n\tQuantidade de estoque\tENTER\n\tPreco\tENTER')
    nome_prod = input()
    unidade = input()
    try:
        qtd_estoque = float(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return criarItems()
    try:
        preco = float(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return criarItems()
    # os.system('cls')

    if nome_prod == None or unidade == None:
        print('Preencha todos os campos corretamente')
        return criarItems()

    print('\tNome do produto: {}\n\tUnidade: {}\n\tQuantidade em estoque: {}\n\tPreço: {}\n'.format(nome_prod, unidade, qtd_estoque, preco))
    print('Você confirma a alteração dos dados?\n\t[ 1 ] - Sim\n\t[ 2 ] - Não\n\n\t[ 0 ] - Cancelar operação\n')
    try:
        opcao = int(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return criarItems()

    if opcao == 1:
        if nome_prod == '' or unidade == '' or qtd_estoque == '' or preco == '':
            print('Preencha todos os campos\n\n')
            return criarItems()
        novo_item = ItemEstoque(nome_prod, unidade, qtd_estoque, preco) 
        novo_item.setItem()
        print('\n\n\tEstoque atualizado com sucesso!')
        return novo_item

    elif opcao == 2:
        return criarItems()
    else:
        print('Opção inválida, abortando criação de itens')
        return -1


def criarIngrediente(estoque):

    print('\n\nTELA: CRIAR INGREDIENTE\n\n')
    # os.system('cls')
    if estoque.estoqueVazio() == 0:
        print('Não há itens em seu estoque. Cadastre eles primeiro para poder vincular o ingrediente ao seu respectivo item de estoque\n')
        # os.system('')
        return -1
    print(ItemEstoque.all())
    print('\n\nDigite o ID do item de estoque que você deseja vincular ao ingrediente:\n')
    try:
        item_id = int(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return criarIngrediente(estoque)

    item_estoque = estoque.getEstoque(item_id-1)
    print('Dados do item de estoque escolhido: \n\t\t{}'.format(item_estoque))

    print('Vocẽ deve inserir os seguintes dados em ordem:\n\n\tUnidade\n\tQuantidade de estoque\n')

    unidade = input()

    if unidade == None:
        print('Preencha todos os campos corretamente')
        return  criarIngrediente(estoque)

    try:
        qtd_estoque = float(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return criarIngrediente(estoque)

    # if unidade == '':
    #     print('Preencha todos os campos corretamente')
    #     return criarIngrediente(estoque)

    print('Novo ingrediente a ser criado:')
    print('\tUnidade: {}\n\tQuantidade em estoque: {}\n\tNome do item de estoque vinculado ao ingrediente: {}\n'.format(unidade, qtd_estoque, item_estoque.nome_prod))
    print('Você confirma a inclusão do ingrediente?\n\t[ 1 ] - Sim\n\t[ 2 ] - Não\n\n\t[ 0 ] - Cancelar operação\n')
    try:
        opcao = int(input())
    except ValueError:
        print('Preencha os dados corretamente')
        return criarIngrediente(estoque)

    if opcao == 0:
        print('voce cancelou a operação')
        return -1
    elif opcao == 1:
        # print(item_estoque)

        ingrediente = Ingredientes(unidade, qtd_estoque)
        ingrediente.setIngredient(item_estoque)

        return ingrediente
    elif opcao == 2:
        return criarIngrediente(estoque)
    else:
        pass
    print('INFORMAÇÃO INVÁLIDA')
    return -1


def atualizarEstoque(estoque):
    print('\n\nTELA: ATUALIZAR ESTOQUE\n\n')
    if estoque == None:
        print('O estoque ainda não foi criado')
        return -1

    print('Você deseja criar um novo item ou atualizar um item já criado:\n\t\t[ 1 ] Criar novo item\n\t\t[ 2 ] Atualizar item já criado\n\n\t\t[ 0 ] Cancelar operação\n')
    try:
        opcao = int(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return atualizarEstoque(estoque)

    if opcao == 1:                          # criando novo item
        item = criarItems()
        estoque.setEstoque(item)
        return estoque
    elif opcao == 2:                        # atualizando item já criado
        print(estoque.listaEstoque())
        print('\n\nDigite o ID do item de estoque que você deseja atualizar:\n')

        try:
            item_estoque = int(input())
        except ValueError:
            print('Preencha todos os campos corretamente')
            return atualizarEstoque(estoque)

        print('Vocẽ deve inserir os seguintes dados em ordem:\n\n\tQuantidade de estoque\n')

        try:
            qtd_estoque = int(input())
        except ValueError:
            print('Preencha todos os campos corretamente')
            return atualizarEstoque(estoque)

        item = estoque.getEstoque(item_estoque-1)

        print('Prévia da alteração da quantidade em estoque do produto:\n')
        print('\tNome do produto: {}\n\tUnidade: {}\n\tQuantidade em estoque: {}\n\tPreço: {}\n'.format(item.nome_prod, item.unidade, qtd_estoque, item.preco))
        print('Você confirma a alteração dos dados?\n\t[ 1 ] - Sim\n\t[ 2 ] - Não\n\n\t[ 0 ] - Cancelar operação\n')

        try:
            sub_opcao = int(input())
        except ValueError:
            print('Preencha todos os campos corretamente')
            return atualizarEstoque(estoque)

        if sub_opcao == 1:
            item.atualizaEstoque(item_estoque - 1, qtd_estoque)
            return estoque
        elif sub_opcao == 2:
            return atualizarEstoque(estoque)
        elif sub_opcao == 0:
            print('cancelando a operação')
            return -1

    elif opcao == 0:
        print('cancelando a operação')
        return -1


def exibicoes(estoque, receitas, refeicoes, pedidos):
    print('\n\nTELA : EXIBIÇÕES\n\n')
    os.system('cls')
    print('Escolha a opção desejada:\n\n'
          '\t\t[ 1 ] ESTOQUE\n'
          '\t\t[ 2 ] RECEITAS\n'
          '\t\t[ 3 ] REFEIÇÕES\n'
          '\t\t[ 4 ] PEDIDOS\n'
          '\t\t[ 0 ] voltar para o menu anterior'
          )
    try:
        opcao = int(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return exibicoes(estoque, receitas, refeicoes, pedidos)

    if opcao == 1:
        print('lista de itens em estoque:')
        print(estoque.listaEstoque())
    elif opcao == 2:
        print('lista de receitas')
        print(receitas, '\n')
    elif opcao == 3:
        print('Lista de refeições')
        print(refeicoes, '\n')
    elif opcao == 4:
        print('Lista dos pedidos')
        for ped in pedidos:
            imprimePedido(ped, calculoCaloriasRefeicao(ped.receitas))
    elif opcao == 0:
        return
    else:
        pass


def cadastrarReceita(estoque):

    print('\n\nTELA: CADASTRAR RECEITA\n\n')

    ingrediente_list = []
    receita = Receita()
    receita_ing = None
    cont_ing = 0
    print('Cadastro de receitas\n\n')
    print('Preencha os dados na seguinte ordem:\n\tNome da receita - ENTER\n\tModo de preparo - ENTER\n\tNúmeor de porções - ENTER\n\tValor calórico de uma porção\n')
    nome = input()
    modo_preparo = input()
    try:
        no_porcoes = int(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return cadastrarReceita(estoque)

    try:
        valor_calorico = float(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return cadastrarReceita(estoque)

    if nome == None or modo_preparo == None:
        print('Preencha todos os campos corretamente')
        return cadastrarReceita(estoque)

    print('Deseja incluir ingredientes na receita?\n\t[ 1 ] - Sim\n\t[ 2 ] - Não\n\n\t[ 0 ] - Cancelar operação\n')
    try:
        opcao_principal = int(input())
    except ValueError:
        print('Preencha todos os campos corretamente')
        return cadastrarReceita(estoque)

    if opcao_principal == 1:

        opcao = 1

        while(opcao == 1):

            if opcao == 1:
                receita_ing = criarIngrediente(estoque)
                if receita_ing == -1:
                    print('Não há ingredientes cadastrados, cadastre os ingredientes para criar uma receita')
                    return -1
                else:
                    ingrediente_list.append(receita_ing)
                    # print('Lista de ingrediente atualizada!\n\t', ingrediente_list)
                    cont_ing += 1
                    print('Ingrediente criado com sucesso')
            elif opcao == 0:
                print('Cancelando a operação')
                return -1
            elif opcao == 2:
                pass

            print('Deseja incluir mais ingredientes na receita?\n\t[ 1 ] - Sim\n\t[ 2 ] - Não\n\n\t[ 0 ] - Cancelar operação\n')
            try:
                opcao = int(input())
            except ValueError:
                print('Preencha todos os campos corretamente')
                return cadastrarReceita(estoque)


        if cont_ing >= 1:
            print('Confirma o cadastramento da receita?\n\t[ 1 ] - Sim\n\t[ 2 ] - Não\n\n\t[ 0 ] - Cancelar operação\n')
            try:
                opcao = int(input())
            except:
                print('Preencha todos os campos corretamente')
                return cadastrarReceita(estoque)

            if opcao == 1:
                receita.setReceita(nome, modo_preparo, no_porcoes, valor_calorico, ingrediente_list)
                print('receita cadastrada com sucesso')
                return receita
            elif opcao == 2:
                return cadastrarReceita(estoque)
            elif opcao == 0:
                return -1
        #colocar else: print(não há ingredientes criados na receita) return -1
    elif opcao_principal == 2:
        return cadastrarReceita(estoque)
    else:
        print('Cancelando operação')
        return -1


def calculaCusto(qtd_ref, receitas):

    valor = 0

    for i in range(0, len(receitas)):
        for j in range(0, len(receitas[i].ingredientes_receita)):
            # print('qtd do item de estoque: ',receitas[i].ingredientes_receita[j].item_estoque.qtd_estoque)
            # print('qtd do ingrediente: ', receitas[i].ingredientes_receita[j].qtd_estoque)
            # print('valor de custo do item: ', receitas[i].ingredientes_receita[j].item_estoque.preco)
            temp = (float(receitas[i].ingredientes_receita[j].item_estoque.preco) * float(receitas[i].ingredientes_receita[j].qtd_estoque) * qtd_ref)
            valor += temp
    print('valor total da refeição: R$', valor)
    return valor


def calculoCaloriasRefeicao(receitas):
    calorias = 0
    # calorias da receita = valor calorico * porção
    for i in range(0, len(receitas)):
        print('qtd de calorias da receita por porção: ', receitas[i].valor_calorico)
        temp = int(receitas[i].valor_calorico)
        calorias += temp
    return calorias


def calculoCaloriasReceitas(receitas):
    calorias = 0

    for i in range(0, len(receitas)):
        temp = int(receitas[i].valor_calorico * receitas[i].no_porcoes)
        calorias += temp
    print('O total de calorias de uma receita é: ', calorias)
    return calorias


def calculaCustoTESTE(num_ref, receitas):

    # print('quantidade de ingredientes cadastradas',len(receitas[0].ingredientes_receita))
    # print('ingredientes vinculados a receita',(receitas[0].ingredientes_receita))

    valor = 0
    i = 0
    # for i in range(0, len(receitas)):
    for j in range(0, len(receitas.ingredientes_receita)):
        print('qtd do item de estoque: ',receitas.ingredientes_receita[j].item_estoque.qtd_estoque)
        print('qtd do ingrediente: ', receitas.ingredientes_receita[j].qtd_estoque)
        temp = (int(receitas.ingredientes_receita[j].item_estoque.preco) * int(receitas.ingredientes_receita[j].qtd_estoque) )
        valor += temp
    print('valor total da refeição: ',valor)


def montarRefeicao(estoque, receitas):
    print('\n\nTELA: MONTAR REFEIÇÃO\n\n')

    recei_refec = []

    if receitas == []:
        print('\nNão há receitas cadastradas. Cadastre as receitas para montar uma refeição\n')
        return -1
    sub_opcao = 0
    opcao = 2

    while(opcao == 2):
        print(receitas)
        print('\nEscolha o ID da receita que deseja vincular a essa refeição\n\n\n\t [ 0 ] - Digite para cancelar a operação')
        
        try:
            id = int(input())
        except:
            print('Digite uma opção válida para montar uma refeição')
            return montarRefeicao(estoque, receitas)
        
        if id == 0:
            print('Operação cancelada')
            return -1
        
        recei_refec.append(receitas[id-1])
        
        print('Receitas associadas a essa refeição:\n\n', recei_refec)

        print('\n\nOque você deseja fazer?\n\t[ 1 ] - Finalizar refeição\n\t[ 2 ] - Vincular nova receita a refeição\n\t[ 3 ] - Excluir uma receita da refeição\n\n\t[ 0 ] - Cancelar operação\n')
        try:
            opcao = int(input())
        except:
            print('entrada no formato errado, cancelando caso de uso')
            return montarRefeicao(estoque, receitas)

        if opcao == 1:
            #salva refeicao e gera um pedido
            print('digite o número de refeições')
            try:
                qtd_ref = int(input())
            except:
                print('entrada no formato errado, cancelando caso de uso')
                return montarRefeicao(estoque, receitas)


            qtd_item_estoque, id_item_estoque = calculaIngredientes(recei_refec, estoque, qtd_ref)

            if verificaEstoque(qtd_item_estoque, id_item_estoque, estoque) == 0:
                refeicao = Refeicao()
                pedido = Pedidos()
                custo_refeic = calculaCusto(qtd_ref, recei_refec)
                refeicao.setRefeicao(qtd_ref, custo_refeic, recei_refec)
                # print('quantidade total de calorias de uma refeição; ', calculoCaloriasRefeicao(recei_refec))
                print('items com quantidade ok! Pedido liberado')
                pedido.setPedido(refeicao, custo_refeic, qtd_item_estoque, id_item_estoque)
                imprimePedido(pedido, calculoCaloriasRefeicao(recei_refec))
                liberaEstoque(estoque, qtd_item_estoque, id_item_estoque)
            else:
                print('Há itens em estoque que não possuem a quantidade exigida.\nDeseja atualizar o estoque dos produtos?\n\t[ 1 ] Sim\n\t[ 2 ] Não\nEscolhendo o não, o pedido não será criado')
                opcao_estoque = int(input())
                if opcao_estoque == 1:
                    atualizarEstoque(estoque)
                    print('A refeição deve ser criada novamente para que o pedido seja criado corretamente')
                    return montarRefeicao(estoque, receitas)
                else:
                    return -1
                # atualizarEstoque(estoque)

            return refeicao, pedido
        elif opcao == 0:
            # cancela a operação
            print('Cancelando operação')
            return -1
        elif opcao == 3:
            #   excluindo elementos
            print(recei_refec, '\n\nQual elemento você deseja remover? Digite o seu ID:')
            try:
                element_del = int(input())-1
            except:
                print('entrada inserida errada, tente novamente')
                return -1
                
            print('Você deseja exlcuir o elemento\n\t {}\n\t[ 1 ] - Sim\n\t[ 2 ] - Não\n\n\t[ 0 ] - Cancelar operação\n'.format(recei_refec[element_del-1]))
            try:
                sub_opcao = int(input())
            except:
                print('entrada inserida errada, tente novamente')
                return -1

            if sub_opcao == 0:
                print('Cancelando operação')
                return -1
            elif sub_opcao == 1:
                print('A receita {} foi excluída com sucesso'.format(recei_refec[element_del].nome))
                del recei_refec[element_del]
                print(recei_refec)
        else:
            print('criando nova receita')
            pass


def calculaIngredientes(receitas, estoque, qtd_ref):
    qtd_ing = []
    id_estoque = []
    # k = 0
    for k in range(0, estoque.estoque_len):
        item = estoque.getEstoque(k)
        valor = 0
        for i in range(0, len(receitas)):
            for j in range(0, len(receitas[i].ingredientes_receita)):
                if int(receitas[i].ingredientes_receita[j].item_estoque.id) == int(item.id):
                    valor += float(receitas[i].ingredientes_receita[j].qtd_estoque*qtd_ref)
        qtd_ing.append(float(valor))
        id_estoque.append(int(item.id - 1))
        k += 1
    #
    # print('valor dos ingredientes utilizados: ', qtd_ing)
    # print('id dos itens de estoque', id_estoque)
    return qtd_ing, id_estoque


def verificaEstoque(ingred, id_ingred, estoque):
    estoque_incorreto = 0

    for i in range(0, len(ingred)):
        item = estoque.getEstoque(i)
        if float(item.qtd_estoque) < float(ingred[i]):
            print('O item {} atualmente tem uma quantidade em estoque de {}\nAtualize a quantidade de estoque em +{} para que o pedido tenha a quantidade minima para ser criado corretamente\n'.format(item.nome_prod, item.qtd_estoque, ingred[i] - item.qtd_estoque))
            estoque_incorreto = -1
    return estoque_incorreto


def liberaEstoque(estoque, ingred, id_ingred):

    for i in range(0, len(ingred)):
        item = estoque.getEstoque(id_ingred[i])
        item.atualizaEstoque(int(id_ingred[i]), float(item.qtd_estoque - ingred[i]))


def imprimePedido(pedido, calorias_refeicao):

    print('\n\nTELA: GERA PEDIDO\n\n')
    for i in range(len(pedido)):
        print('Pedido n°: {}\n'.format(pedido.id))
        print('Receitas do pedido: {}\n'.format(pedido.refec[i]))
        print('Quantidade de refeições: {}'.format(pedido.qtd_refec))
        print('Custo da refeição completa: R${}'.format(pedido.custo_pedido))
        print('Calorias de uma refeição completa por pessoa: {} cal'.format(calorias_refeicao))



############################################################

if __name__ == "__main__":
    
    estoque = Estoque()
    #
    # ingrediente_list = []

    movimenta_estoque = 0
    #
    # receitas = []
    #
    # refeicoes = []
    #
    # pedidos = []

    ru = RU()

    opcao_principal = 1


    while opcao_principal != 0:
        # os.system('cls')
        print('\n\nTELA: MENU PRINCIPAL\n\n')
        print('Escolha a opção desejada:\n\n'
            '\t\t[ 1 ] cadastrar receita\n'
            '\t\t[ 2 ] atualizar estoque\n'
            '\t\t[ 3 ] montar refeição\n'
            '\t\t[ 4 ] EXIBIÇÕES\n'
            '\t\t[ 0 ] sair do programa\n'
        )
        try:
            opcao_principal = int(input())
        except ValueError:
            print('opção inválida')

        if opcao_principal == 1:
            print('cadastra receita')
            rec = cadastrarReceita(ru.estoque)
            if rec == -1:
                print('cadastro da receita falhou')
            else:
                # receitas.append(rec)
                ru.setReceita(rec)
                # print(calculaCustoTESTE(5,rec))
                # print(rec)
        elif opcao_principal == 2:
            movimenta_estoque = 1
            print('atualiza o estoque')
            estoque = atualizarEstoque(ru.estoque)
            ru.setEstoque(estoque)
        elif opcao_principal == 3:
            print('monta uma refeição')
            try:
                refeicao, pedido = montarRefeicao(ru.estoque, ru.receitas)
            except TypeError:
                refeicao = -1
                pedido = -1
            if refeicao == -1:
                print('Não foi possível criar a refeição')
            else:
                if pedido == -1:
                    print('não foi possível gerar o pedido devido a erro no preenchimento, cadastre a refeição novamente')
                else:
                    # pedidos.append(pedido)
                    # refeicoes.append(refeicao)
                    ru.setRefeicao(refeicao)
                    ru.setPedido(pedido)
                    # print('lindooooo')
                    # calculaCusto(refeicao.qtd_refec, refeicao.receitas)
                    # retorno_teste, retorno_teste2 = calculaIngredientes(refeicao.receitas, estoque)
                    # pedido.setPedido(refeicao, calculaCusto(refeicao.qtd_refec, refeicao.receitas), retorno_teste, retorno_teste2)

        elif opcao_principal == 4:
            print('exibe os valores')
            exibicoes(ru.estoque, ru.receitas, ru.refeicoes, ru.pedidos)
        elif opcao_principal == 0:
            print('Saindo do programa. Até logo!')
            exit(0)
        else:
            print('insira uma opção válida')
    pass