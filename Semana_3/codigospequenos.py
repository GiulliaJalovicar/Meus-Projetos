1
# Atividade de pressão! Vamos calcular a área de um hexágono regular.
lado = 8  # O comprimento do lado do hexágono
raiz_3 = 1.732  # Aproximação da raiz quadrada de 3

# Fórmula da área de um hexágono regular: (3√3/2) * lado²
area = (3 * raiz_3 / 2) * (lado ** 2)

# Arredondando a área para 2 casas decimais
area_arredondada = round(area, 2)

# Exibindo o resultado
print("Área do hexágono =", area_arredondada, "cm²")

2
# Hora de filtrar e contar números.
numeros = (2, 5, 8, 9, 12, 15, 18)

# Exibindo os números menores ou iguais a 15
print("Números menores de 15:")
for n in numeros:
    if n <= 15:
        print(n, end=' ')
print()  # Para quebrar a linha

# Contando a quantidade de números pares menores ou iguais a 15
contagem = 0
for n in numeros:
    if n <= 15 and n % 2 == 0:
        contagem += 1

# Exibindo o resultado
print("Quantidade de números pares =", contagem)

3
# Vamos somar os números da lista.
lista = (1, 2)

def soma_lista(lista):
    total = 0
    # Somando todos os números da lista
    for num in lista:
        total += num
    return total

# Exibindo o resultado
print(soma_lista(lista))

4
# Vamos transformar nomes em maiúsculo.
nomes = ('alice', 'bob', 'lucas')

# Criando uma nova tupla com os nomes em maiúsculo
nomes_maiusculo = tuple(nome.upper() for nome in nomes)

# Exibindo os resultados
print(nomes_maiusculo)

5
# Só imprimir números de 0 a 4.
for i in range(5):
    print(i)
