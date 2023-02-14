import time

tempoInicial = time.time() # tempo inicial

matrizDeEntrada = open('matriz.txt').readlines() # ler o arquivo de entrada


pontosDeEntrega = [] 
restaurante = ()
distanciaMinima = 0
melhorPercurso = []

for indiceLinha, item in enumerate(matrizDeEntrada): # percorrer a matriz de entrada e adicionar os pontos de entrega na lista de pontos de entrega
    linha = matrizDeEntrada[indiceLinha].split()
    for indiceColuna in range(len(linha)):
        if linha[indiceColuna] == 'R':
            restaurante = (indiceLinha, indiceColuna, linha[indiceColuna])
        elif linha[indiceColuna] != '0':
            pontosDeEntrega.append((indiceLinha, indiceColuna, linha[indiceColuna])) # adicionar os pontos de entrega na lista de pontos de entrega

def permutarPontosDeEntrega(listaDePontos): # permutar os pontos de entrega para encontrar o melhor caminho com função yield
    if len(listaDePontos) == 1:
        yield listaDePontos
        return
    for percurso in permutarPontosDeEntrega(listaDePontos[1:]):
        for i, _ in enumerate(listaDePontos):
            yield percurso[:i] + listaDePontos[0:1] + percurso[i:]

def inserirRestaurante(percusoSemInicio): # inserir restaurante no começo e no fim do percurso
    percusoSemInicio.insert(0, restaurante)
    percusoSemInicio.append(restaurante)
    return percusoSemInicio

def calcularDistanciaDeDoisPontosEntrega(primeiroPonto, segundoPonto): # calcular a distância entre dois pontos de entrega
  distanciaDaLinha = abs(primeiroPonto[0] - segundoPonto[0])
  distanciaDaColuna = abs(primeiroPonto[1] - segundoPonto[1])
  return distanciaDaLinha + distanciaDaColuna


def somarDistanciasDeUmCaminho(listaDistancia): # somar as distâncias de um caminho
    distancia = 0 
    for i in range(len(listaDistancia) - 1):
        distancia += calcularDistanciaDeDoisPontosEntrega(listaDistancia[i], listaDistancia[i + 1])
    return distancia


for percurso in permutarPontosDeEntrega(pontosDeEntrega): # percorrer todos os caminhos possíveis
    percursoComInicio = inserirRestaurante(percurso)
    distanciaDoPercurso = somarDistanciasDeUmCaminho(percursoComInicio)
    if distanciaDoPercurso < distanciaMinima or distanciaMinima == 0:
        distanciaMinima = distanciaDoPercurso
        melhorPercurso = percursoComInicio


print("Tempo de execução: ", time.time() - tempoInicial) # tempo de execução
print("Distância mínima: ", distanciaMinima) # distância mínima
print("Melhor percurso: ", end="") # melhor percurso
for ponto in melhorPercurso:
    print(ponto[2], end=" ")