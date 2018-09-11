# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("capacity.csv", "r", encoding="utf-8", errors="ignore") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok! File Read.")

print("Linha 0: ")
print(data_list[0])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

i = 1
for row in data_list:
    if i <= 3:
        print (row[5])
        i += 1
