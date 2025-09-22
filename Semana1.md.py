# Meus-Projetos

import random
import time

# Definindo variáveis iniciais do jogo
# Estoque de recursos e pessoas da vila
estacas = 4           # Número de estacas para proteger o vilarejo
sacos_de_grao = 22    # Quantidade de sacos de grãos
plantacoes = 4        # Número de plantações
ferreiro = 10         # Vida do ferreiro
mineiro = 10          # Vida do mineiro
lenhador = 4          # Vida do lenhador

def combate():
    # Função que simula o combate contra os goblins
    global estacas, plantacoes, ferreiro, mineiro, lenhador

    # Decide se haverá 2 ou 3 invasões de goblins
    r = random.random()
    if r < 0.5:
        invasoes = 2  # Se a probabilidade for menor que 0.5, haverá 2 invasões
    else:
        invasoes = 3  # Se não, haverá 3 invasões

    # Loop para realizar cada invasão
    for i in range(invasoes):
        print(f"\nINVASÃO {i+1}")
        time.sleep(1)

        # Determina o número de goblins (de 2 a 5) para cada invasão
        goblins = int(random.random() * 4) + 2
        print(f"Goblins se aproximando... ({goblins} goblins)")
        time.sleep(1)

        # Loop para simular cada goblin
        for g in range(goblins):
            print(f"\nGOBLIN {g+1}")
            time.sleep(1)

            # Verifica se há estacas restantes
            if estacas > 0:
                # Existe uma chance de a estaca quebrar (30% de chance)
                chance_quebrar = random.random()
                if chance_quebrar <= 0.3:
                    estacas -= 1  # Se a estaca quebrar, diminui o número de estacas
                    print(f"Goblin quebrou uma estaca! Estacas restantes: {estacas}")

                    # Pergunta se o jogador quer enfrentar o goblin
                    luta = input("Goblin avançou! Você quer enfrentar? (s/n) ").strip().lower()
                    if luta == "s":
                        print("Você enfrentou o goblin! que comece a porradaria de cartas!")
                    else:
                        # Caso o jogador não queira lutar, diminui a vida de outros moradores
                        ferreiro -= 1
                        mineiro -= 1
                        lenhador -= 1
                        print("O goblin atacou nossos amigos! (-1 de vida cada)")
                        morte()  # Verifica se algum morador morreu

                        # Existe uma chance de que a plantação seja queimada (5% de chance)
                        if random.random() <= 0.05 and plantacoes > 0:
                            plantacoes -= 1
                            print("Uma plantação foi queimada🔥!")

                else:
                    # Caso a estaca não quebre, o goblin é repelido
                    print("A estaca resistiu bobão!")

            else:
                # Caso não haja estacas restantes, o goblin passa direto
                print("!!!Sem estacas!!! Goblin passou direto!")

                # Pergunta novamente se o jogador quer enfrentar o goblin
                resposta = input("Você quer enfrentar? (s/n) ").strip().lower()
                if resposta == "s":
                    print("Você enfrentou o goblin! que comece a porradaria de cartas!")
                else:
                    # Se o jogador não quiser lutar, diminui a vida dos moradores
                    ferreiro -= 1
                    mineiro -= 1
                    lenhador -= 1
                    print("O goblin atacou nossos amigos! (-1 de vida cada)")
                    morte()  # Verifica se algum morador morreu

                    # Verifica se a plantação pode ser queimada
                    if random.random() <= 0.05 and plantacoes > 0:
                        plantacoes -= 1
                        print("Uma plantação foi queimada🔥!")

def morte():
    # Função que verifica se algum morador morreu
    if ferreiro <= 0:
        print("!!!O Ferreiro morreu!!!")
    if mineiro <= 0:
        print("!!!O Mineiro morreu!!!")
    if lenhador <= 0:
        print("!!!O Lenhador morreu!!!")

# Inicia o combate
combate()

# Resultado final após o combate
print("\n   FIM DO COMBATE   ")
print(f"Estacas restantes: {estacas}")
print(f"Plantações restantes: {plantacoes}")
print(f"Sacos de grão restantes: {sacos_de_grao}")

# Estado final dos moradores
print("Estado final dos moradores:")
print(f"Ferreiro: {max(ferreiro, 0)}")  # Mostra a vida restante do ferreiro (não pode ser negativa)
print(f"Mineiro: {max(mineiro, 0)}")    # Mostra a vida restante do mineiro (não pode ser negativa)
print(f"Lenhador: {max(lenhador, 0)}")  # Mostra a vida restante do lenhador (não pode ser negativa)
