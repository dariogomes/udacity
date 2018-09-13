# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import sys

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")


# TAREFA 1
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

for index, row in enumerate(data_list[:20]):
    print("- Amostra {}: {}".format(index + 1, row))

input("Aperte Enter para continuar...")


# TAREFA 2
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for index, row in enumerate(data_list[:20]):
    print("- Gênero da amostra {}: {}".format(index + 1, row[-2]))

input("Aperte Enter para continuar...")


# TAREFA 3
def column_to_list(data, index):
    """Extrai, de uma lista de listas, uma coluna pela posição desejada retornando uma lista com todos os valores.
    Arguments:
        data {list} -- Lista contendo todas as colunas extraídas do arquivo CSV.
        index {int} -- Posição da coluna a ser extraída.
    Returns:
        list -- Lista contendo todos os valores da coluna extraída.
    """

    column_list = []

    for row in data:
        column_list.append(row[index])

    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4

male = 0
female = 0
for row in column_to_list(data_list, -2):
    if row.lower() == "female":
        female += 1
    elif row.lower() == "male":
        male += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Retorna a quantidade de homens e mulheres que utilizaram o serviço.
    Arguments:
        data_list {list} -- Lista contendo os dados completos obtidos do CSV lido.
    Returns:
        list -- Lista contendo a quantidade de homens na primeira posição e de mulheres na segunda posição.
    """

    male = 0
    female = 0

    for row in column_to_list(data_list, -2):
        if row.lower() == "female":
            female += 1
        elif row.lower() == "male":
            male += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """Retorna o gênero mais popular dentre os que utilizaram o serviço.
    Arguments:
        data_list {list} -- Lista contendo os dados completos obtidos do CSV lido.
    Returns:
        string -- "Masculino", "Feminino" ou "Igual".
    """

    male, female = count_gender(data_list)

    if male > female:
        result = "Masculino"
    elif female > male:
        result = "Feminino"
    else:
        result = "Igual"

    return result


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)
