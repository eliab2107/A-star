'''
    A busca A* tem uma função de avaliação f(n), que é a soma do custo do caminho já percorrido (g(n)) e a função heurística adotada no problema (h(n))
    A h(n) utilizada para esse caso é a distância em linha reta entre dois pontos, dada pela variável matriz_distancias_linha_reta
    O custo do caminho depende da matriz_distancias_real
'''

def availableFunc(initial: int, lilnode: int, destiny: int):
    global custo_caminho_tempo, linha
    heuristica = matrix_distancias_linha_reta[lilnode-1][destiny-1] / 0.5
    path_cost =  custo_caminho_tempo + matrix_distancias_real[initial-1][lilnode-1] / 0.5
    func = heuristica + path_cost
    if linha not in graph[lilnode][-1] and linha != '':
        func += 4
        path_cost += 4
    return (func,path_cost)

def Astar (initial: int, destiny: int, path_list: list):
    global  custo_caminho_tempo, linha
    if initial == destiny:
        path_list.append(initial)
        return path_list
    else:
        path_list.append(initial)
        no_potenciais = graph[initial][:-1]
        ordem = []
        for node in no_potenciais:
            funcao = availableFunc(initial,node,destiny)
            if ordem == []:
                menorFuncao = funcao[0]
                ordem.append([node,funcao[1]])
            else:
                if menorFuncao >= funcao[0]:
                    menorFuncao = funcao[0]
                    custoPossivel = funcao[1]
                    ordem.insert(0,[node,custoPossivel])
        custo_caminho_tempo = ordem[0][1]
        for lin in graph[initial][-1]: #atualizar linha
            if lin in graph[ordem[0][0]][-1]:
                linha = lin
        return Astar(ordem[0][0],destiny,path_list)

graph = {1 : [2, ('azul')],
         2 : [1, 3, 10, 9, ('azul', 'amarela')],
         3 : [2, 4, 9, 13, ('azul', 'vermelha')],
         4 : [3, 5, 13, 8, ('azul', 'verde')],
         5 : [4, 6, 7, 8, ('azul', 'amarela')],
         6 : [5, ('azul')],
         7 : [5, ('amarela')],
         8 : [4, 5, 9, 12, ('verde', 'amarela')],
         9 : [2, 3, 8, 11, ('vermelha', 'amarela')],
         10 : [2, ('amarela')],
         11 : [9, ('vermelho')],
         12 : [8, ('verde')],
         13 : [3, 4, 14, ('verde', 'vermelho')],
         14 : [13, ('verde')]
}

matrix_distancias_linha_reta = [
    [0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],
    [10, 0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],
    [18.5, 8.5, 0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
    [24.8, 14.8, 6.3, 0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
    [36.4, 26.6, 18.2, 12, 0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
    [38.8, 29.1, 20.6, 14.4, 3, 0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
    [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],
    [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20, 0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6],
    [17.6, 10, 9.4, 12.6, 23.3, 25.7, 23, 8.2, 0, 13.5, 11.2, 10.9, 21.2, 26.6],
    [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0, 17.6, 24.2, 18.7, 21.2],
    [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0, 14.2, 31.5, 35.5],
    [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0, 28.8, 33.6],
    [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0, 5.1],
    [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1, 0]
]

matrix_distancias_real = [
    [-1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [10, -1, 8.5, -1, -1, -1, -1, -1, 10, 3.5, -1, -1, -1, -1],
    [-1, 8.5, -1, 6.3, -1, -1, -1, -1, 9.4, -1, -1, -1, 18.7, -1],
    [-1, -1, 6.3, -1, 13, -1, -1, 15.3, -1, -1, -1, -1, 12.8, -1],
    [-1, -1, -1, 13, -1, 3, 2.4, 30, -1, -1, -1, -1, -1, -1],
    [-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,2.4,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, -1, -1, 15.3, 30, -1, -1, -1, 9.6, -1, -1, 6.4, -1,-1],
    [-1, 10, 9.4, -1, -1, -1, -1, 9.6, -1, -1, 12.2, -1, -1, -1],
    [-1, 3.5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,-1,-1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 12.2, -1, -1, -1,-1,-1],
    [-1, -1, -1, -1, -1, -1, -1, 6.4, -1, -1, -1, -1, -1, -1],
    [-1, -1, 18.7, 12.8, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5.1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5.1, -1]
]


print(graph[9][-1])

initial = int(input())
destiny = int(input())
linha = ''

if initial in graph and destiny in graph: #verificar se o numero digitado pelo usuário está dentro do limite da quantidade de estações
    if initial == destiny:
        custo_caminho_tempo = 0
        print('amor voce ta na mesma estacao se manca bichona')
    else: 
        print('vamos começar seu trajeto!')
        path = []
        custo_caminho_tempo = 4
        resultado = Astar(initial, destiny,path)
        print(resultado)
        print( custo_caminho_tempo)
else:
    print('essa estação nao existe amr')