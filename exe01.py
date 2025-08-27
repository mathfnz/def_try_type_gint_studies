# %% 
# Leitura Simples: Escreva um script que abra o ficheiro producao_sensores.csv, leia o seu conteúdo e imprima cada linha no terminal.
import csv

csv_file: str = "base.csv"
# lendo csv
def csv_reader(csv_file_path: str)-> list:
    try:
        with open(csv_file, "r", encoding="UTF-8", newline='') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]
        print(data)
    except FileNotFoundError:
        print(f"Error: the file {csv_file} was not found!")
    except Exception as e:
        print(f"Error: {e}")
    return data
# %%
dados_lidos = csv_reader(csv_file)

# %% 
print(f"Temos {len(dados_lidos)} linhas")

# %%
type(dados_lidos)
find_fails = [row for row in dados_lidos if "Falha" in row]
print(find_fails)

# %%
with open(csv_file, "r", encoding="UTF-8", newline='') as file_dict:
    csv_dict_reader = csv.DictReader(file_dict)
    data_dict = [row for row in csv_dict_reader]
print(f"{data_dict}")

# %%


# %%
temperature_list: list = []

temperature_list = [float(linha['medida_temperatura']) for linha in data_dict]

print(temperature_list)

# %%
# SUM the list temperature_list and take the average
average_tempo = sum(temperature_list) / len(temperature_list)  
print(average_tempo)

# %% find the higher temperature 
higher_temperature: float = max(temperature_list)
print(data_dict)

# %%
percorrendo_lista: list = []

for row in data_dict:
    if float(row['medida_temperatura']) == higher_temperature:
        percorrendo_lista.append(row)

print(percorrendo_lista)
