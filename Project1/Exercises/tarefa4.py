# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

data_list = data_list[1:]

def column_to_list(data, index):
    """
    Função que adiciona as colunas(features) de uma lista em outra lista, na mesma ordem.
      Argumentos:
          data: A lista de dados (list).
          index: O indice da coluna (int).
      Retorna:
          Uma lista com os valores da coluna escolhida pelo indice 'index'
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for sample in data:
        column_list.append(sample[index])
    return column_list

# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
list = column_to_list(data_list, -2)
for gender in list:
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------
